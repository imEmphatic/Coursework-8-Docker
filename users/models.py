from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """
    Модель пользователя.
    Наследуется от AbstractUser и расширяется дополнительными полями:
    - email (используется как основной идентификатор пользователя);
    - avatar (аватар пользователя);
    - tg_chat_id (chat-id пользователя в Telegram).
    """

    username = None  # Убираем поле username, так как используем email как уникальный идентификатор
    email = models.EmailField(verbose_name="почта", unique=True)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="аватар", **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Телеграм chat-id", **NULLABLE
    )

    USERNAME_FIELD = "email"  # Указываем email как основной идентификатор пользователя
    REQUIRED_FIELDS = []  # Оставляем пустым, так как email уже указан в USERNAME_FIELD

    def __str__(self):
        """
        Строковое представление пользователя — возвращает его email.
        """
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
