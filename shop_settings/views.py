from .api import Logo
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LogoSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404


class GetProductBySlugAPIView(RetrieveAPIView):
    pass
    # queryset = Logo
    # serializer_class = ProductDetailSerializer
    # lookup_field = 'slug'  # Optional, if the product's slug field name is different
    #
    # def get_object(self):
    #     # queryset = self.get_queryset()
    #     # queryset_sku = Goods().active_sku
    #     # obj = get_object_or_404(queryset, slug=self.kwargs['product_slug'])
    #     # #resp = obj
    #     # obj2 = get_list_or_404(queryset_sku, product__slug=self.kwargs['product_slug'])
    #     # print(obj)
    #     # print(obj2)
    #     # resp = {
    #     #    "product": obj,
    #     #     "skus": obj2,
    #     # }
    #
    #     return pass