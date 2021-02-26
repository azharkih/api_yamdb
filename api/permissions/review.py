from rest_framework import permissions

from users.models import User


class IsAuthorOrAdminOrModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            if request.method == 'POST':
                return True
            else:
                return (
                    obj.author == request.user
                    or request.user.role == User.Role.ADMIN
                    or request.user.role == User.Role.MODERATOR
                    or request.user.is_superuser
                )
