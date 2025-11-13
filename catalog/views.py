from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm
from .models import Product


@permission_required("catalog.can_unpublish_product", raise_exception=True)
def unpublish_product(request, pk):
    """Отмена публикации (доступно только модератору)."""
    product = get_object_or_404(Product, pk=pk)
    product.status = "unpublished"
    product.save()
    messages.warning(request, f"Продукт «{product.name}» снят с публикации.")
    return redirect("catalog:product_detail", pk=pk)


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


class AddProductView(LoginRequiredMixin, CreateView):
    """Добавление продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = "users:login"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    login_url = "users:login"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    login_url = "users:login"
