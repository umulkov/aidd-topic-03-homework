from rest_framework import serializers

from .models import Portfolio, Transaction


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ("id", "name", "created_at", "owner")
        read_only_fields = ("id", "created_at", "owner")


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "portfolio",
            "share",
            "transaction_type",
            "quantity",
            "price",
            "created_at",
        )
        read_only_fields = ("id", "created_at")

    def validate_portfolio(self, value):
        request = self.context.get("request")
        if request and value.owner != request.user:
            raise serializers.ValidationError("Not your portfolio.")
        return value
