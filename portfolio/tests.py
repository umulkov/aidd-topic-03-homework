from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from dashboard.models import Share
from .models import Portfolio, Transaction

User = get_user_model()


class PortfolioAccessTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="user1", email="user1@example.com", password="password"
        )
        self.other = User.objects.create_user(
            username="user2", email="user2@example.com", password="password"
        )
        self.portfolio = Portfolio.objects.create(owner=self.user, name="My Portfolio")
        self.client = Client()
        self.client.login(username="user1", password="password")

    def test_create_portfolio(self):
        response = self.client.post(
            reverse("portfolio:create"), {"name": "Second"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Portfolio.objects.filter(owner=self.user, name="Second").exists()
        )

    def test_add_transaction(self):
        share = Share.objects.create(
            figi="FIGI1", isin="ISIN1", name="Apple", ticker="AAPL",
            currency="usd", uid="uid-1", last_price=150.0,
        )
        response = self.client.post(
            reverse("portfolio:detail", args=[self.portfolio.id]),
            {
                "share": share.id,
                "transaction_type": Transaction.BUY,
                "quantity": 10,
                "price": 100.0,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.portfolio.transactions.count(), 1)

    def test_foreign_portfolio_returns_404(self):
        other_portfolio = Portfolio.objects.create(
            owner=self.other, name="Other"
        )
        response = self.client.get(
            reverse("portfolio:detail", args=[other_portfolio.id])
        )
        self.assertEqual(response.status_code, 404)


class PortfolioCalculationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="calc", email="calc@example.com", password="password"
        )
        self.portfolio = Portfolio.objects.create(owner=self.user, name="Calc")
        self.share = Share.objects.create(
            figi="FIGI2", isin="ISIN2", name="Test", ticker="TEST",
            currency="usd", uid="uid-2", last_price=120.0,
        )

    def test_average_price_and_pnl(self):
        Transaction.objects.create(
            portfolio=self.portfolio, share=self.share,
            transaction_type=Transaction.BUY, quantity=10, price=100.0,
        )
        Transaction.objects.create(
            portfolio=self.portfolio, share=self.share,
            transaction_type=Transaction.BUY, quantity=10, price=120.0,
        )
        Transaction.objects.create(
            portfolio=self.portfolio, share=self.share,
            transaction_type=Transaction.SELL, quantity=5, price=130.0,
        )
        h = self.portfolio.holdings()[0]
        self.assertEqual(h["quantity"], 15)
        self.assertAlmostEqual(h["avg_price"], 110.0)
        self.share.last_price = 120.0
        self.share.save()
        h2 = self.portfolio.holdings()[0]
        self.assertAlmostEqual(h2["market_value"], 15 * 120.0)
        self.assertAlmostEqual(h2["pnl"], 15 * 120.0 - 1650.0)
        self.assertAlmostEqual(self.portfolio.total_pnl_percent, (1800 - 1650) / 1650 * 100)

    def test_mocked_last_price(self):
        Transaction.objects.create(
            portfolio=self.portfolio, share=self.share,
            transaction_type=Transaction.BUY, quantity=4, price=50.0,
        )
        self.share.last_price = 60.0
        self.share.save()
        self.assertAlmostEqual(self.portfolio.total_market_value, 4 * 60.0)
        self.assertAlmostEqual(self.portfolio.total_pnl, 4 * 60.0 - 4 * 50.0)
        self.assertAlmostEqual(self.portfolio.total_pnl_percent, 20.0)
