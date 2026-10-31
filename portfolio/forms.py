from django import forms

from .models import Portfolio, Transaction


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ("name",)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("share", "transaction_type", "quantity", "price")
