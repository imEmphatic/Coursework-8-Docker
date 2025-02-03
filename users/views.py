from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с пользователями.
    Позволяет выполнять CRUD операции (создание, чтение, обновление, удаление)
    с моделью User. Доступ разрешен любому пользователю (AllowAny).
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """
        Переопределяем метод создания пользователя.
        После сохранения пользователя, устанавливаем его пароль
        с использованием метода set_password для хеширования.
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
