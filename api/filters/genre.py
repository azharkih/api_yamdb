from django_filters import rest_framework as filters

from ..models.genre import Genre


class GenreFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Genre
        fields = ['name']
