from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .api import Cat, Brands, Goods
from .serializers import BrandSerializer, CategorieSerializer, ProductSkuSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.serializers import CartItemSkuSerializer
from rest_framework import generics, status
from rest_framework.exceptions import NotFound


class GetAllBrands(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer


class GetAllSlider(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brands().active_brand


class GetAllCategory(ListAPIView):
    serializer_class = CategorieSerializer
    queryset = Cat().list_category()


class ProductSkuView(ListAPIView):
    serializer_class = ProductSkuSerializer

    def get_queryset(self):
        try:
            print('hi')
            products = Goods().active_products
            if self.request.GET.get('id'):
                return products.filter(pk=self.request.GET.get('id'))
            if self.request.GET.get('category'):
                return products.filter(category__slug=self.request.GET.get('category'))
            if self.request.GET.get('search'):
                return products.filter(title__icontains=self.request.GET.get('search'))
            else:
                return Response({1}, status=404)
        except BaseException as e:
            return Response({str(e)})


class GetCategoryProducts(ListAPIView):
    serializer_class = ProductSkuSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        queryset = Goods().active_sku.filter(category__slug=category_slug)
        return queryset


class GetProductSlugWithCategory(RetrieveAPIView):
    serializer_class = ProductSkuSerializer

    def get_object(self):
        category_slug = self.kwargs['category_slug']
        product_slug = self.kwargs['product_slug']
        obj = Goods().get_product_by_slug(product_slug=product_slug, category_slug=category_slug)
        return obj


class GetProductWithId(RetrieveAPIView):
    serializer_class = ProductSkuSerializer

    def get_queryset(self):
        product_sku_id = self.kwargs['pk']
        product_sku = Goods().active_sku.filter(id=product_sku_id)
        return product_sku
