from django.urls import path
from users.views import  delete_token, send_sms, get_profile_info, login_or_register, change_user_info

urlpatterns = [
    path('user/login_or_register/', login_or_register),
    path('user/logout/', delete_token),
    path('user/info/', get_profile_info),
    path('user/change_info/', change_user_info),
    path('sendsms/', send_sms),
]
