from django_filters import rest_framework as filters

from core.apps.accounts.models import ProfileModel


class ProfileFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ProfileModel
        fields = [
            "name",
        ]
