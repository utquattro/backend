from rest_framework import serializers
from .models import CartItem, Cart
from goods.models import ProductSku


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = ('id', 'stock')


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('session', 'cart_items')

    def create(self, validated_data):
        cart_items_data = validated_data.pop('cart_items')
        cart = Cart.objects.create(**validated_data)
        for cart_item_data in cart_items_data:
            CartItem.objects.create(cart=cart, **cart_item_data)
        return cart