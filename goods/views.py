from .api import Cat, Brands, Goods
from .serializers import BrandSerializer, CategorieSerializer, ProductSerializer, \
    ProductSkuSerializer, CharacteristicSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework.decorators import api_view


class GetAllBrands(ListAPIView):
    queryset = Brands().active_brand
    serializer_class = BrandSerializer


class GetAllCategory(ListAPIView):
    queryset = Cat().active_category
    serializer_class = CategorieSerializer


@api_view(['GET'])
def search_product(request):
    try:
        search_query = request.query_params.get('search')
        if len(request.query_params.get('search')) >= 2:
            find_product = []
            brand_id = []
            if search_query:
                name = Goods().active_products.filter(name__icontains=search_query)
                for i in name:
                    find_product.append(i.pk)
                brand = Brands().active_brand.filter(name__icontains=search_query)
                for j in brand:
                    brand_id.append(j.pk)
                product_by_brand = Goods().active_products.filter(brand__in=brand_id)

                char = Goods().active_sku.filter(characteristics__value__value__icontains=search_query)
                sku = Goods().active_sku.filter(sku__icontains=search_query)
                product_name = Goods().active_sku.filter(product_skus__in=find_product)
                by_brand = Goods().active_sku.filter(product_skus__in=product_by_brand)

                queryset = char | sku | product_name | by_brand
                queryset_sort = queryset.distinct()
                serializer = ProductSkuSerializer(queryset_sort, many=True)
                serialized_data = serializer.data
                f = []
                host = str('http://'+request.get_host())
                for i in serialized_data:
                    i['title'] = Goods().get_title(sku_id=i['id'])
                    if i['img_url']:
                        i['img_url'] = host + i['img_url']
                        print(i)
                    f.append(i)
                if len(f) > 1:
                    #print(f)
                    #print('asd:', request.get_host())
                    return Response(f)
                return Response({'message': 'not found'}, status=404)
        return Response({'error': 2002,
                         'message': f"shot query request :( you request len({search_query})  < 2'"}, status=404)

    except KeyError as e:
        return Response({'error': str(e)}, status=400)

    except TypeError as e:
        return Response({'error': str(e)}, status=400)

class GetCategoryProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Goods().products_by_category_slug(self.kwargs['category_slug'])
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
