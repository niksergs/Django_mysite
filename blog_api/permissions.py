from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Переопределяем класс разрешений,
    что бы только автор записи имел права на ее редактирование и удаление"""
    def has_permission(self, request, view):
        """Только аутентифицированные пользователи могут видеть представление списка постов"""
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Разрешение на чтение есть для любого запроса, поэтому мы всегда будем
        разрешать запросы GET, HEAD или OPTIONS"""
        if request.method in permissions.SAFE_METHODS:
            return True
        """Права на запись есть только у автора поста и у администратора"""
        return obj.author == request.user or request.user.is_staff
