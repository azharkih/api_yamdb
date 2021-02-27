from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from users.permissions import IsAdminOrReadOnly
from ..filters import TitleFilter
from ..models import Title
from ..serializers.title import TitleSerializer, TitleSerializerGet


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    permission_classes = [IsAdminOrReadOnly, ]

    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleSerializerGet
        return TitleSerializer
