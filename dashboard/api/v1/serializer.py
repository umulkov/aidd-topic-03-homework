from rest_framework import serializers

from dashboard.models import Portfolio, Share, Transaction


class PortfolioSerializer(serializers.ModelSerializer):
    total_value = serializers.FloatField(read_only=True)
    total_cost = serializers.FloatField(read_only=True)
    pnl = serializers.FloatField(read_only=True)
    pnl_percent = serializers.FloatField(read_only=True, allow_null=True)

    class Meta:
        model = Portfolio
        fields = (
            "id",
            "name",
            "created_at",
            "total_value",
            "total_cost",
            "pnl",
            "pnl_percent",
        )
        read_only_fields = (
            "id",
            "created_at",
            "total_value",
            "total_cost",
            "pnl",
            "pnl_percent",
        )


class TransactionSerializer(serializers.ModelSerializer):
    portfolio = serializers.PrimaryKeyRelatedField(queryset=Portfolio.objects.all())
    share = serializers.PrimaryKeyRelatedField(queryset=Share.objects.all())

    class Meta:
        model = Transaction
        fields = (
            "id",
            "portfolio",
            "share",
            "operation",
            "quantity",
            "price",
            "executed_at",
        )
        read_only_fields = ("id",)


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = (
            "id",
            "figi",
            "isin",
            "name",
            "ticker",
            "currency",
            "last_price",
            "is_trend_high",
            "updated_at",
        )
