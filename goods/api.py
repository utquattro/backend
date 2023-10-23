from .models import Categorie, Product, ProductSku,  Characteristic, Brand
from .serializers import CategorieSerializer, ProductSerializer, ProductSkuSerializer, CharacteristicSerializer, \
    CharacteristicValueSerializer, BrandSerializer, CategoryAndProductSerializer
from django.shortcuts import get_object_or_404, get_list_or_404


class Attributes:
    def __init__(self):
        self.active_characteristic = get_list_or_404(Characteristic.active_objects)

    def get_active_characteristic(self):
        try:
            response_data = CharacteristicSerializer(self.active_characteristic.active_objects, many=True).data
            return response_data
        except Exception as e:
            return None, e


class Brands:

    def __init__(self):
        self.active_brand = get_list_or_404(Brand.active_objects)
        # self.active_brand = BrandSerializer(get_list_or_404(Brand.active_objects), many=True).data


    def get_all_brands(self):
        try:
            response_data = BrandSerializer(self.active_brand, many=True).data
            return response_data
        except Exception as e:
            return None, e


class Cat:
    def __init__(self):
        self.active_category = Categorie.active_objects

    def slug_category(self, category_slug):
        category = get_object_or_404(Categorie.active_objects, slug=category_slug)
        category_data = CategorieSerializer(category).data
        products = Product.objects.filter(category=category)
        products_data = ProductSerializer(products, many=True).data

        response_data = {
            'category_data': category_data,
            'products': products_data
        }
        return response_data
    def get_active_category(self):
        pass

    def get_category_id_by_name(self, category_name):
        pass

    def check_category_name(self, category_name):
        pass


class Goods:
    def __init__(self):
        self.active_products = Product.active_objects.all()

    def check_category_name(self, product_name):
        try:
            self.active_products.get(link_url=product_name)
            return True
        except Exception as e:
            return False

    def get_product_id_by_name(self, product_name):
        product = self.active_products.filter(link_url=product_name)
        if product:
            response_data = ProductSerializer(product, many=True).data[0]['id']
            return response_data
        else:
            return None

    def get_product_by_name(self, product_name):
        product = self.active_products.filter(link_url=product_name)
        if product:
            response_data = ProductSerializer(product, many=True).data
            print(response_data)
            return response_data
        else:
            return False

    # def get_product_full_info_by_name(self, product_name):
    #     try:
    #         product = self.get_product_by_name(product_name)
    #
    #         product_id = product[0]['id']
    #         response_data = {product_name: product}
    #         if product:
    #             return response_data
    #         else:
    #             return False
    #     except Exception as e:
    #         return type(e)




class Sku:

    def __init__(self):
        self.active_sku = ProductSku.objects.filter(active=True)

    def check_sku_id(self, product_sku):
        try:
            self.active_sku.get(id=product_sku)
            return True
        except Exception as e:
            return False

    def get_sku_by_product_id(self, product_name):
        get_sku = Goods().get_product_id_by_name(product_name)
        print('gg', get_sku)
        product = self.active_sku.filter(product=get_sku)
        if product:
            response_data = ProductSkuSerializer(product, many=True).data
            print('jj: ', response_data)
            return response_data
        else:
            return None


def hz_hz():
    text = 'hello'
    response_data = {'test': text}
    return response_data
