from django_filters import rest_framework as filters
from rest_framework.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from dashboard.models import Portfolio, Share, Transaction

from .serializer import PortfolioSerializer, ShareSerializer, TransactionSerializer


class ShareFilter(filters.FilterSet):
    class Meta:
        model = Share
        fields = ("name", "ticker")


class ShareViewSet(viewsets.ModelViewSet):
    serializer_class = ShareSerializer
    queryset = Share.objects.all()
    filter_backends = (OrderingFilter, filters.DjangoFilterBackend, SearchFilter)
    filterset_class = ShareFilter
    ordering_fields = ["name", "ticker"]
    search_fields = ["$name"]


class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.select_related("share", "portfolio").all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(portfolio__user=self.request.user)

    def perform_create(self, serializer):
        portfolio = serializer.validated_data["portfolio"]
        if portfolio.user_id != self.request.user.id:
            raise PermissionDenied("You do not own this portfolio.")
        serializer.save()
