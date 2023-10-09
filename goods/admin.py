from django.contrib import admin
from .models import Categorie, Product, ProductSku, CharacteristicValue, Characteristic


class CharacteristicValueAdmin(admin.ModelAdmin):
    """"""
    pass


class CharacteristicsValueAdmin(admin.ModelAdmin):
    """"""
    pass

class CategorieAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'category_name', 'title',
        'description', 'img_url', 'link_url',
        'create_date', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'category_name', 'title', 'description')
    list_editable = ('active',)
    list_filter = ('active',)
    exclude = ['link_url', 'category_name']


class ProductAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'category', 'title',
        'description', 'img_url', 'link_url',
        'create_date', 'active')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'category_name', 'title', 'description')
    list_editable = ('active',)
    list_filter = ('active',)

    exclude = ['link_url', 'category_name', 'name']


class ProductItemAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'product', 'sku',
        'price', 'description', 'img_url',
        'create_date', 'active')
    list_display_links = ('id', 'product', 'sku')
    search_fields = ('id',  'product', 'description')
    list_editable = ('active',)
    list_filter = ('active',)


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSku, ProductItemAdmin)

admin.site.register(CharacteristicValue, CharacteristicValueAdmin)
admin.site.register(Characteristic, CharacteristicValueAdmin)
