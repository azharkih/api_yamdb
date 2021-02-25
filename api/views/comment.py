from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from api.models.comment import Comment


class CommentViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass