from django.apps import AppConfig


class AddressesConfig(AppConfig):
    name = "apps.addresses"
    label = "apps_addresses"

    class Meta:
        verbose_name = "Direcciones"
