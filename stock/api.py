from .models import Warehouse, WarehouseAmount
from .serializers import WarehouseSerializer, WarehouseAmountSerializer


class Stock:

    def __init__(self):
        self.active_stock_amount = WarehouseAmount.objects.filter(active=True)

    def get_stock_amount_by_product_sku(self, product_sku_id):
        try:
            get_stocks = self.active_stock_amount.filter(product_item=product_sku_id)
            print(get_stocks)
            assert get_stocks

            response_data = WarehouseAmountSerializer(get_stocks, many=True).data
            return response_data
        except TypeError as e:
            return {'eer': e}
