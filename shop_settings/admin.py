from django.contrib import admin
from .models import PaySystem, Information, Socical, Logo, MarketingBanner

admin.site.register(Information)
admin.site.register(PaySystem)
admin.site.register(Socical)
admin.site.register(Logo)
admin.site.register(MarketingBanner)