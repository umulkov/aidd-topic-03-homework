from django.conf import settings
from django.db import models

from dashboard.models import Share


class Portfolio(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolios",
    )
    name = models.CharField(max_length=255, verbose_name="Название портфеля")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан")

    class Meta:
        verbose_name = "Портфель"
        verbose_name_plural = "Портфели"

    def __str__(self):
        return self.name

    def _transactions_by_share(self):
        grouped = {}
        for tx in self.transactions.select_related("share").order_by(
            "created_at", "id"
        ):
            grouped.setdefault(tx.share_id, []).append(tx)
        return grouped

    def holdings(self):
        result = []
        for share_id, txs in self._transactions_by_share().items():
            share = txs[0].share
            qty = 0
            cost = 0.0
            for tx in txs:
                if tx.transaction_type == "BUY":
                    cost += tx.quantity * tx.price
                    qty += tx.quantity
                else:
                    if qty > 0:
                        avg = cost / qty
                        sold = min(tx.quantity, qty)
                        cost -= sold * avg
                        qty -= sold
            avg_price = (cost / qty) if qty > 0 else 0.0
            last_price = share.last_price if share.last_price is not None else 0.0
            market_value = qty * last_price
            pnl = market_value - cost
            pnl_percent = (pnl / cost * 100) if cost else 0.0
            result.append(
                {
                    "share": share,
                    "quantity": qty,
                    "avg_price": avg_price,
                    "last_price": last_price,
                    "cost_basis": cost,
                    "market_value": market_value,
                    "pnl": pnl,
                    "pnl_percent": pnl_percent,
                }
            )
        return result

    @property
    def total_cost_basis(self):
        return sum(h["cost_basis"] for h in self.holdings())

    @property
    def total_market_value(self):
        return sum(h["market_value"] for h in self.holdings())

    @property
    def total_pnl(self):
        return self.total_market_value - self.total_cost_basis

    @property
    def total_pnl_percent(self):
        if not self.total_cost_basis:
            return 0.0
        return self.total_pnl / self.total_cost_basis * 100

    @property
    def average_purchase_price(self):
        total_qty = sum(h["quantity"] for h in self.holdings())
        if not total_qty:
            return 0.0
        return self.total_cost_basis / total_qty

    # Aliases
    avg_price = average_purchase_price
    current_value = total_market_value
    total_value = total_market_value
    pnl = total_pnl
    profit_loss = total_pnl
    pnl_percent = total_pnl_percent
    profit_loss_percent = total_pnl_percent


class Transaction(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    TRANSACTION_TYPES = ((BUY, "Покупка"), (SELL, "Продажа"))

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name="transactions"
    )
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=4, choices=TRANSACTION_TYPES, verbose_name="Тип операции"
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.FloatField(verbose_name="Цена за штуку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создана")

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.transaction_type} {self.share.ticker} x{self.quantity}"
