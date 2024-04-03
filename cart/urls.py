from django.urls import path
from .views import AddToCartView, UserCartView, DeleteToCartView


urlpatterns = [
    path('cart/', UserCartView.as_view()),
    path('cart/add/', AddToCartView.as_view()),
    path('cart/remove/', DeleteToCartView.as_view()),

]
