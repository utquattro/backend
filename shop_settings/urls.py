from django.urls import path
from goods.views import GetProductBySlugAPIView

urlpatterns = [
    path('settings/', GetProductBySlugAPIView.as_view()),
]