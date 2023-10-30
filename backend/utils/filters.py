from apps.users.models import User
from django_filters import rest_framework
from apps.rabbits.models import Rabbit
from apps.cages.models import Cage
from apps.addresses.models import Address


class UserFilterSet(rest_framework.FilterSet):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class RabbitFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Rabbit
        fields = (
            "created",
            "breed",
            "genre",
            "birthday",
            "price",
            "tag",
            "weight",
            "cage_id",
            "is_active",
        )


class CageFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Cage
        fields = (
            "count_rabbits",
            "price",
            "farm_id",
            "is_public",
            "is_active",
            "total_weight",
        )
        ordering = ("created",)

class AddressFilterSet(rest_framework.FilterSet):
    class Meta:
        model = Address
        fields = (
            'address', 
            'state_id__state', 
            'city_id__city'
        )
        ordering = ("created",)