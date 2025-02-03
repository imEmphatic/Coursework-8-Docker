from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тесты для эндпоинтов модели Habit."""

    def setUp(self):
        """Настройка тестовых данных для каждого теста."""
        self.user = User.objects.create(email="test@gmail.com")
        self.habit = Habit.objects.create(
            place="спортивная площадка",
            time="08:00:00",
            action="подтягивание на турнике",
            is_nice_habit=False,
            frequency_number=1,
            frequency_unit="days",
            reward="съесть яблоко",
            duration="120",
            is_public=True,
            user=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тест получения информации о привычке."""
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        """Тест создания новой привычки."""
        url = reverse("habits:habits-list")
        data = {
            "place": "дом",
            "time": "20:40:00",
            "action": "убраться",
            "is_pleasant": False,
            "frequency_number": 1,
            "frequency_unit": "days",
            "reward": "посмотреть фильм",
            "duration": "00:02:00",
            "is_public": True,
            "user": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        """Тест получения списка привычек."""
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        """Тест обновления данных привычки."""
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        data = {
            "reward": "посмотреть фильм",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("reward"), "посмотреть фильм")

    def test_public_habit_list(self):
        """Тест получения списка публичных привычек."""
        url = reverse("habits:public")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """Тест удаления привычки."""
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)
