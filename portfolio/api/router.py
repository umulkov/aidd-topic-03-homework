from rest_framework import routers

from .views import PortfolioViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r"portfolios", PortfolioViewSet)
router.register(r"transactions", TransactionViewSet)
