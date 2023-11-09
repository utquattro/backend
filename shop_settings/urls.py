from django.urls import path
from .views import GetAllMK, Settings

urlpatterns = [
    path('banners/', GetAllMK.as_view()),
    path('settings/', Settings.as_view()),
]