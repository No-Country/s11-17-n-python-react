from rest_framework import serializers
from apps.profiles.models import Profile
from apps.addresses.api.serializer import AddressSerializer
import re


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ("created", "updated")

    def validate_first_name(self, value):
        pattern = r'^[a-zA-Z\s]+$'
        if re.match(pattern, value):
            return value
        raise serializers.ValidationError("Solo se permiten letras")

    def validate_last_name(self, value):
        pattern = r'^[a-zA-Z\s]+$'
        if re.match(pattern, value):
            return value
        raise serializers.ValidationError("Solo se permiten letras")

    def validate_qualification(self, value):
        if value >= 0 and value <= 5:
            return value
        raise serializers.ValidationError("La calificacion no puede ser inferior a cero ni mayor a 5")
        fields = "__all__"


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("photo",)

    def update(self, instance, validated_data):
        instance.photo = validated_data.get("photo", instance.photo)
        instance.save()
        return instance
