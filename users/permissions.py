from rest_framework import permissions

from users.models import User


class IsUser(permissions.BasePermission):
    """
    Класс IsUser используется для определения соответствия роли пользователя
    отправившего запрос как "обычный пользователь".

    Родительский класс -- permissions.BasePermission.
    Переопределенные методы -- has_permission.
    """

    def has_permission(self, request, view):
        """Определить и вернуть право на поступивший запрос."""
        if bool(request.user and request.user.is_authenticated):
            return request.user.role == User.Role.USER
        return False


class IsModerator(permissions.BasePermission):
    """
    Класс IsModerator используется для определения соответствия роли
    пользователя отправившего запрос как "модератор".

    Родительский класс -- permissions.BasePermission.
    Переопределенные методы -- has_permission.
    """

    def has_permission(self, request, view):
        """Определить и вернуть право на поступивший запрос."""
        if bool(request.user and request.user.is_authenticated):
            return request.user.role == User.Role.MODERATOR
        return False


class IsAdmin(permissions.BasePermission):
    """
    Класс IsAdmin используется для определения соответствия роли пользователя
    отправившего запрос как "администратор".

    Родительский класс -- permissions.BasePermission.
    Переопределенные методы -- has_permission.
    """

    def has_permission(self, request, view):
        """Определить и вернуть право на поступивший запрос."""
        if bool(request.user and request.user.is_authenticated):
            return (request.user.role == User.Role.ADMIN
                    or request.user.is_superuser)
        return False


class IsOwner(permissions.BasePermission):
    """
    Класс IsOwner используется для определения принадлежности запрашивоемой
    записи текущему пользователю.

    Родительский класс -- permissions.BasePermission.
    Переопределенные методы -- has_permission, has_object_permission.
    """

    def has_permission(self, request, view):
        """Определить и вернуть право на поступивший запрос."""
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Определить и вернуть право на доступ к объекту."""
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if bool(request.user and request.user.is_authenticated):
            return (request.user.role == User.Role.ADMIN
                    or request.user.is_superuser)
