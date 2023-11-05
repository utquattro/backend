from django.contrib import admin
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic, CharacteristicName, Brand


class BaseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'created_at', 'updated_at', 'active')
    list_editable = ('active',)


class BrandAdmin(BaseAdmin):
    """"""
    pass

class CharacteristicNameAdmin(BaseAdmin):
    """"""
    pass


class CharacteristicValueAdmin(BaseAdmin):
    """"""
    pass


class CharacteristicsValueAdmin(BaseAdmin):
    """"""
    pass


class CategorieAdmin(BaseAdmin):
    """

    """
    prepopulated_fields = {"slug": ("name", )}


class ProductAdmin(BaseAdmin):
    """

    """
    prepopulated_fields = {"slug": ("name",)}


class ProductItemAdmin(BaseAdmin):
    pass


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSku, ProductItemAdmin)
admin.site.register(CharacteristicName, CharacteristicNameAdmin)
admin.site.register(CharacteristicValue, CharacteristicValueAdmin)
admin.site.register(Characteristic, CharacteristicValueAdmin)

admin.site.register(Brand, BrandAdmin)