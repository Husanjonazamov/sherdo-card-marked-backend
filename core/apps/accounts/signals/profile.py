from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import ProfileModel


@receiver(post_save, sender=ProfileModel)
def ProfileSignal(sender, instance, created, **kwargs): ...
