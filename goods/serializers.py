from rest_framework import serializers
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, Brand



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'category_name', 'title', 'description', 'img_url', 'link_url', 'active',)


class CharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicValue
        fields = ('id', 'value', 'description', 'active')


class CharacteristicSerializer(serializers.ModelSerializer):
    values = CharacteristicValueSerializer(many=True, read_only=True)

    class Meta:
        model = Characteristic
        fields = ('id', 'name', 'values', 'description', 'active')


class ProductSkuSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicValueSerializer(many=True, read_only=True)

    class Meta:
        model = ProductSku
        fields = ('id', 'sku', 'price', 'characteristics', 'description', 'img_url', 'active')


class ProductSerializer(serializers.ModelSerializer):
    skus = ProductSkuSerializer(many=True, read_only=True)
    #brand = BrandSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category_id', 'title', 'brand', 'skus',  'img_url', 'link_url',
                  'active',)

