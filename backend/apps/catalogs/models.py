from django.db import models
from apps.abstracts.models import AbstractModel


# Create your models here.
class State(AbstractModel):
    """
      It is relevant to know that rabbits farms are
      geographically distributed, so the state catalog
      does exists for that functionality.

    Args:
        state(str): The name or description of the state.

    Meta:
        the real postgreSQL table name is "states_catalog";
        General presentation of the state catalog is ordered by state name.

    Comments:
        The state catalog is read-only in any use case.
    """

    state = models.CharField(max_length=25)

    class Meta:
        db_table = "states_catalog"
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["state"]

    def __str__(self):
        return self.state


class City(AbstractModel):
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name="state_city"
    )
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "cities_catalog"
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["city"]

    def __str__(self):
        return self.city


class Breed(AbstractModel):
    breed = models.CharField(max_length=80)

    class Meta:
        db_table = "breeds_catalog"
        verbose_name = "breed"
        verbose_name_plural = "breeds"
        ordering = ["breed"]

    def __str__(self):
        return self.breed