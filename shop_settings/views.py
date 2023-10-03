from django.shortcuts import render
from .api import create_test_value, main_page_setup

from shop_settings.models import Copyright, PaySystem, Phone, Logo, Socical
from rest_framework import viewsets
from rest_framework.response import Response


def index(request):
    dd = main_page_setup()
    data = {"setup": dd}
    return render(request, "index.html", context=data)


def create_settings_value(request):
    create_test_value()
    dd = '21312'
    data = {"header": "Hello Django", "message": dd}
    return render(request, "index.html", context=data)


class MainPageSetup(viewsets.ViewSet):
    def list(self, request):
        return Response(main_page_setup())

