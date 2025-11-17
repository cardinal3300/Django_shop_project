from .models import Product


def get_products_by_category(category_id: int):
    """Возвращает список продуктов по ID категории."""
    return Product.objects.filter(category_id=category_id, status="published")
