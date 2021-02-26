from rest_framework.filters import SearchFilter

from users.permissions import IsAdminOrReadOnly
from .base import ListObjectsViewSet
from ..models import Genre
from ..serializers.genre import GenreSerializer


class GenreViewSet(ListObjectsViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', ]
