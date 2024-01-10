from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, PhoneSerializer

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
    return Response(serializer.errors, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    try:
        user = get_object_or_404(User, username=request.data['username'])
        if not request.data['code'] == 1111:
            return Response({"code": 1001,
                             "message": "ivalid code"}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key})
    except KeyError as e:
        return Response({"code": 1002,
                         "message": f"invalid key {e}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_profile_info(request):
    token = request.auth
    user = Token.objects.get(key=token).user
    user_info = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    }
    return Response(user_info)

@api_view(['POST'])
def send_sms(request):
    try:
        phone = request.data['phone']
        return Response({"status": "ok",
                         "sent": phone}, status=status.HTTP_200_OK)
    except KeyError as e:
        return Response({"key error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_token(request):
    request.user.auth_token.delete()
    return Response({"status": "ok"}, status=status.HTTP_200_OK)

