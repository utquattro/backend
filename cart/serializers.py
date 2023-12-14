from rest_framework import serializers
from goods.models import ProductSku


class ProductSkuIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = ('id',)


class CartProductSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = ('id', 'sku', 'img_url', 'price', 'stock')


class CartItemSerializer(serializers.Serializer):
    product_sku_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)


class CartSerializer(serializers.Serializer):
    cart = CartItemSerializer(many=True)
    items_count = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)

