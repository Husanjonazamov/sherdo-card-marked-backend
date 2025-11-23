from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from model_bakery import baker



class CardModel(AbstractBaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="cards")
    card_number = models.CharField(max_length=16)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=10.000)
    
    def __str__(self):
        return str(self.user.first_name) + " - " + str(self.card_number)

    @classmethod
    def _baker(cls):
        return baker.make(cls)

    class Meta:
        db_table = "card"
        verbose_name = _("CardModel")
        verbose_name_plural = _("CardModels")
