from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Конфигурация приложения пользователей.
    Настройка приложения для модели пользователей в Django.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
