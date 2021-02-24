from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.permissions import IsAdminOrReadOnly
from ..filters.genre import GenreFilter
from ..models.genre import Genre
from ..serializers.genre import GenreSerializer


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = GenreFilter
