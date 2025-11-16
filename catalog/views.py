from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm
from .models import Product

@login_required
def can_unpublish_product(request, pk):
    """Отмена публикации (доступно только владельцу и модераторам)."""
    product = get_object_or_404(Product, pk=pk)
    product.status = "unpublished"
    product.save()
    messages.warning(request, f"Продукт «{product.name}» снят с публикации.")
    return redirect("catalog:product_detail", pk=product.pk)


class HomeView(ListView):
    """Главная страница — вывод последних 5 товаров."""

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        # возвращаем последние 5 товаров
        return Product.objects.order_by("-created_at")[:5]


class ContactsView(TemplateView):
    """Статическая страница контактов."""

    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    """Детальная страница товара."""

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddProductView(LoginRequiredMixin, CreateView):
    """Добавление продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = "users:login"

    def form_valid(self, form):
        # Привязываем владельца к текущему пользователю
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = "users:login"

    def test_func(self):
        product = self.get_object()
        # Редактировать может владелец или модератор
        return product.owner == self.request.user

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    login_url = "users:login"

    def test_func(self):
        product = self.get_object()
        # Удалять может владелец или модератор
        return (
                product.owner == self.request.user
                or self.request.user.has_perm("catalog.can_unpublish_product")
        )
