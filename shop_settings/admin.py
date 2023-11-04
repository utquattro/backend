from django.contrib import admin
from .models import Logo, PaySystem, Information, Socical

admin.site.register(Information)
admin.site.register(PaySystem)
admin.site.register(Socical)
admin.site.register(Logo)