from django.core.validators import RegexValidator
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(source="username", required=False)

    class Meta(object):
        model = User
        fields = ['phone', 'email', 'first_name', 'last_name']


class UserInfoEditSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = User
        fields = ['first_name', 'last_name']

    def validate_email(self, value):
        user_id = self.instance.id
        existing_user = User.objects.filter(email=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that email already exists.")
        return value


class UserPhoneEditSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(source="username",
                                     validators=[RegexValidator(regex='^7[9][0-9]{9}$',
                                                                message='incorrect phone number')])
    code = serializers.IntegerField(validators=[RegexValidator(regex='^\d{4}$',
                                                               message='Code must be a 4-digit number')])

    class Meta(object):
        model = User
        fields = ['phone', 'code']

    def validate_phone(self, value):
        print(self.instance.id)
        if not (79000000000 <= value <= 79999999999):
            raise serializers.ValidationError("Phone number must be in the range of 79000000000 to 79999999999")
        user_id = self.instance.id
        existing_user = User.objects.filter(username=value).exclude(id=user_id).first()
        if existing_user:
            raise serializers.ValidationError("A user with that phone already exists.")
        return value




class PhoneSerializer(serializers.Serializer):
    username = serializers.IntegerField(validators=[RegexValidator(regex='^7[9][0-9]{9}$',
                                                                message='incorrect phone number')])
    code = serializers.IntegerField(validators=[RegexValidator(regex='^\d{4}$',
                                                               message='Code must be a 4-digit number')])