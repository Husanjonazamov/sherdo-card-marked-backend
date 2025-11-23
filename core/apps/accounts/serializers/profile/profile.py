from rest_framework import serializers

from core.apps.accounts.models import ProfileModel


class BaseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = [
            "id",
            "name",
        ]


class ListProfileSerializer(BaseProfileSerializer):
    class Meta(BaseProfileSerializer.Meta): ...


class RetrieveProfileSerializer(BaseProfileSerializer):
    class Meta(BaseProfileSerializer.Meta): ...


class CreateProfileSerializer(BaseProfileSerializer):
    class Meta(BaseProfileSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
