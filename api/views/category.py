from rest_framework.filters import SearchFilter

from users.permissions import IsAdminOrReadOnly
from .base import ListObjectsViewSet
from ..models import Category
from ..serializers.category import CategorySerializer


class CategoryViewSet(ListObjectsViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', ]
