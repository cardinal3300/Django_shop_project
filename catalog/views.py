from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm
from .models import Product


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
    success_url = reverse_lazy("catalog:home")
    login_url = "users:login"


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")
    login_url = "users:login"


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    login_url = "users:login"
