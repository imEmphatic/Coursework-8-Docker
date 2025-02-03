from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя с предустановленными учетными данными"""

    def handle(self, *args, **options):
        """Создает суперпользователя с указанным email и паролем"""
        user = User.objects.create(email="admin@sky.pro")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password("123")
        user.save()
