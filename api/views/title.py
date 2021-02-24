from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from ..filters.title import TitleFilter
from ..models.title import Title
from ..serializers.title import TitleSerializerGet


class TitleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Title.objects
    # .annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializerGet
    lookup_field = 'name'
    #    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TitleFilter
