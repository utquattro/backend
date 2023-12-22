from .api import Cat, Brands, Goods
from .serializers import BrandSerializer, CategorieSerializer, ProductSkuSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view
from cart.serializers import CartItemSkuSerializer

class GetAllBrands(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer


class GetAllSlider(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer

class GetAllCategory(ListAPIView):
    queryset = Cat().active_category
    serializer_class = CategorieSerializer


class SearchProduct(GenericAPIView):
    serializer_class = ProductSkuSerializer

    def get(self, request, *args, **kwargs):
        if self.request.query_params.get('id'):
            product_id = self.request.query_params.get('id')
            queryset = Goods().get_product_by_id(product_id=product_id)
            serializer_class = ProductSkuSerializer(queryset)
            data = serializer_class.data
            data['img_url'] = f"http://{request.META['HTTP_HOST']}{data['img_url']}"
            return Response(data, status=200)


        elif self.request.query_params.get('search'):
            search_query = self.request.query_params.get('search')
            if len(search_query) >= 2:
                queryset = Goods().find_products_by_text(src_text=search_query)
                serializer_class = ProductSkuSerializer(queryset, many=True, read_only=True)
                for i in serializer_class.data:
                    i['img_url'] = f"http://{request.META['HTTP_HOST']}{i['img_url']}"
                return Response(serializer_class.data, status=200)
            return Response({'error': 2002,
                         'message': f"shot query request :( you request len({search_query})  < 2'"}, status=404)
        else:
            return Response({'message':'not valid queryparams'}, status=400)



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

