from .models import Categorie, Product, ProductSku
from .serializers import CategorieSerializer, ProductSerializer, ProductSkuSerializer


class Cat:

    def __init__(self):
        self.active_category = Categorie.objects.filter(active=True)

    def get_active_category(self):
        try:
            response_data = CategorieSerializer(self.active_category, many=True).data
            return response_data
        except Exception as e:
            return None, e

    def get_category_id_by_name(self, category_name):
        try:
            get_category = self.active_category.filter(link_url=category_name)
            result = CategorieSerializer(get_category, many=True).data[0]['id']
            return result
        except IndexError as e:
            return False

    def check_category_name(self, category_name):
        try:
            self.active_category.get(link_url=category_name)
            return True
        except Exception as e:
            return False


class Goods:

    def __init__(self):
        self.active_products = Product.objects.filter(active=True)

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
            return response_data
        else:
            return False

    def get_product_full_info_by_name(self, product_name):
        try:
            product = self.get_product_by_name(product_name)

            product_id = product[0]['id']
            sku = Sku().get_sku_by_product_id(product_id)
            product[0]['sku'] = sku
            response_data = {product_name: product}
            if product:
                return response_data
            else:
                return False
        except Exception as e:
            return type(e)

    def get_products_by_category_name(self, category_name):
        try:
            category_id = Cat().get_category_id_by_name(category_name)
            products = self.active_products.filter(category_id=category_id)
            if products.count() == 0:
                return False
            else:
                response_data = ProductSerializer(products, many=True).data
                return response_data
        except Exception as e:
            print('exp!!')
            return e
class Sku:

    def __init__(self):
        self.active_sku = ProductSku.objects.filter(active=True)

    def check_sku_id(self, product_sku):
        try:
            self.active_sku.get(id=product_sku)
            return True
        except Exception as e:
            return False

    def get_sku_by_product_id(self, product_id):
        product = self.active_sku.filter(product=product_id)
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


# def add_property(p_name):
#     new_propery_list = []
#     new_propoperty = PropertyName.objects.create(name=p_name[0], active=True)
#     for propery_name in p_name[1]:
#         new_type_id = PropertyValue.objects.create(value=propery_name, active=True)
#         new_val_id = Property.objects.create(property_name=new_propoperty,
#                                              property_value=new_type_id, active=True)
#         new_propery_list.append(new_type_id.id)
#     return new_propoperty.id
#
#
# def add_property_to_category(category_id, property_name_id):
#     new_cat_prop_id = CategoryPropertyConfig.objects.create(category_id=category_id,
#                                                             property_name_id=property_name_id, active=True)
#     return new_cat_prop_id.id

