from django.urls import path
from .views import GetInformation, AllFieldsAPIView

urlpatterns = [
    path('info/', GetInformation.as_view()),
    path('settings/', AllFieldsAPIView.as_view()),
]