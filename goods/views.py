from django.http import Http404

from .api import Cat, Goods, Brands, Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import BrandSerializer, CategorieSerializer, CategorieNameSerializer, CombinedSerializer
from rest_framework.generics import ListAPIView, GenericAPIView



class MyPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class Full(APIView):
    def get(self, request, sku_name):
        try:
            obj = Brands()
            return Response({obj})
        except AssertionError as e:
            return Response(status=404, data={'error': 'brand not found'})


class NewBrandAPIView(ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        return Brands().active_brand


class NewCatAPIView(ListAPIView):
    serializer_class = CategorieSerializer

    def get_queryset(self):
        return Cat().active_category


class NewCatByNameAPIView(ListAPIView):
    serializer_class = CategorieSerializer

    def get(self, request, category_slug):
        try:
            category_info = Cat().slug_category(category_slug)
            serializer = self.serializer_class(category_info)
            return Response(serializer.data)

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})


class TestListAPIView(ListAPIView):
    serializer_class = CombinedSerializer

    def get_queryset(self, category_slug):
        return {
            'category': Cat().slug_category(category_slug),
            'product': Product().active_objects
        }

class BrandAll(APIView):
    def get(self, request):
        try:
            queryset = Brands().active_brand

            paginator = MyPagination()
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = BrandSerializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)

        except Http404 as e:
            return Response(status=404, data={'not found': str(e)})


class CategoryAll(APIView):
    def get(self, request):
        try:
            queryset = Cat().active_category
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


class ShowCategory(APIView):
    def get(self, request):
        try:
            category_all = Cat().active_category
            cat_response = CategorieSerializer(category_all, many=True)
            return Response(status=200, data=cat_response.data)

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})


class CategoryByName(APIView):
    def get(self, request, category_name):
        try:
            category_info = Cat().slug_category(category_name)
            return Response(status=200, data=category_info)

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})


class ProductFullInfo(APIView):
    def get(self, request, product_name, category_name):
        try:
            if Cat().old_check_category_name(category_name):
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
