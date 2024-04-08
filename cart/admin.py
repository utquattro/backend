from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Cart, CartItem

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', '_session_data', 'expire_date']


class BaseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'created_at', 'updated_at', 'active')
    list_editable = ('active',)


class CartAdmin(BaseAdmin):
    """"""
    list_display = (
        'id',  'user', 'active', 'created_at', 'updated_at',)


class CartItemAdmin(BaseAdmin):
    """"""
    list_display = (
        'id', 'cart', 'product', 'quantity', 'active', 'created_at', 'updated_at', 'active')


admin.site.register(Session, SessionAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
