from rest_framework import serializers
from .models import Phone


class PhoneSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('number', 'number', 'description')

# class LogoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Logo
#         fields = ('logo_url',)
#
#
# class PaySystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaySystem
#         fields = ('pay_system_name', 'img_url', 'description',)
#
#
#
#
#
# class SocicalSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Socical
#         fields = ('name', 'description', 'link', 'img_url', )
#
#
# class CopyrightSystemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Copyright
#         fields = ('name', 'description',)

