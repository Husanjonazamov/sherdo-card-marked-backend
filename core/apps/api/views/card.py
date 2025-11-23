from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import CardModel
from core.apps.api.serializers.card import CreateCardSerializer, ListCardSerializer, RetrieveCardSerializer


@extend_schema(tags=["card"])
class CardView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CardModel.objects.all()
    serializer_class = ListCardSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCardSerializer,
        "retrieve": RetrieveCardSerializer,
        "create": CreateCardSerializer,
    }
