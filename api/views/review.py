from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models.review import Review


class ReviewViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass