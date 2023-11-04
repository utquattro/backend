from django.contrib import admin
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, CharacteristicName, Brand


class BrandAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'img_url',
        'created_at', 'updated_at', 'active')
    list_editable = ('active',)


class CharacteristicNameAdmin(admin.ModelAdmin):
    """"""
    pass


class CharacteristicValueAdmin(admin.ModelAdmin):
    """"""
    pass


class CharacteristicsValueAdmin(admin.ModelAdmin):
    """"""
    pass


class CategorieAdmin(admin.ModelAdmin):
    """

    """
    list_display = (
        'id', 'name', 'img_url',
        'created_at', 'slug', 'updated_at', 'active')
    list_editable = ('active',)
    prepopulated_fields = {"slug": ("name", )}


class ProductAdmin(admin.ModelAdmin):
    """

    """
    list_display = (
        'id', 'name', 'img_url',
        'created_at', 'slug', 'updated_at', 'active')
    list_editable = ('active',)

    prepopulated_fields = {"slug": ("name",)}


class ProductItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSku, ProductItemAdmin)
admin.site.register(CharacteristicName, CharacteristicNameAdmin)
admin.site.register(CharacteristicValue, CharacteristicValueAdmin)
admin.site.register(Characteristic, CharacteristicValueAdmin)

admin.site.register(Brand, BrandAdmin)