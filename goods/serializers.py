from rest_framework import serializers
from .models import Brand, Categorie, Product, ProductSku, \
    CharacteristicValue, Characteristic, CharacteristicName


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'img_url', 'active')


class CharacteristicNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicName
        fields = ['name']


class CharacteristicValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicValue
        fields = ['value']


class CharacteristicSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = Characteristic
        fields = ['name', 'value']

class ProductSkuSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = ProductSku
        fields = ('id', 'name', 'category', 'title', 'slug',  'brand', 'sku', 'description',
                  'img_url', 'price', 'stock', 'characteristics', 'active',)



class ProductSkuSearchSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = ProductSku
        fields = ('id', 'sku', 'img_url', 'price', 'stock', 'characteristics', 'active',)


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField()
    category = serializers.CharField()
    skus = ProductSkuSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'category', 'description', 'slug', 'img_url', 'active', 'skus',)


class CategoryAndProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug', 'img_url', 'active', 'product',)


class CategorieSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug', 'characteristics', 'img_url', 'active',)


class CategorieNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug', 'img_url', 'active',)


