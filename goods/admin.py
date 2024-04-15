from django.contrib import admin
from .models import Categorie, ProductSku, CharacteristicValue, Characteristic, CharacteristicName, Brand


class BaseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'created_at', 'updated_at', 'active')
    list_editable = ('active',)


class BrandAdmin(BaseAdmin):
    """"""
    list_display = (
        'id',  'name', 'active', 'description', 'img_url',
        'created_at', 'updated_at', 'active')


class CharacteristicNameAdmin(BaseAdmin):
    """"""
    list_display = (
        'id',  'name',
        'created_at', 'updated_at', 'active')


class CharacteristicValueAdmin(BaseAdmin):
    """"""
    list_display = (
        'id',  'value',
        'created_at', 'updated_at', 'active')


class CharacteristicsAdmin(BaseAdmin):
    """"""
    list_display = (
        'id', 'name',  'value',
        'created_at', 'updated_at', 'active')


class CategorieAdmin(BaseAdmin):
    """

    """
    list_display = (
        'id', 'slug', 'name', 'img_url',
        'created_at', 'updated_at', 'active')
    prepopulated_fields = {"slug": ("name", )}


class ProductAdmin(BaseAdmin):
    """

    """
    list_display = (
        'id', 'slug', 'name', 'category', 'brand',
        'created_at', 'updated_at', 'active')
    prepopulated_fields = {"slug": ("name",)}


class ProductItemAdmin(BaseAdmin):
    list_display = (
        'id', 'category', 'name', 'title', 'rate', 'brand', 'sku', 'price', 'stock', 'description',
        'img_url',
        'created_at', 'updated_at', 'active')


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(ProductSku, ProductItemAdmin)
admin.site.register(CharacteristicName, CharacteristicNameAdmin)
admin.site.register(CharacteristicValue, CharacteristicValueAdmin)
admin.site.register(Characteristic, CharacteristicsAdmin)
admin.site.register(Brand, BrandAdmin)

