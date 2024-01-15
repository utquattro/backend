from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'email']


class UserEditSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta(object):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def validate_email(self, value):
        user_id = self.instance.id
        existing_user = User.objects.filter(email=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that email already exists.")
        return value

    def validate_username(self, value):
        user_id = self.instance.id
        existing_user = User.objects.filter(username=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that username already exists.")
        return value




class PhoneSerializer(serializers.Serializer):
    username = serializers.IntegerField()
    code = serializers.IntegerField()


class CheckCodeSerializer(serializers.Serializer):
    phone = serializers.IntegerField()


