"""
URL configuration for e_shop project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop_settings import views
from goods.views import CategoryByName, CategoryAll, ProductFullInfo, BrandAll
from stock.views import StockAmountBySku

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brand/',  BrandAll.as_view()),
    path('cat/<slug:category_name>/', CategoryByName.as_view()),
    # path('category/', CategoryAll.as_view()),
    # path('category/<slug:post_slug>/', show_post, name='category_detail'),
    # path('category/<str:category_name>/<str:product_name>/', ProductFullInfo.as_view()),
    path('stock/<str:product_sku_id>/', StockAmountBySku.as_view()),
    path('shop_settings/', include('shop_settings.urls')),
    path('create_/', views.create_settings_value),
    path('', views.index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
