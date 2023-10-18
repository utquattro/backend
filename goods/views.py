from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .api import hz_hz
from .api import Cat, Goods, Attributes, Brands
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import BrandSerializer


class MyPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductFull(APIView):
    def get(self, request, sku_name):
        try:

            obj = Brands()

            return Response({obj})
        except AssertionError as e:
            return Response(status=404, data={'error': 'brand not found'})


class BrandAll(APIView):
    def get(self, request):
        try:
            queryset = Brands().active_brand
            if len(queryset) > 16:
                paginator = MyPagination()
                paginated_queryset = paginator.paginate_queryset(queryset, request)
                serializer = BrandSerializer(paginated_queryset, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                serializer = BrandSerializer(queryset, many=True).data
                return Response(status=200, data={'brand list': serializer})
        except Http404 as e:
            return Response(status=404, data={'not found': str(e)})


# Create your views here.
class MainPageSetup(viewsets.ViewSet):
    def list(self, request):
        return Response(hz_hz())


class CategoryAll(APIView):
    def get(self, request):
        try:
            queryset = Cat().active_brand
            if len(queryset) > 16:
                paginator = MyPagination()
                paginated_queryset = paginator.paginate_queryset(queryset, request)
                serializer = BrandSerializer(paginated_queryset, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                serializer = BrandSerializer(queryset, many=True).data
                return Response(status=200, data={'brand list': serializer})
        except Http404 as e:
            return Response(status=404, data={'not found': str(e)})

    def get(self, request):
        try:
            att = Attributes().get_active_characteristic()
            print(att)
            obj = Cat()
            all_category = obj.get_active_category()
            assert all_category
            return Response({
                'active category': all_category,
                'attr': att,
            })

        except AssertionError as e:
            return Response(status=404, data={'error': 'active category not found'})


class CategoryByName(APIView):
    def get(self, request, category_name):
        try:
            category_info = Cat().slug_category(category_name)
            print('asd', type(category_info))
            return Response(status=200, data={category_name: category_info})

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})


class ProductFullInfo(APIView):
    def get(self, request, product_name, category_name):
        try:
            if Cat().check_category_name(category_name):
                if Goods().check_category_name(product_name):
                    product_full_info = Goods().get_product_by_name(product_name)
                    return Response(product_full_info)
                else:
                    return Response(status=404, data={
                        'error': 'product not found',

                    })
            return Response(status=404, data={
                'error': 'category not found',

            })
        except Exception as e:
            print(e)
            return Response(status=404, data={
                'error': 'Exception product',

            })

# class Asdas(APIView):
#     # def get(self, request, prop_id):
#     #     try:
#     #         product_full_info = Attr().get_propertry_by_id(prop_id)
#     #         if product_full_info:
#     #             return Response(product_full_info)
#     #         else:
#     #             return Response(status=404, data={
#     #                 'error': 'attr not found',
#     #
#     #             })
#     #     except Exception as e:
#     #         print(e)
#     #         return Response(status=404, data={
#     #             'error': 'Exception product',
#     #
#     #         })
#     def get(self, request):
#         try:
#             obj = Attr()
#             print("obj", obj)
#             all_attr = obj.get_active_propertry()
#             print("all_attr", all_attr)
#             #assert all_attr
#             return Response({
#                 'prop': all_attr
#             })
#
#         except AssertionError as e:
#             return Response(status=404, data={'error': 'active category not found'})


# class AddNewProperty(APIView):
#
#     def get(self, request):
#         memory = ['RAM', [64, 128, 256, 512, 1024, 2048]]
#         color = ['Color', ['White', 'Gold', 'Blue', 'Green', 'Yellow', 'Pink', 'Red', 'Black']]
#         display = ['Display', ['IPS', 'LED', 'AMOLED', ]]
#         internet = ['Internet', ['5g', '4g', 'LTE', 'GPRS']]
#         brand = ['Brand', ['Acer', 'Asus', 'Apple', 'HP']]
#         d1 = add_property(memory)
#         d2 = add_property(display)
#         d3 = add_property(internet)
#         d4 = add_property(color)
#         d5 = add_property(brand)
#         print(d1)
#         add_property_to_category(category_id=1, property_name_id=d1)
#         add_property_to_category(category_id=1, property_name_id=d2)
#         add_property_to_category(category_id=1, property_name_id=d3)
#         add_property_to_category(category_id=2, property_name_id=d4)
#         add_property_to_category(category_id=1, property_name_id=d5)
#         add_property_to_category(category_id=2, property_name_id=d5)
#         return Response(status=200, data={'ok': 's'})
