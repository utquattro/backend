from rest_framework import serializers
from .models import PaySystem, Socical, MarketingBanner, Settings


class SocicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socical
        fields = ('name', 'description',  'img_url', 'active')


class PaySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaySystem
        fields = ('name', 'description', 'img_url', 'active')


class MarketingBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingBanner
        fields = ('name', 'description', 'start_date', 'end_date', 'img_url', 'active')


class SettingsSerializer(serializers.Serializer):
    logo = serializers.ImageField()
    phone_main = serializers.CharField()
    phone_sec = serializers.CharField()
    copyright = serializers.CharField()
    social = SocicalSerializer(many=True, read_only=True)
    pay_system = PaySystemSerializer(many=True, read_only=True)


    class Meta:
        model = Settings
        fields = ('logo', 'phone_main', 'phone_sec', 'copyright', 'social', 'pay_system')

class CatCollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingBanner
        fields = ('name', 'description', 'link', 'img_url', 'active')