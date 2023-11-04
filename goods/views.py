from django.http import Http404

from .api import Cat, Brands, Goods
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BrandSerializer, CategorieSerializer, ProductSerializer, CombinedSerializer, \
    ProductSkuSerializer, CharacteristicListSerializer, ProductDetailSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404


class NewBrandAPIView(ListAPIView):
    serializer_class = BrandSerializer

    def get_queryset(self):
        sd = Brands().active_brand
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


class ProductWithSku(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            category_slug = self.kwargs['category_slug']  # Получаем значение category_slug из URL параметра
            product_slug = self.kwargs['product_slug']  # Получаем значение product_slug из URL параметра
            # queryset = Goods().active_products.filter(category__slug=category_slug).filter(slug=product_slug)
            if get_object_or_404(Cat().active_category.get(slug=category_slug)):
                #print('atice cat', dd)
                #queryset = Goods().active_products.filter(category__slug=category_slug)
                #qq = get_list_or_404(Goods().active_sku.filter(product__slug=product_slug))
                #serializer = self.serializer_class(qq)
                #print(type(queryset))
                #print(qq)
                return None
            else:
                raise AssertionError

        except BaseException as e:
            return str(e)


class FroductWithSku(APIView):
    def get(self, request, category_slug, product_slug):
        try:
            product = Goods().active_products.get(product__slug=product_slug)
            skus = Goods().active_sku.filter(product__slug=product_slug)

            product_serializer = ProductSerializer(product)
            sku_serializer = ProductSkuSerializer(skus, many=True)
            print('product_serializer', product_serializer)
            data = {
                'product': product_serializer.data,
                'sku': sku_serializer.data
            }

            return Response(data)

        except BaseException as e:
            return Response(str(e))


class GetProductBySlugAPIView(RetrieveAPIView):
    queryset = Goods().active_products
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'  # Optional, if the product's slug field name is different

    # You can also override the get_object() method if you need to customize the retrieval logic
    def get_object(self):
        queryset = self.get_queryset()
        queryset_sku = Goods().active_sku
        obj = get_object_or_404(queryset, slug=self.kwargs['product_slug'])
        #resp = obj
        obj2 = get_list_or_404(queryset_sku, product__slug=self.kwargs['product_slug'])
        print(obj)
        print(obj2)
        resp = {
           "product": obj,
            "skus": obj2,
        }

        return resp



