from django.db import models
import uuid
from apps.abstracts.models import AbstractModel

# Create your models here.

AVATAR_FARM = "https://django-good-rabbit.s3.amazonaws.com/fotos/granjas/granja.jpg"


class Farm(AbstractModel):
    """
      It is a place where the farmer care their animals and
      manage them for trade.
    Args:
        name ( str ): farm name.
        address ( str ): farm address
        is_active ( bool ): logic delete
    """

    name = models.CharField(max_length=150, blank=False)
    address = models.CharField(max_length=150, blank=False)
    description = models.TextField(max_length=200)
    photo = models.ImageField(
        "Farms",
        upload_to="fotos/granjas/",
        default="granja.jpg",
        null=True,
        blank=True,
    )

    # Modifica como se visualiza el nombre de la clase en el admin
    # Como ordenar los datos en el admin
    class Meta:
        db_table = "farm"
        verbose_name = "farm"
        verbose_name_plural = "farm"
        ordering = ["name"]

    def __str__(self):
        return f"{self.id} {self.name} {self.address} {self.is_active}"
