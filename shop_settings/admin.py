from django.contrib import admin
from .models import PaySystem, Socical, MarketingBanner, Settings


class BaseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'created_at', 'updated_at', 'active')


class SettingsAdmin(BaseAdmin):
    """"""
    list_display = (
        'id', 'logo', 'phone_main', 'phone_sec', 'copyright', 'created_at', 'updated_at')
    exclude = ('active',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



class MarketingBannerAdmin(BaseAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(active=True)


admin.site.register(PaySystem, BaseAdmin)
admin.site.register(Socical, BaseAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(MarketingBanner, MarketingBannerAdmin)
