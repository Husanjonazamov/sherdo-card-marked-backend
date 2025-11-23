from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CardModel


@register(CardModel)
class CardTranslation(TranslationOptions):
    fields = []
