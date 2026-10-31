from django.conf import settings
from django.db import models
from django.utils import timezone


class Share(models.Model):
    """Акция"""

    figi = models.CharField(max_length=255, unique=True)
    isin = models.CharField(max_length=255)
    name = models.CharField(max_length=255, verbose_name="Наименование компании")
    ticker = models.CharField(max_length=10, unique=True, verbose_name="Тикер")
    currency = models.CharField(max_length=20, verbose_name="Валюта")
    uid = models.CharField(max_length=255, unique=True)
    last_price = models.FloatField(blank=True, null=True, verbose_name="Текущая цена")
    is_trend_high = models.BooleanField(
        blank=True, null=True, verbose_name="Растет цена"
    )
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"


class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "name"),)
        ordering = ["name"]

    def positions(self):
        totals = {}
        for transaction in self.transactions.select_related("share"):
            position = totals.setdefault(
                transaction.share_id,
                {
                    "share": transaction.share,
                    "buy_quantity": 0,
                    "buy_cost": 0.0,
                    "sell_quantity": 0,
                },
            )
            if transaction.operation == "buy":
                position["buy_quantity"] += transaction.quantity
                position["buy_cost"] += transaction.price * transaction.quantity
            else:
                position["sell_quantity"] += transaction.quantity

        positions = []
        for total in totals.values():
            quantity = total["buy_quantity"] - total["sell_quantity"]
            if quantity <= 0:
                continue

            avg_buy_price = (
                total["buy_cost"] / total["buy_quantity"]
                if total["buy_quantity"]
                else None
            )
            last_price = total["share"].last_price
            positions.append(
                {
                    "share": total["share"],
                    "quantity": quantity,
                    "avg_buy_price": avg_buy_price,
                    "last_price": last_price,
                    "value": quantity * last_price if last_price is not None else None,
                    "cost": quantity * avg_buy_price
                    if avg_buy_price is not None
                    else 0,
                }
            )
        return positions

    def total_value(self):
        return sum(
            position["value"]
            for position in self.positions()
            if position["value"] is not None
        )

    def total_cost(self):
        return sum(position["cost"] for position in self.positions())

    def pnl(self):
        return self.total_value() - self.total_cost()

    def pnl_percent(self):
        total_cost = self.total_cost()
        return self.pnl() / total_cost * 100 if total_cost > 0 else None


class Transaction(models.Model):
    OPERATION_CHOICES = [("buy", "Buy"), ("sell", "Sell")]

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="transactions"
    )
    share = models.ForeignKey(Share, on_delete=models.PROTECT)
    operation = models.CharField(max_length=4, choices=OPERATION_CHOICES)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    executed_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-executed_at", "-id"]
