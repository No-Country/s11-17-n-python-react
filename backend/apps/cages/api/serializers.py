from rest_framework import serializers
from apps.cages.models import Cage


class CageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = "__all__"
        read_only_fields = ( "id", "price", "count_rabbits", "total_weight", "created",)
