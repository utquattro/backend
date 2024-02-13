from django.urls import path
from .views import GetAllMK, Settings, GetAllCollection

urlpatterns = [
    path('banners/', GetAllMK.as_view()),
    path('cat_collection/', GetAllCollection.as_view()),
    path('settings/', Settings.as_view()),
]