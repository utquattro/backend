from rest_framework import viewsets
from .api import hz_hz
from .api import Cat, Goods
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class MainPageSetup(viewsets.ViewSet):
    def list(self, request):
        return Response(hz_hz())


class CategoryAll(APIView):
    def get(self, request):
        try:
            obj = Cat()
            all_category = obj.get_active_category()
            assert all_category
            return Response({
                'active category': all_category
            })

        except AssertionError as e:
            return Response(status=404, data={'error': 'active category not found'})


class CategoryByName(APIView):
    def get(self, request, category_name):
        try:
            assert (Cat().check_category_name(category_name))
            products = Goods().get_products_by_category_name(category_name)

            return Response(status=200, data=
            {category_name: products}
                            )

        except AssertionError as e:
            return Response(status=404, data={'error': 'category not found'})


class ProductFullInfo(APIView):
    def get(self, request, product_name, category_name):
        try:
            valid_product_name = Goods().check_category_name(product_name)
            valid_category_name = Cat().check_category_name(category_name)
            if valid_product_name & valid_category_name:
                product_full_info = Goods().get_product_full_info_by_name(product_name)
                return Response(product_full_info)
            else:
                return Response(status=404, data={
                    'error': 'product not found',

                })
        except Exception as e:
            print(e)
            return Response(status=404, data={
                'error': 'Exception product',

            })
