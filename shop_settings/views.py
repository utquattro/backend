from .api import ShopSetting
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SocicalSerializer, PaySystemSerializer, \
    SettingsSerializer, MarketingBannerSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.sites.shortcuts import get_current_site


class GetAllMK(ListAPIView):
    queryset = ShopSetting().active_marketing_banner
    serializer_class = MarketingBannerSerializer


class Settings(RetrieveAPIView):
    serializer_class = SettingsSerializer

    def get_object(self):
        obj = ShopSetting().active_settings
        return get_object_or_404(obj)
