from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Product
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    """
    Главная страница — вывод последних 5 товаров.
    Контекст: 'products' (в шаблоне ожидается именно этот ключ).
    """
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        # возвращаем последние 5 товаров
        return Product.objects.order_by('-created_at')[:5]


class ContactsView(TemplateView):
    """
    Статическая страница контактов. Если нужна обработка формы — можно заменить
    на View и переопределить post/get.
    """
    template_name = 'catalog/contacts.html'


class ProductDetailView(DetailView):
    """
    Детальная страница товара.
    В шаблоне доступен объект product (context_object_name).
    """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class AddProductView(LoginRequiredMixin, CreateView):
    """
    Форма добавления продукта.
    Используем ProductForm (ModelForm) — он должен содержать поле purchase_price.
    """
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'
    success_url = reverse_lazy('catalog:home')
    login_url = 'users:login'

