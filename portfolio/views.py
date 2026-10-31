from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from dashboard.models import Share
from .forms import PortfolioForm, TransactionForm
from .models import Portfolio, Transaction


class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = "portfolio/list.html"
    context_object_name = "portfolios"

    def get_queryset(self):
        return Portfolio.objects.filter(owner=self.request.user)


class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = "portfolio/create.html"
    success_url = reverse_lazy("portfolio:list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PortfolioDetailView(LoginRequiredMixin, DetailView):
    model = Portfolio
    template_name = "portfolio/detail.html"
    context_object_name = "portfolio"

    def get_queryset(self):
        return Portfolio.objects.filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = self.object
        context["transactions"] = portfolio.transactions.all()
        context["holdings"] = portfolio.holdings()
        context["transaction_form"] = TransactionForm()
        context["shares"] = Share.objects.all().order_by("name")
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = TransactionForm(request.POST)
        if form.is_valid():
            tx = form.save(commit=False)
            tx.portfolio = self.object
            tx.save()
            return redirect("portfolio:detail", pk=self.object.pk)
        context = self.get_context_data()
        context["transaction_form"] = form
        return render(request, self.template_name, context)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = "portfolio/transaction_create.html"

    def dispatch(self, request, *args, **kwargs):
        self.portfolio = get_object_or_404(
            Portfolio, pk=kwargs["pk"], owner=request.user
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.portfolio = self.portfolio
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("portfolio:detail", kwargs={"pk": self.portfolio.pk})
