from django.contrib import admin
from .models import Warehouse

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

