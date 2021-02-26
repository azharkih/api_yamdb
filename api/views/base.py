from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListObjectsViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.DestroyModelMixin,
                         GenericViewSet):
    """ Класс ListObjectsViewSet используется для обеспечения действий create()
    и list().
    """
    pass
