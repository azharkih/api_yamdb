from rest_framework import mixins, permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

#from django.db.models import Avg

from users.permissions import IsAdminOrReadOnly
from ..models.title import Title
from ..serializers.title import TitleSerializer, TitleSerializerGet


class TitleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Title.objects.all() #queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = [SearchFilter]
    search_fields = ['genre__slug', ]

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return TitleSerializerGet
        else:
            return TitleSerializer
