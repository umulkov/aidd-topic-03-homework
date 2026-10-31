from config.settings import logger
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, View, UpdateView
from django.views.generic import DetailView
from tinkoff.invest.exceptions import RequestError

from .forms import ShareModelForm
from .models import Portfolio, Share, Transaction
from .services.graph import get_graph
from django.contrib.auth.mixins import UserPassesTestMixin


class IsUserAuthenticatedMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect_to_login(
            self.request.get_full_path(), reverse_lazy("user:login")
        )


class ShareListView(ListView):
    """Список акций"""

    model = Share
    template_name = "dashboard/list.html"
    paginate_by = 100
    ordering = ["name"]


class ShareDetailView(View):
    @staticmethod
    def get(request, pk):
        share = get_object_or_404(Share, id=pk)
        try:
            plot_div = get_graph(share)
        except RequestError as error:
            logger.warning(
                "Could not load historical graph for %s: %s", share.ticker, error
            )
            plot_div = None

        return render(
            request,
            "dashboard/detail.html",
            {"plot_div": plot_div, "share": share},
        )


class ShareCreateView(IsUserAuthenticatedMixin, CreateView):
    """Добавление инструмента"""

    template_name = "dashboard/create.html"
    form_class = ShareModelForm
    success_url = reverse_lazy("dashboard:index")


class ShareUpdateView(IsUserAuthenticatedMixin, UpdateView):
    """Редактирование инструмента"""

    model = Share
    template_name = "dashboard/create.html"
    form_class = ShareModelForm
    success_url = reverse_lazy("dashboard:index")


class ShareDeleteView(IsUserAuthenticatedMixin, DeleteView):
    """Удаление задачи"""

    model = Share
    template_name = "dashboard/delete.html"
    success_url = reverse_lazy("dashboard:index")


class PortfolioListView(IsUserAuthenticatedMixin, ListView):
    model = Portfolio
    template_name = "dashboard/portfolio_list.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)


class PortfolioCreateView(IsUserAuthenticatedMixin, CreateView):
    model = Portfolio
    fields = ["name"]
    template_name = "dashboard/portfolio_form.html"
    success_url = reverse_lazy("dashboard:portfolio_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioDetailView(IsUserAuthenticatedMixin, DetailView):
    model = Portfolio
    template_name = "dashboard/portfolio_detail.html"
    context_object_name = "portfolio"

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.object
        context.update(
            {
                "positions": portfolio.positions(),
                "total_value": portfolio.total_value(),
                "total_cost": portfolio.total_cost(),
                "pnl": portfolio.pnl(),
                "pnl_percent": portfolio.pnl_percent(),
                "transactions": portfolio.transactions.select_related("share"),
            }
        )
        return context


class TransactionCreateView(IsUserAuthenticatedMixin, CreateView):
    model = Transaction
    fields = ["share", "operation", "quantity", "price", "executed_at"]
    template_name = "dashboard/transaction_form.html"

    def get_portfolio(self):
        return get_object_or_404(
            Portfolio, pk=self.kwargs["pk"], user=self.request.user
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["class"] = "form-control"
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio"] = self.get_portfolio()
        return context

    def form_valid(self, form):
        form.instance.portfolio = self.get_portfolio()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:portfolio_detail", kwargs={"pk": self.object.portfolio_id}
        )
