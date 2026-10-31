from rest_framework import permissions, viewsets

from ..models import Portfolio, Transaction
from ..serializers import PortfolioSerializer, TransactionSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Portfolio.objects.none()

    def get_queryset(self):
        return Portfolio.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Transaction.objects.none()

    def get_queryset(self):
        return Transaction.objects.filter(portfolio__owner=self.request.user)
