from .models import Categorie, Brand, ProductSku
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import  ProductSkuSerializer

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
        self.active_products = ProductSku.active_objects
        self.active_sku = ProductSku.active_objects

    def products_by_category_slug(self, category_slug):
        queryset = get_list_or_404(self.active_products.filter(category__slug=category_slug))
        return queryset

    def find_products_by_text(self, src_text):
        queryset = get_list_or_404(self.active_sku.filter(title__icontains=src_text))
        return queryset

    def get_product_by_slug(self, product_slug, category_slug):
        product = get_object_or_404(self.active_sku, slug=product_slug, category__slug=category_slug)
        return product

    def get_product_by_id(self, product_id):
        product = get_object_or_404(self.active_sku, id=product_id)
        return product

    def get_sku_by_id(self, sku_id: int):
        sku = get_object_or_404(self.active_sku, pk=sku_id)
        return sku

    def get_skus_by_ids(self, product_ids):
        products = get_list_or_404(self.active_sku.filter(id__in=product_ids))
        return products

    def get_title(self, sku_id):
        product_sku = get_object_or_404(self.active_sku, id=sku_id)
        product = get_object_or_404(self.active_products, skus__id = sku_id)
        serializer_product = ProductSkuSerializer(product)
        serializer_sku = ProductSkuSerializer(product_sku)
        full_name = f"{str(serializer_product.data['brand'])} {str(serializer_product.data['name'])}"
        characteristics = serializer_sku.data['characteristics']
        characteristic_value = ""
        for item in characteristics:
            characteristic_value += f" {item['value']}"

        return f"{full_name}{characteristic_value}"
