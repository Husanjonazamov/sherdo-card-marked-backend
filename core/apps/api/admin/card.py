from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CardModel


@admin.register(CardModel)
class CardAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
