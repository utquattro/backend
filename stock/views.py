from rest_framework import viewsets
from .api import Stock
from goods.api import Sku

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class StockAmountBySku(APIView):
    def get(self, request, product_sku_id):
        try:
            if Sku().check_sku_id(product_sku_id):
                product_full_info = Stock().get_stock_amount_by_product_sku(product_sku_id)
                print('ppp', product_full_info)
                return Response(product_full_info)
            else:
                return Response(status=404, data={'error': 'wrong product SKU'})
        except AssertionError as efs:
            return Response(status=404, data={'error': efs})
        except TypeError as e:
            return Response(status=404, data={'error': 'e'})
