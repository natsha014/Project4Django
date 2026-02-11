from django.core.cache import cache
from .models import Product
from config import settings


def get_products_by_category(category_id):
    """Возвращает список опубликованных продуктов конкретной категории."""

    if not settings.CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id, is_published=True)

    key = f'products_list_category_{category_id}'

    products = cache.get(key)

    if products is None:
        products = list(Product.objects.filter(category__id=category_id, is_published=True))
        cache.set(key, products, 60)

    return products
