from rest_framework import serializers

from core.apps.api.models import CardModel


class BaseCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardModel
        fields = [
            "id",
            "name",
        ]


class ListCardSerializer(BaseCardSerializer):
    class Meta(BaseCardSerializer.Meta): ...


class RetrieveCardSerializer(BaseCardSerializer):
    class Meta(BaseCardSerializer.Meta): ...


class CreateCardSerializer(BaseCardSerializer):
    class Meta(BaseCardSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
