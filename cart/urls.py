from django.urls import path
from cart.views import cart_add, cart_remove, CartDetailAPIView

urlpatterns = [
    path('cart/', CartDetailAPIView.as_view()),
    path('cart/add/', cart_add),
    path('cart/remove/', cart_remove),
]

