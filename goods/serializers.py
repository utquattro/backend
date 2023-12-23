from rest_framework import serializers
from .models import Brand, Categorie, ProductSku, \
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


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug', 'img_url', 'active',)


class CategorieProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'name', 'slug')

class ProductSkuSerializer(serializers.ModelSerializer):
    characteristics = CharacteristicSerializer(many=True, read_only=True)
    category = CategorieProductSerializer(read_only=True)

    class Meta:
        model = ProductSku
        fields = ('id', 'name', 'category', 'title', 'slug',  'brand', 'sku', 'description',
                  'img_url', 'price', 'stock', 'characteristics', 'active',)




