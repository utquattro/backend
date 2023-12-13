from django.urls import path
from cart.views import  cart_add, cart_detail, cart_remove

urlpatterns = [


    path('cart', cart_detail),
    path('cart/add', cart_add),
    path('cart/remove', cart_remove),
]

