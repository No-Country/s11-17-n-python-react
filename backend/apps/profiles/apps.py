from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = "apps.profiles"
    label = "apps_profiles"

    class Meta:
        verbose_name = "Perfiles"

    def ready(self):
        from . import receivers