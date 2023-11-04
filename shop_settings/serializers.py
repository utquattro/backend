from rest_framework import serializers
from .models import Information, PaySystem, Socical, Logo, MarketingBanner


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ('name', 'value',)



class SocicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socical
        fields = ('name', 'description', 'img_url')


class PaySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaySystem
        fields = ('name', 'description', 'img_url')


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = ('name', 'img_url',)


class MarketingBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingBanner
        fields = ('name', 'description', 'img_url')


class MainSettingSerializer(serializers.Serializer):
    logo = LogoSerializer()
    information = InformationSerializer()
    pay_system = PaySystemSerializer()
    social = SocicalSerializer()
    marketing_banner = MarketingBannerSerializer()

    class Meta:
        fields = ('logo', 'information', 'pay_system', 'social', 'marketing_banner',)

