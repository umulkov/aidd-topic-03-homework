from django.urls import include, path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.PortfolioListView.as_view(), name="list"),
    path("create/", views.PortfolioCreateView.as_view(), name="create"),
    path("<int:pk>/", views.PortfolioDetailView.as_view(), name="detail"),
    path("api/", include("portfolio.api.urls")),
]
