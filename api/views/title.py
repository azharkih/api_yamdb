from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from users.permissions import IsAdminOrReadOnly
from ..models.title import Title
from ..serializers.title import TitleSerializerGet


class TitleViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Title.objects.all()
    # .annotate(rating=Avg('reviews__score'))
    serializer_class = TitleSerializerGet
    lookup_field = 'name'
    permission_classes = [IsAdminOrReadOnly, ]
