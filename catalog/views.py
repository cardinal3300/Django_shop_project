from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def home(request):
    """
    Контроллер для отображения домашней страницы.
    Возвращает шаблон home.html.
    """
    # Получаем последние 5 товаров по дате создания
    products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'catalog/home.html', {'products': products})


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


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')  # после сохранения — на главную
    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})
