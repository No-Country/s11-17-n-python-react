from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address",
        "state_id",
        "city_id",
    )
    search_fields = (
        "state_id",
        "city_id",
    )
    ordering = ("city_id",)


admin.site.register(Address, AddressAdmin)
