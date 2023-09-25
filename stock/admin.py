from django.contrib import admin
from .models import Warehouse, WarehouseAmount



class WarehouseAmountAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'stock', 'product_item', 'quantity',
        'create_date', 'active')
    list_display_links = ('id',)
    search_fields = ('id', )
    list_editable = ('active',)
    list_filter = ('active',)


class WarehouseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'description',
        'create_date', 'active')
    list_display_links = ('id',)
    search_fields = ('name', )
    list_editable = ('active',)


# Register your models here.
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(WarehouseAmount, WarehouseAmountAdmin)

