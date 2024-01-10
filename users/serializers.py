from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email']


class PhoneSerializer(serializers.Serializer):
    username = serializers.IntegerField()
    code = serializers.IntegerField()


