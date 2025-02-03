from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Разрешение, позволяющее доступ только владельцу объекта"""

    def has_object_permission(self, request, view, obj):
        """Проверяет, является ли пользователь владельцем объекта"""
        return obj.user == request.user
