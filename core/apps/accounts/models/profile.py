from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from model_bakery import baker


class ProfileModel(AbstractBaseModel):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name="profile")
    class Types(models.TextChoices):
        STANDARD = "standard", _("Standard")
        PREMIUM = "premium", _("Premium")
    
    profile_type = models.CharField(max_length=20, choices=Types.choices, default=Types.STANDARD)
    
    def __str__(self):
        return str(self.user.first_name) + " - " + str(self.profile_type)

    @classmethod
    def _baker(cls):
        return baker.make(cls)

    class Meta:
        db_table = "profile"
        verbose_name = _("ProfileModel")
        verbose_name_plural = _("ProfileModels")
