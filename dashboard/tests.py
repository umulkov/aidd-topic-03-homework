from datetime import datetime, timedelta
from types import SimpleNamespace
from unittest.mock import patch

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from grpc import StatusCode
from rest_framework import status
from rest_framework.test import APITestCase
from tinkoff.invest.exceptions import RequestError

from dashboard.models import Portfolio, Share, Transaction
from dashboard.services.market_data import compute_trend, get_last_data


class DashboardTests(APITestCase):
    def setUp(self) -> None:
        self.apple_share = Share.objects.create(
            figi="BBG000B9XRY4",
            isin="US0378331005",
            name="Apple",
            ticker="AAPL",
            currency="usd",
            uid="a9eb4238-eba9-488c-b102-b6140fd08e38",
            last_price=100.50,
            is_trend_high=True,
        )
        self.api_user = get_user_model().objects.create_user(
            username="api-user", password="test-password"
        )

        self.second_company = {
            "figi": "BBG000B9XRY5",
            "isin": "US0378331004",
            "name": "Company_test",
            "ticker": "TESTTEST",
            "currency": "usd",
            "uid": "a9eb4238-eba9-488c-b102-b6140fd08e39",
            "last_price": 1.50,
            "is_trend_high": False,
        }

    def test_positions_aggregates_buy_and_sell(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="Main")
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="buy",
            quantity=10,
            price=10,
        )
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="buy",
            quantity=5,
            price=20,
        )
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="sell",
            quantity=3,
            price=15,
        )

        position = portfolio.positions()[0]
        self.assertEqual(position["quantity"], 12)
        self.assertAlmostEqual(position["avg_buy_price"], 200 / 15)
        self.assertEqual(position["last_price"], self.apple_share.last_price)
        self.assertEqual(position["value"], 12 * self.apple_share.last_price)
        self.assertAlmostEqual(position["cost"], 160)

    def test_empty_portfolio_zero(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="Empty")

        self.assertEqual(portfolio.total_value(), 0)
        self.assertEqual(portfolio.total_cost(), 0)
        self.assertEqual(portfolio.pnl(), 0)
        self.assertIsNone(portfolio.pnl_percent())

    def test_sell_exceeds_buy_position_hidden(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="Over-sold")
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="buy",
            quantity=2,
            price=10,
        )
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="sell",
            quantity=3,
            price=15,
        )

        self.assertEqual(portfolio.positions(), [])
        self.assertEqual(portfolio.total_value(), 0)

    def test_pnl_percent_only_when_cost_positive(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="Sales only")
        Transaction.objects.create(
            portfolio=portfolio,
            share=self.apple_share,
            operation="sell",
            quantity=1,
            price=15,
        )

        self.assertEqual(portfolio.total_cost(), 0)
        self.assertIsNone(portfolio.pnl_percent())

    def test_portfolio_list_requires_auth(self):
        response = self.client.get("/api/v1/portfolios/")

        self.assertIn(
            response.status_code,
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN),
        )

    def test_portfolio_list_only_own(self):
        Portfolio.objects.create(user=self.api_user, name="User A portfolio")
        user_b = get_user_model().objects.create_user(
            username="user-b", password="test-password"
        )
        self.client.force_authenticate(user=user_b)

        response = self.client.get("/api/v1/portfolios/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"], [])

    def test_transaction_create_for_own_portfolio(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="Owned")
        self.client.force_authenticate(user=self.api_user)

        response = self.client.post(
            "/api/v1/transactions/",
            {
                "portfolio": portfolio.pk,
                "share": self.apple_share.pk,
                "operation": "buy",
                "quantity": 2,
                "price": 10.5,
            },
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["portfolio"], portfolio.pk)

    def test_transaction_create_for_foreign_portfolio(self):
        portfolio = Portfolio.objects.create(user=self.api_user, name="User A")
        user_b = get_user_model().objects.create_user(
            username="user-b", password="test-password"
        )
        self.client.force_authenticate(user=user_b)

        response = self.client.post(
            "/api/v1/transactions/",
            {
                "portfolio": portfolio.pk,
                "share": self.apple_share.pk,
                "operation": "buy",
                "quantity": 2,
                "price": 10.5,
            },
            format="json",
        )

        self.assertIn(
            response.status_code,
            (status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN),
        )

    def test_portfolio_list_redirects_anonymous(self):
        response = self.client.get("/portfolio/")

        self.assertRedirects(
            response,
            "/user/login/?next=%2Fportfolio%2F",
            fetch_redirect_response=False,
        )

    def test_portfolio_detail_own(self):
        html_user = get_user_model().objects.create_user(
            username="htmluser", password="htmlpass123"
        )
        self.portfolio = Portfolio.objects.create(user=html_user, name="My Portfolio")
        self.assertTrue(self.client.login(username="htmluser", password="htmlpass123"))

        response = self.client.get(
            reverse("dashboard:portfolio_detail", args=[self.portfolio.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.portfolio.name)
        self.assertIn("P&L", response.content.decode().replace("&amp;", "&"))

    def test_user_urls_have_trailing_slash(self):
        self.assertEqual(reverse("user:login"), "/user/login/")
        self.assertEqual(reverse("user:registration"), "/user/registration/")
        self.assertEqual(reverse("user:logout"), "/user/logout/")

    def test_celery_schedule_name_matches_interval(self):
        from config.celery import app as celery_app

        schedule = celery_app.conf.beat_schedule
        self.assertIn("update-last-price-every-10s", schedule)
        self.assertEqual(schedule["update-last-price-every-10s"]["schedule"], 10.0)

    def test_share_create_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse("dashboard:create"))
        self.assertRedirects(
            response, "/user/login/?next=%2Fcreate", fetch_redirect_response=False
        )

    def test_share_list_html(self):
        response = self.client.get(reverse("dashboard:index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_share_list(self):
        response = self.client.get("/api/v1/shares/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        apple_share = response.json().get("results")[0]
        self.assertEqual(apple_share["id"], self.apple_share.id)
        self.assertEqual(apple_share["figi"], self.apple_share.figi)
        self.assertEqual(apple_share["isin"], self.apple_share.isin)
        self.assertEqual(apple_share["name"], self.apple_share.name)
        self.assertEqual(apple_share["ticker"], self.apple_share.ticker)
        self.assertEqual(apple_share["currency"], self.apple_share.currency)

    def test_share_detail(self):
        response = self.client.get("/api/v1/shares/")
        share_detail = response.json().get("results")[0]
        response = self.client.get(f"/api/v1/shares/{share_detail['id']}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_share_detail_invalid(self):
        response = self.client.get("/api/v1/shares/2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_share_page_detail_missing_returns_404(self):
        response = self.client.get("/999999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_share_detail_renders_when_tinkoff_graph_is_unavailable(self):
        error = RequestError(
            StatusCode.UNAVAILABLE, "self-signed certificate in certificate chain", None
        )
        with (
            patch("dashboard.views.get_graph", side_effect=error),
            self.assertLogs("main", level="WARNING") as captured,
        ):
            response = self.client.get(
                reverse("dashboard:detail", args=[self.apple_share.pk])
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.apple_share.name)
        self.assertContains(response, "Исторический график временно недоступен")
        self.assertNotContains(response, "self-signed certificate")
        self.assertIn("AAPL", captured.output[0])

    def test_last_price_keeps_fractional_part(self):
        response = SimpleNamespace(
            last_prices=[
                SimpleNamespace(
                    price=SimpleNamespace(units=12, nano=345_000_000),
                    time=datetime(2026, 1, 1),
                )
            ]
        )
        with patch("dashboard.services.market_data.Client") as client_class:
            client_class.return_value.__enter__.return_value.market_data.get_last_prices.return_value = (
                response
            )
            price, _ = get_last_data(self.apple_share)

        self.assertAlmostEqual(price, 12.345)

    def test_compute_trend_compares_prices(self):
        self.assertTrue(compute_trend(100.0, 100.0))
        self.assertFalse(compute_trend(100.0, 99.99))

    def test_compute_trend_without_previous_price_logs_and_returns_none(self):
        with self.assertLogs("main", level="WARNING") as captured:
            result = compute_trend(None, 100.0, "AAPL")

        self.assertIsNone(result)
        self.assertIn("no previous price for AAPL, skipping trend", captured.output[0])

    def test_graph_keeps_fractional_candle_price(self):
        candle = SimpleNamespace(
            time=datetime(2026, 1, 1),
            close=SimpleNamespace(units=12, nano=345_000_000),
        )
        with (
            patch("dashboard.services.graph.Client") as client_class,
            patch("dashboard.services.graph.plot", return_value="graph"),
            patch("dashboard.services.graph.Scatter") as scatter,
        ):
            client_class.return_value.__enter__.return_value.get_all_candles.return_value = [
                candle
            ]
            from dashboard.services.graph import get_graph

            self.assertEqual(get_graph(self.apple_share), "graph")

        self.assertAlmostEqual(scatter.call_args.kwargs["y"][0], 12.345)

    def test_last_price_float_field_preserves_fractional_value(self):
        self.apple_share.last_price = 100.125
        self.apple_share.save(update_fields=["last_price"])
        self.apple_share.refresh_from_db()
        self.assertAlmostEqual(self.apple_share.last_price, 100.125)

    def test_price_task_skips_trend_when_previous_price_is_missing(self):
        from dashboard.tasks import update_last_price

        self.apple_share.last_price = None
        self.apple_share.save(update_fields=["last_price"])
        with patch("dashboard.tasks.get_last_data", return_value=[101.25, None]):
            with self.assertLogs("main", level="WARNING") as captured:
                update_last_price.run()

        self.apple_share.refresh_from_db()
        self.assertAlmostEqual(self.apple_share.last_price, 101.25)
        self.assertIsNone(self.apple_share.is_trend_high)
        self.assertIn("no previous price for AAPL, skipping trend", captured.output[0])

    def test_price_task_updates_updated_at(self):
        from dashboard.tasks import update_last_price

        old_updated_at = timezone.now() - timedelta(days=1)
        Share.objects.filter(pk=self.apple_share.pk).update(updated_at=old_updated_at)
        with patch("dashboard.tasks.get_last_data", return_value=[101.25, None]):
            with patch.object(
                Share.objects, "bulk_update", wraps=Share.objects.bulk_update
            ) as bulk_update:
                update_last_price.run()

        self.apple_share.refresh_from_db()
        self.assertGreater(self.apple_share.updated_at, old_updated_at)
        bulk_update.assert_called_once_with(
            [self.apple_share], ["last_price", "is_trend_high", "updated_at"]
        )

    def test_share_update(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.get("/api/v1/shares/")
        share_detail = response.json().get("results")[0]
        response = self.client.put(
            f"/api/v1/shares/{share_detail['id']}/",
            {
                "id": share_detail["id"],
                "figi": self.apple_share.figi,
                "isin": self.apple_share.isin,
                "name": f"{self.apple_share.name}_test",
                "ticker": self.apple_share.ticker,
                "currency": self.apple_share.currency,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertEqual(body["figi"], self.apple_share.figi)
        self.assertEqual(body["name"], f"{self.apple_share.name}_test")

    def test_share_update_invalid(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.get("/api/v1/shares/")
        share_detail = response.json().get("results")[0]
        response = self.client.put(
            f"/api/v1/shares/{share_detail['id']}/",
            {
                "figi": self.apple_share.figi,
                "name": f"{self.apple_share.name}_test",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_share_create(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.post(
            "/api/v1/shares/", self.second_company, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        body = response.json()
        self.assertEqual(body["figi"], self.second_company["figi"])
        self.assertEqual(body["name"], self.second_company["name"])
        self.assertEqual(body["ticker"], self.second_company["ticker"])

        response = self.client.get("/api/v1/shares/")
        self.assertEqual(len(response.data["results"]), 2)

    def test_share_create_invalid(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.post(
            "/api/v1/shares/", {"figi": "BBG000B9XRY5"}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_share_delete(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.get("/api/v1/shares/")
        share_detail = response.json().get("results")[0]
        response = self.client.delete(f"/api/v1/shares/{share_detail['id']}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get("/api/v1/shares/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 0)

    def test_share_delete_invalid(self):
        self.client.force_authenticate(user=self.api_user)
        response = self.client.delete("/api/v1/shares/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_share_create_requires_authentication(self):
        response = self.client.post(
            "/api/v1/shares/", self.second_company, format="json"
        )
        self.assertIn(
            response.status_code,
            (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN),
        )
