from rest_framework import serializers
from .models import Warehouse, WarehouseAmount


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ('id',  'name', 'description', 'active',)


class WarehouseAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseAmount
        fields = ('id', 'stock_id', 'product_item', 'quantity', 'active',)
        read_only_fields = ('product_item',)