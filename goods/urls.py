# from rest_framework import routers
# from goods.views import TestListAPIView
#
#
# router = routers.DefaultRouter()
# router.register('', TestListAPIView, 'category')
#
#
# urlpatterns = router.urls
from django.urls import path
from goods.views import NewCatAPIView, NewBrandAPIView, CategoryProductNameAPIView, GetProductBySlugAPIView

urlpatterns = [
    path('brand/', NewBrandAPIView.as_view()),
    path('category/', NewCatAPIView.as_view()),
    path('category/<slug:category_slug>/', CategoryProductNameAPIView.as_view()),

    path('product/<int:pk>/', GetProductBySlugAPIView.as_view()),
    path('product/<slug:product_slug>/', GetProductBySlugAPIView.as_view()),
]

