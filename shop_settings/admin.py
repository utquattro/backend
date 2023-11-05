from django.contrib import admin
from .models import PaySystem, Information, Socical, Logo, MarketingBanner

class BaseAdmin(admin.ModelAdmin):
    """"""
    list_display = (
        'id', 'created_at', 'updated_at', 'active')
    list_editable = ('active',)



admin.site.register(Information,BaseAdmin)
admin.site.register(PaySystem,BaseAdmin)
admin.site.register(Socical,BaseAdmin)
admin.site.register(Logo,BaseAdmin)
admin.site.register(MarketingBanner,BaseAdmin)