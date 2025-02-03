from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Настройки отображения модели Habit в админ-панели Django"""

    list_display = (
        "user",
        "action",
    )
