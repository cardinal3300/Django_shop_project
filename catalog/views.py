from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProductForm
from .models import Product


class ContactsView(TemplateView):
    """Статическая страница контактов."""

    template_name = "catalog/contacts.html"
    success_url = reverse_lazy("catalog:home")


class ProductListView(ListView):
    """
    Главная страница — вывод последних 5 товаров.
    Контекст: 'products' (в шаблоне ожидается именно этот ключ).
    """

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        # возвращаем последние 5 товаров
        return Product.objects.order_by("-created_at")[:5]


class ProductDetailView(DetailView):
    """
    Детальная страница товара.
    В шаблоне доступен объект product (context_object_name).
    """

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    """
    Форма добавления продукта.
    Используем ProductForm (ModelForm) — он должен содержать поле purchase_price.
    """

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    """Форма обновления продукта."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_update.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    """Форма удаления продукта."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
