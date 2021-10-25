from appRestaurante.models.address import Address
from rest_framework import serializers
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('calle', 'no_calle','barrio')