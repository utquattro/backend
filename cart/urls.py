from django.urls import path
from cart.views import cart_add, cart_remove, cart_view

urlpatterns = [
    path('cart/', cart_view),
    path('cart/add/', cart_add),
    path('cart/remove/', cart_remove),

]

