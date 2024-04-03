from django.core.validators import MinValueValidator
from rest_framework import serializers
from .models import CartItem, Cart
from goods.models import ProductSku
from goods.serializers import RecommendedProductSerializer


class CartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)])
    product = RecommendedProductSerializer()


class CartDeleteSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()

    class Meta:
        model = ProductSku
        fields = ('product_id',)

class CartAddItemSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField(validators=[MinValueValidator(1)])


class CartSerializer(serializers.Serializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_cost = serializers.IntegerField()
    total_goods = serializers.IntegerField()
    total_quantity = serializers.IntegerField()


