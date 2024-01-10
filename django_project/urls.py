"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.contrib.auth.urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from .views import login, signup, test_token, send_sms, delete_token

schema_view = get_schema_view(  # new
    openapi.Info(
        title="е_шоп API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[path('api/', include('goods.urls')),
              path('api/', include('shop_settings.urls')),
              path('api/', include('cart.urls'))],
    public=True)

urlpatterns = [
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    url(  # new
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),

    path('admin/', admin.site.urls),

    path('api/', include('goods.urls')),
    path('api/', include('shop_settings.urls')),
    path('api/', include('cart.urls')),
    path('accounts', include("django.contrib.auth.urls")),
    path('api/login/', login),
    path('api/user/logout/', delete_token),
    path('api/user/info/', test_token),
    path('api/signup/', signup),
    path('api/sendsms/', send_sms),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
