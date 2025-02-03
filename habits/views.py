from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginations import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


@method_decorator(
    name="list", decorator=swagger_auto_schema(operation_description="Cписок привычек")
)
class HabitViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с привычками пользователя.
    Позволяет выполнять CRUD-операции над привычками, доступными только для аутентифицированных пользователей.
    Предоставляет функционал поиска и сортировки по полю 'action' и 'time'.
    """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ("action",)
    ordering_fields = ("time",)
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Возвращает список привычек текущего пользователя, отсортированный по ID.
        """
        return Habit.objects.filter(user=self.request.user.pk).order_by("id")

    def perform_create(self, serializer):
        """
        Выполняет создание новой привычки с присвоением текущего пользователя.
        """
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class PublicHabitListAPIView(ListAPIView):
    """
    Представление для получения публичных привычек.
    Возвращает список привычек, которые помечены как публичные.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitPaginator
