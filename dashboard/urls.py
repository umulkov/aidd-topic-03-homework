from django.urls import include, path

from dashboard.views import (
    ShareCreateView,
    ShareDeleteView,
    ShareDetailView,
    ShareListView,
    ShareUpdateView,
    PortfolioCreateView,
    PortfolioDetailView,
    PortfolioListView,
    TransactionCreateView,
)

app_name = "dashboard"

urlpatterns = [
    path("", ShareListView.as_view(), name="index"),
    path("<int:pk>", ShareDetailView.as_view(), name="detail"),
    path("create", ShareCreateView.as_view(), name="create"),
    path("update/<int:pk>", ShareUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", ShareDeleteView.as_view(), name="delete"),
    path("portfolio/", PortfolioListView.as_view(), name="portfolio_list"),
    path(
        "portfolio/create/",
        PortfolioCreateView.as_view(),
        name="portfolio_create",
    ),
    path(
        "portfolio/<int:pk>/",
        PortfolioDetailView.as_view(),
        name="portfolio_detail",
    ),
    path(
        "portfolio/<int:pk>/transaction/add/",
        TransactionCreateView.as_view(),
        name="transaction_create",
    ),
    path("api/", include("dashboard.api.urls")),
]
