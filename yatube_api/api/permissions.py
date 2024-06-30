from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Класс для проверки авторства."""

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                ) or obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    """Класс, разрешающий только метододы для чтения."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        raise MethodNotAllowed('Этот метод доступен только администратору!')

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        raise MethodNotAllowed('Этот метод доступен только администратору!')
