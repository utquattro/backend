from rest_framework import serializers
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'img_url', 'active')


class CharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicValue
        fields = ('id', 'value', 'active')


class CharacteristicSerializer(serializers.ModelSerializer):
    values = CharacteristicValueSerializer(many=True, read_only=True)

    class Meta:
        model = Characteristic
        fields = ('id', 'name', 'values',  'active')





class ProductSkuSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicValueSerializer(many=True, read_only=True)

    class Meta:
        model = ProductSku
        fields = ('id', 'sku', 'characteristics', 'price',  'description', 'img_url', 'active')


class ProductSerializer(serializers.ModelSerializer):
    skus = ProductSkuSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'category', 'skus', 'description', 'img_url', 'active',)


class CategoryAndProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name',  'slug',  'img_url', 'active', 'product',)


class CategorieSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    class Meta:
        model = Categorie
        fields = ('id', 'name',  'slug', 'characteristics', 'img_url', 'active',)


class CategorieNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = ('id', 'name',  'slug', 'img_url', 'active',)


class CombinedSerializer(serializers.Serializer):
    category = CategorieSerializer()
    product = ProductSerializer()

