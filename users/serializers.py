from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(source="username", required=False)

    class Meta(object):
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']


class UserEditSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(source="username", required=False)

    class Meta(object):
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']

    def validate_email(self, value):
        user_id = self.instance.id
        existing_user = User.objects.filter(email=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate_phone(self, value):
        user_id = self.instance.id
        existing_user = User.objects.filter(username=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that phone already exists.")
        return value




class PhoneSerializer(serializers.Serializer):
    username = serializers.IntegerField()
    code = serializers.IntegerField()


class CheckCodeSerializer(serializers.Serializer):
    phone = serializers.IntegerField()


