from .api import ShopSetting
from .serializers import SettingsSerializer, MarketingBannerSerializer, CatCollectSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404


class GetAllMK(ListAPIView):
    queryset = ShopSetting().active_marketing_banner
    serializer_class = MarketingBannerSerializer


class Settings(RetrieveAPIView):
    serializer_class = SettingsSerializer

    def get_object(self):
        obj = ShopSetting().active_settings
        return get_object_or_404(obj)


class GetAllCollection(ListAPIView):
    queryset = ShopSetting().active_cat_collection
    serializer_class = CatCollectSerializer

