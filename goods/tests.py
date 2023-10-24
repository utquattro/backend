from django.test import TestCase
from goods.serializers import CombinedSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
from goods.api import Cat
from goods.models import Categorie


class CategoryTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(name="lion")

    def test_anima(self):
        """Animals that can speak are correctly identified"""
        ss = Cat().active_category
        print(ss)

