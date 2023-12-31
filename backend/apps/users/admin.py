from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_active")
    search_fields = ("username", "email")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
