from rest_framework import serializers
from apps.addresses.models import Address

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = ("id", "address", "state_id", "city_id")
        read_only_fields = ("created", "updated")