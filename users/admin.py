from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Админская модель для пользователя.
    Позволяет фильтровать пользователей по ID и email в интерфейсе администрирования.
    """

    list_filter = ("id", "email")
