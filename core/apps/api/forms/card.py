from django import forms

from core.apps.api.models import CardModel


class CardForm(forms.ModelForm):

    class Meta:
        model = CardModel
        fields = "__all__"
