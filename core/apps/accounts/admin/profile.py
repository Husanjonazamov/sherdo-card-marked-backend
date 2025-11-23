from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import ProfileModel


@admin.register(ProfileModel)
class ProfileAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
