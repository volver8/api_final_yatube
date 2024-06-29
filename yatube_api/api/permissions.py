from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Класс для проверки авторства."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
