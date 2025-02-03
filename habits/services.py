import requests
from django.conf import settings
from django.utils.timezone import localtime
from rest_framework import status


def send_telegram(habit):
    """Отправляет уведомление в Telegram о запланированной привычке.

    Args:
        habit (Habit): Экземпляр привычки, содержащий информацию о действии, времени и пользователе.

    Отправляет сообщение в Telegram через API, используя токен бота из настроек.
    Если запрос неуспешен, выводит ошибку в консоль.
    """
    local_habit_time = localtime(habit.time)
    formatted_time = local_habit_time.strftime("%H:%M")

    text = f"{habit.action} запланировано сегодня на {formatted_time}"
    chat_id = habit.user.tg_chat_id
    params = {"text": text, "chat_id": chat_id}

    response = requests.get(
        f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", data=params
    )
    if response.status_code != status.HTTP_200_OK:
        print(f"Ошибка: {response.text}")
