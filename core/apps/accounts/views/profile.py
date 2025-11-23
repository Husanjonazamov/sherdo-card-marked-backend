from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import ProfileModel
from core.apps.accounts.serializers.profile import (
    CreateProfileSerializer,
    ListProfileSerializer,
    RetrieveProfileSerializer,
)


@extend_schema(tags=["profile"])
class ProfileView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProfileModel.objects.all()
    serializer_class = ListProfileSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProfileSerializer,
        "retrieve": RetrieveProfileSerializer,
        "create": CreateProfileSerializer,
    }
