from django import forms

from core.apps.accounts.models import ProfileModel


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ProfileModel
        fields = "__all__"
