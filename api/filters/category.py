from django_filters import rest_framework as filters

from ..models.category import Category


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']
