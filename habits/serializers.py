from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import (
    DurationTimeValidator,
    PleasantHabitValidator,
    RegularityValidator,
    RelatedHabitValidator,
    RewardValidator,
)


class HabitSerializer(ModelSerializer):
    """Сериализатор для модели Habit с встроенными валидаторами"""

    class Meta:
        """Метаданные сериализатора Habit"""

        model = Habit
        fields = "__all__"

    validators = [
        RewardValidator(field1="reward", field2="related_habit"),
        RelatedHabitValidator(field="related_habit"),
        DurationTimeValidator(field="duration"),
        PleasantHabitValidator(field="is_nice_habit"),
        RegularityValidator(field1="frequency_number", field2="frequency_unit"),
    ]
