from .models import Categorie, Brand, Product
from django.shortcuts import get_object_or_404, get_list_or_404


class Brands:
    def __init__(self):
        self.active_brand = get_list_or_404(Brand.active_objects)


class Cat:
    def __init__(self):
        self.active_category = Categorie.active_objects

    def slug_category(self, category_slug):
        category = get_object_or_404(self.active_category, slug=category_slug)
        return category


class Goods:
    def __init__(self):
        self.active_products = Product.active_objects

    def product_by_slug(self, product_slug):
        product_list = get_object_or_404(self.active_products, slug=product_slug)
        return product_list

    def product_by_category(self, cat_id):
        product = self.active_products.filter(category=cat_id)
        dd = get_list_or_404(product)
        return dd
