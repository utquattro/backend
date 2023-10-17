from django.contrib import admin
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, Brand


class BrandAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'img_url',
        'created_at', 'updated_at', 'active')
    list_editable = ('active',)



class CharacteristicValueAdmin(admin.ModelAdmin):
    """"""
    pass


class CharacteristicsValueAdmin(admin.ModelAdmin):
    """"""
    pass


class CategorieAdmin(admin.ModelAdmin):
    """

    """
    prepopulated_fields = {"slug": ("name", )}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ProductItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSku, ProductItemAdmin)

admin.site.register(CharacteristicValue, CharacteristicValueAdmin)
admin.site.register(Characteristic, CharacteristicValueAdmin)

admin.site.register(Brand, BrandAdmin)