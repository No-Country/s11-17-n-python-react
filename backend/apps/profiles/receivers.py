from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.profiles.models import Profile
from apps.addresses.models import Address

@receiver(post_save, sender=Profile)
def create_address(sender, instance, created, **kwargs):
    if created:
        address = Address.objects.create()
        instance.address_id=address
        instance.save()