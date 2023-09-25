from django.contrib import admin
from .models import Promotion, PromotionCategory


class PromotionAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'discount_rate','title', 'description', 'start_date', 'end_date',
        'create_date', 'active')
    list_display_links = ('id',)
    search_fields = ('id', )
    list_editable = ('active',)
    list_filter = ('active',)


class PromotionCategoryAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'name', 'promotion', 'category',
        'create_date', 'active')
    list_display_links = ('id',)
    search_fields = ('name', )
    list_editable = ('active',)


admin.site.register(Promotion, PromotionAdmin)
admin.site.register(PromotionCategory, PromotionCategoryAdmin)

