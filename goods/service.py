from django_filters import rest_framework as filters
from .models import ProductSku


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    characteristics = CharFilterInFilter(field_name='characteristics__value__value', lookup_expr='in')
    price = filters.RangeFilter()

    class Meta:
        model = ProductSku
        fields = ['characteristics', 'price']

