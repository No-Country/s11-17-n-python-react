from django.db import models
from apps.cages.models import Cage
from apps.abstracts.models import AbstractModel
from django.utils import timezone

AVATAR_RABBIT = "https://django-good-rabbit.s3.amazonaws.com/fotos/conejos/conejo.jpg"


# Create your models here.
class Rabbit(AbstractModel):
    """
    The animal of the farm for trade.

    Args:
        cage_id (str): related with cage model
        breed (str): breed of the rabbit
        genre (str): genre of the rabbit
        price (decimal): public price for trade
        tag (str): identifier od the rabbit
        weight (decimal): weight of the rabbit
        is_active (boolean): logic delete

    """

    BREED_CHOICE = (
        ("Azteca", "Azteca"),
        ("Cabeza de León", "Cabeza de León"),
        ("California", "California"),
        ("Chinchilla", "Chinchilla"),
        ("Gigante de Flandes", "Gigante de Flandes"),
        ("Mariposa", "Mariposa"),
        ("Nueva Zelanda", "Nueva Zelanda"),
        ("Rex", "Rex"),
        ("Otro", "Otro"),
    )
    GENDER_CHOICE = (
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
    )

    cage_id = models.ForeignKey(Cage, on_delete=models.CASCADE)
    breed = models.CharField(choices=BREED_CHOICE, blank=False, default="Especie")
    genre = models.CharField(choices=GENDER_CHOICE, blank=False, default="Genero")
    birthday = models.DateField(null=False, blank=False, default=timezone.now)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    tag = models.CharField(max_length=15, unique=True, blank=False)
    weight = models.DecimalField(max_digits=3, decimal_places=1, default=1)
    photo = models.ImageField(
        "Rabbits",
        upload_to="fotos/conejos/",
        default="conejo.jpg",
        null=True,
        blank=True,
    )
