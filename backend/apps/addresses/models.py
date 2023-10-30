from django.db import models
from apps.abstracts.models import AbstractModel
from apps.catalogs.models import State, City

# Create your models here.
class Address(AbstractModel):
    """
     The address is extended of profile data.
    
    Args:
        state_id ( coolean ): prelated with state model
        city_id ( float ): related with with city model
        address ( str ): address of user
        is_active ( boolean ): logic delete.
    """

    state_id = models.ForeignKey(State, on_delete=models.CASCADE, related_name="state_address", null=True, blank=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_address", null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
   
    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"
