from django.shortcuts import render, get_object_or_404
from .models import Product


def home(request):
    """
    Контроллер для отображения домашней страницы.
    Возвращает шаблон home.html.
    """
    return render(request, 'catalog/home.html')


def contacts(request):
    """
    Контроллер для отображения страницы с контактной информацией.
    """
    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    """
    Контроллер для отображения подробной информации о товаре.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
