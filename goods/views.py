from rest_framework import viewsets
from .api import hz_hz, add_property, add_property_to_category
from .api import Cat, Goods, Attr
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class MainPageSetup(viewsets.ViewSet):
    def list(self, request):
        return Response(hz_hz())


class CategoryAll(APIView):
    def get(self, request):
        try:
            obj = Cat()
            all_category = obj.get_active_category()
            assert all_category
            return Response({
                'active category': all_category
            })

        except AssertionError as e:
            return Response(status=404, data={'error': 'active category not found'})


class CategoryByName(APIView):
    def get(self, request, category_name):
        try:
            assert (Cat().check_category_name(category_name))
            products = Goods().get_products_by_category_name(category_name)
            if products:
                return Response(status=200, data={'category': category_name,
                                                  'products': products,
                                                  'Property': 'sad'})
            else:
                return Response(status=204, data={'category': category_name,
                                                  'products': None})
        except AssertionError as e:
            return Response(status=404, data={'error': 'category not found'})


class ProductFullInfo(APIView):
    def get(self, request, product_name, category_name):
        try:
            valid_product_name = Goods().check_category_name(product_name)
            valid_category_name = Cat().check_category_name(category_name)
            if valid_product_name & valid_category_name:
                product_full_info = Goods().get_product_full_info_by_name(product_name)
                return Response(product_full_info)
            else:
                return Response(status=404, data={
                    'error': 'product not found',

                })
        except Exception as e:
            print(e)
            return Response(status=404, data={
                'error': 'Exception product',

            })


class Attributs(APIView):
    # def get(self, request, prop_id):
    #     try:
    #         product_full_info = Attr().get_propertry_by_id(prop_id)
    #         if product_full_info:
    #             return Response(product_full_info)
    #         else:
    #             return Response(status=404, data={
    #                 'error': 'attr not found',
    #
    #             })
    #     except Exception as e:
    #         print(e)
    #         return Response(status=404, data={
    #             'error': 'Exception product',
    #
    #         })
    def get(self, request):
        try:
            obj = Attr()
            print("obj", obj)
            all_attr = obj.get_active_propertry()
            print("all_attr", all_attr)
            #assert all_attr
            return Response({
                'prop': all_attr
            })

        except AssertionError as e:
            return Response(status=404, data={'error': 'active category not found'})


class AddNewProperty(APIView):

    def get(self, request):
        memory = ['RAM', [64, 128, 256, 512, 1024, 2048]]
        color = ['Color', ['White', 'Gold', 'Blue', 'Green', 'Yellow', 'Pink', 'Red', 'Black']]
        display = ['Display', ['IPS', 'LED', 'AMOLED', ]]
        internet = ['Internet', ['5g', '4g', 'LTE', 'GPRS']]
        brand = ['Brand', ['Acer', 'Asus', 'Apple', 'HP']]
        d1 = add_property(memory)
        d2 = add_property(display)
        d3 = add_property(internet)
        d4 = add_property(color)
        d5 = add_property(brand)
        print(d1)
        add_property_to_category(category_id=1, property_name_id=d1)
        add_property_to_category(category_id=1, property_name_id=d2)
        add_property_to_category(category_id=1, property_name_id=d3)
        add_property_to_category(category_id=2, property_name_id=d4)
        add_property_to_category(category_id=1, property_name_id=d5)
        add_property_to_category(category_id=2, property_name_id=d5)
        return Response(status=200, data={'ok': 's'})
