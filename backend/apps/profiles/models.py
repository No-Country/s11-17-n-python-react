from django.db import models
import uuid
from apps.users.models import User
from apps.addresses.models import Address


# Create your models here.
class Profile(models.Model):
    """
     The Profile is extended user date.

    Args:
        user_id ( str ): related with user model
        is_producer ( coolean ): productor or user
        qualifications ( float ): average of the grades obtained
        is_active ( boolean ): logic delete.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    is_producer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.CharField(max_length=255, blank=True)
    address_id = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    qualification = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
