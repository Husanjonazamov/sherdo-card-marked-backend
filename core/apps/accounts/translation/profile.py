from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import ProfileModel


@register(ProfileModel)
class ProfileTranslation(TranslationOptions):
    fields = []
