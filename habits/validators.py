from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:
    """Проверяет корректность соотношения двух полей (reward и related_habit)."""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        """Проверяет значения полей. Если оба поля заполнены, выбрасывает ошибку."""
        tmp_val1 = dict(value).get(self.field1)
        tmp_val2 = dict(value).get(self.field2)
        if tmp_val1 and tmp_val2:
            raise ValidationError("Неправильное соотношение полей")


class RelatedHabitValidator:
    """Проверяет, чтобы связанная привычка была приятной."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Проверяет значение поля related_habit. Если оно указано, то проверяет is_pleasant."""
        tmp_val = dict(value).get(self.field)
        if tmp_val:
            if not tmp_val.is_pleasant:
                raise ValidationError("Неправильно заполнено поле приятной привычки")


class DurationTimeValidator:
    """Проверяет продолжительность действия привычки (не более 120 секунд)."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Проверяет значение поля продолжительности. Если продолжительность больше 120 секунд, выбрасывает ошибку."""
        tmp_val = dict(value).get(self.field)
        print(tmp_val)
        if tmp_val is not None and tmp_val > timedelta(seconds=120):
            raise ValidationError("Продолжительность не может превышать 120 секунд")


class PleasantHabitValidator:
    """Проверяет, что у приятной привычки не может быть вознаграждения или связанной привычки."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Проверяет, что у приятной привычки нет значения в полях reward или related_habit."""
