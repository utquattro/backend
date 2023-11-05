from .models import Categorie, Brand, Product, ProductSku
from django.shortcuts import get_object_or_404, get_list_or_404


class Brands:
    def __init__(self):
        self.active_brand = Brand.active_objects


class Cat:
    def __init__(self):
        self.active_category = Categorie.active_objects

    def slug_category(self, category_slug):
        return get_object_or_404(self.active_category, slug=category_slug)

    def list_category(self):
        return get_list_or_404(self.active_category)


class Goods:
    def __init__(self):
        self.active_products = Product.active_objects
        self.active_sku = ProductSku.active_objects

    def products_by_category_slug(self, category_slug):
        queryset = get_list_or_404(self.active_products.filter(category__slug=category_slug))
        return queryset

    def slug_product(self, product_slug, category_slug):
        product = get_object_or_404(self.active_products, slug=product_slug, category__slug =category_slug)
        return product
