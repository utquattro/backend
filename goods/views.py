from django.http import Http404

from .api import Cat, Brands, Goods
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BrandSerializer, CategorieSerializer, ProductSerializer, CombinedSerializer
from rest_framework.generics import ListAPIView, GenericAPIView


class NewBrandAPIView(ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        sd = Goods().active_products
        print(type(sd), sd)
        return sd


class NewCatAPIView(ListAPIView):
    serializer_class = CategorieSerializer

    def get_queryset(self):
        return Cat().active_category


class CategoryProductNameAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            category_slug = self.kwargs['category_slug']  # Получаем значение category_slug из URL параметра
            queryset = Goods().active_products.filter(category__slug=category_slug)
            return queryset

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})


class GetProductBySlugAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get(self, request, product_slug):
        try:
            category_info = Goods().product_by_slug(product_slug)
            print('cat info:', category_info)
            serializer = self.serializer_class(category_info)
            print(serializer)
            return Response(serializer.data)

        except AssertionError as e:
            return Response(status=404, data={'error': str(e)})

