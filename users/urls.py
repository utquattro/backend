from django.urls import path
from users.views import login, delete_token, send_sms, get_profile_info

urlpatterns = [

    path('user/login/', login),
    path('user/logout/', delete_token),
    path('user/info/', get_profile_info),
    path('sendsms/', send_sms),
]
