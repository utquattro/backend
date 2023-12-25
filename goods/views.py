from rest_framework.views import APIView

from .api import Cat, Brands, Goods
from .serializers import BrandSerializer, CategorieSerializer, ProductSkuSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.serializers import CartItemSkuSerializer
from rest_framework import generics
from rest_framework.exceptions import NotFound


class GetAllBrands(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer


class GetAllSlider(ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brands().active_brand


class GetAllCategory(ListAPIView):
    serializer_class = CategorieSerializer
    queryset = Cat().active_category


class ProductSkuView(ListAPIView):
    serializer_class = ProductSkuSerializer

    def get_queryset(self):
        try:
            products = Goods().active_products
            if self.request.GET.get('id'):
                return products.filter(pk=self.request.GET.get('id'))
            if self.request.GET.get('category'):
                return products.filter(category__slug=self.request.GET.get('category'))
            if self.request.GET.get('search'):
                return products.filter(title__icontains=self.request.GET.get('search'))
            else:
                return None
        except BaseException as e:
            return Response({str(e)})


class SearchProduct(generics.ListAPIView):
    serializer_class = ProductSkuSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.query_params.get('id'):
            product_id = self.request.query_params.get('id')
            queryset = Goods().get_product_by_id(product_id=product_id)
            serializer_class = ProductSkuSerializer(queryset)
            data = serializer_class.data
            data['img_url'] = str(f"http://{self.request.META['HTTP_HOST']}{data['img_url']}")
            return data

        elif self.request.query_params.get('category'):
            category_slug = self.request.query_params.get('category')
            queryset = Goods().products_by_category_slug(category_slug=category_slug)
            serializer_class = ProductSkuSerializer(queryset, many=True, read_only=True)
            data = serializer_class.data
            return Response(data, status=200)

        elif self.request.query_params.get('search'):
            search_query = self.request.query_params.get('search')
            if len(search_query) >= 2:
                queryset = Goods().find_products_by_text(src_text=search_query)
                serializer_class = ProductSkuSerializer(queryset, many=True, read_only=True)
                data = serializer_class.data
                for i in data:
                    i['img_url'] = f"http://{self.request.META['HTTP_HOST']}{i['img_url']}"
                return data
            return Response({'error': 2002,
                             'message': f"shot query request :( you request len({search_query})  < 2'"}, status=404)
        else:
            return Response({'message': 'not valid queryparams'}, status=400)


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
