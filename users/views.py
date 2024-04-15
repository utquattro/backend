from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django_project.services import generate_password, generate_name
from .serializers import (UserSerializer, UserPhoneEditSerializer,
                          UserInfoEditSerializer, PhoneSerializer)
from django_project.serializers import AddressSerializer
from django.contrib.auth import get_user_model
from django_project.services import get_address_list_from_dadata


def get_user_id_from_token(token):
    try:
        token_obj = Token.objects.get(key=token)
        user_id = token_obj.user_id
        return user_id
    except Token.DoesNotExist:
        return None


@api_view(['POST'])
def login_or_register(request):
    serializer = PhoneSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get('username')
        code = request.data.get('code')
        password = generate_password(12)
        name = generate_name(10)
        last_name = generate_name(16)
        if code == 1111:
            user = User.objects.filter(username=username).first()
            print(username)
            if user is None:
                # Если пользователя нет, создаем его с произвольным паролем
                user = User.objects.create_user(username, password=password, first_name=name, last_name=last_name)
                # Выдаем токен для нового пользователя
                token = Token.objects.create(user=user)
                return Response({'token': token.key})
            else:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
        else:
            return Response({"code": 1001,
                             "message": "ivalid code"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_user_info(request):
    token = request.auth
    user = Token.objects.get(key=token).user
    user_data = JSONParser().parse(request)
    user_data_serializer = UserInfoEditSerializer(user, data=user_data)
    if user_data_serializer.is_valid():
        user_data_serializer.save()
        return JsonResponse(user_data_serializer.data)
    return JsonResponse(user_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_user_phone(request):
    token = request.auth
    user = Token.objects.get(key=token).user
    user_data = JSONParser().parse(request)

    user_data_serializer = UserPhoneEditSerializer(user, data=user_data)
    if user_data_serializer.is_valid():
        if user_data['code'] == 1111:
            user_data_serializer.save()
            print(type(user_data_serializer.data))
            return JsonResponse(user_data_serializer.data)
        else:
            return Response({"code": 1001,
                             "message": "ivalid code"}, status=status.HTTP_400_BAD_REQUEST)

    return JsonResponse(user_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profile_info(request):
    token = request.auth
    user = Token.objects.get(key=token).user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def send_sms(request):
    try:
        phone = request.data['phone']
        return Response({"status": "ok",
                         "sent": phone}, status=status.HTTP_200_OK)
    except KeyError as e:
        return Response({"key error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_token(request):
    request.user.auth_token.delete()
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_address_list(request):
    address = request.GET.get('address', '')
    if address and len(address) > 3:
        data = get_address_list_from_dadata(address)
        ser = AddressSerializer(data, many=True)
        return Response(ser.data)
    else:
        return Response([], status=404)
