from rest_framework import serializers
from .models import Categorie, Product, ProductSku, PropertyName, Property


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'category_name', 'title', 'description', 'img_url', 'link_url', 'active', )


class ProductSkuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSku
        fields = ('id',  'sku', 'price', 'description', 'img_url', 'active')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'category_id', 'title', 'description', 'img_url', 'link_url', 'active',)


class PropertySerializer(serializers.ModelSerializer):
    pr_name = serializers.StringRelatedField(many=True)
    pr_val = serializers.StringRelatedField(many=True)

    class Meta:
        model = Property
        fields = '__all__'
