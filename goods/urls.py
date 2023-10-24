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
from goods.views import NewCatAPIView, ShowCategory, NewBrandAPIView, NewCatByNameAPIView

urlpatterns = [
    path('category', NewCatAPIView.as_view(), name='api_categories'),
    path('category/<slug:category_slug>/', NewCatByNameAPIView.as_view()),
    path('brand', NewBrandAPIView.as_view()),
]

