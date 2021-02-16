from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListObjectsViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         GenericViewSet):
    """ Класс ListObjectsViewSet используется для обеспечения действий create()
    и list().
    """
    pass


class ProtectObjectIdViewSet(mixins.RetrieveModelMixin,
                             mixins.UpdateModelMixin,
                             GenericViewSet):
    """ Класс ListObjectsViewSet используется для обеспечения действий
    retrieve(), update().
    """
    pass


class ObjectIdViewSet(ProtectObjectIdViewSet,
                      mixins.DestroyModelMixin):
    """ Класс ListObjectsViewSet используется для обеспечения действий
    retrieve(), update(), destroy().
    """
    pass
