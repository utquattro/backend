from rest_framework import serializers
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'img_url', 'active',)


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'category_name', 'title', 'description', 'img_url', 'link_url', 'active',)


class ProductSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = ('id', 'sku', 'price', 'description', 'img_url', 'active')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category_id', 'title', 'brand', 'description', 'img_url', 'link_url',
                  'active',)


class CharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicValue
        fields = ('id', 'value', 'description', 'active')


class CharacteristicSerializer(serializers.ModelSerializer):
    values = CharacteristicValueSerializer(many=True, read_only=True)

    class Meta:
        model = Characteristic
        fields = ('id', 'name', 'values', 'description', 'active')
