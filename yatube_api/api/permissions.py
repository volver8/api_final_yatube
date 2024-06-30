from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс для проверки авторства."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                ) or obj.author == request.user
