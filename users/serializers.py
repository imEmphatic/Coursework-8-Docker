from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели пользователя.
    Позволяет конвертировать данные пользователя в формат JSON и наоборот.
    Включает все поля модели User.
    """

    class Meta:
        model = User
        fields = "__all__"  # Включаем все поля модели пользователя
