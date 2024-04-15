from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    value = serializers.CharField()
    unrestricted_value = serializers.CharField()
    fias_id = serializers.CharField()
    city = serializers.CharField()
