from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Пагинатор для модели Habit, ограничивающий количество объектов на странице"""

    page_size = 5  # Количество объектов на одной странице по умолчанию
    page_size_query_param = (
        "page_size"  # Параметр запроса для изменения размера страницы
    )
    max_page_size = 10  # Максимально допустимое количество объектов на странице
