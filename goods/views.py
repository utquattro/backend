from .api import Cat, Brands, Goods
from .serializers import BrandSerializer, CategorieSerializer, ProductSerializer, ProductSkuSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404


class GetAllBrands(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer


class GetAllCategory(ListAPIView):
    queryset = Cat().active_category
    serializer_class = CategorieSerializer


class GetCategoryProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Goods().products_by_category_slug(self.kwargs['category_slug'])
        return queryset


class GetFindProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        active_products = Goods().active_products
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = active_products.filter(name__icontains=search_query)

        else:
            queryset = active_products

        return queryset


class GetProductSlugWithCategory(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        category_slug = self.kwargs['category_slug']
        product_slug = self.kwargs['product_slug']
        obj = Goods().get_product_by_slug(product_slug=product_slug, category_slug=category_slug)
        return obj


class GetProductWithId(RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        obj = Goods().get_product_by_id(self.kwargs['id'])
        return obj


class GetSkuWithId(RetrieveAPIView):
    serializer_class = ProductSkuSerializer

    def get_object(self):
        obj = Goods().get_sku_by_id(self.kwargs['id'])
        return obj
