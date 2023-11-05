from .api import ShopSetting
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InformationSerializer, SocicalSerializer, PaySystemSerializer, \
    MainSettingSerializer, LogoSerializer, MarketingBannerSerializer
from rest_framework.generics import ListAPIView, GenericAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404, get_list_or_404


class GetInformation(ListAPIView):
    queryset = ShopSetting().active_info
    serializer_class = InformationSerializer


class AllFieldsAPIView(ListAPIView):
    serializer_class = MainSettingSerializer

    def get(self, request):
        shop_api = ShopSetting()
        information = shop_api.active_info
        logo = shop_api.active_logo
        pay = shop_api.active_pay_system
        social = shop_api.active_social
        banners = shop_api.active_marketing_banner

        resp = {
            'logo': LogoSerializer(logo, many=True).data,
            'information': InformationSerializer(information, many=True).data,
            "pay_system": PaySystemSerializer(pay, many=True).data,
            "social": SocicalSerializer(social, many=True).data,
            "marketing_banner": MarketingBannerSerializer(banners, many=True).data
        }
        return Response(resp)
