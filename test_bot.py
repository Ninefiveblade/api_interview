import os
import time

import vk_api
import telegram
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')  # Получаем токен VK.
TOKEN = os.getenv('TOKEN')  # Получаем токен Telegram.
TIME_TO_WAIT = 60  # Время ожидания между запросами.

vk_session = vk_api.VkApi(token=TOKEN)  # Авторизируем сессию в ВК.
longpoll = VkLongPoll(vk_session)  # Подключаем Long Polling для получения сообщений.
chat_id_for_error = 957044130  # Чат ID автора, на случай ошибки.
chat_id = 957044130  # целевой Чат ID для отправки собщений.

def send_message(bot, message):
    """Функция отправки сообщений."""
    bot.send_message(chat_id, message)

def check_tokens():
    """Проверка получения токенов."""
    if not TELEGRAM_TOKEN or not TOKEN:
        return False
    else:
        return True

def main():
    """Основная функция запуска.
       longpoll.listen() - ожидаем обновлений с сервера.
       Если пришло нове сообщение, то пересылаем
       его в телеграмм с указанным chat_id"""
    check_tokens()
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    count = 0
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.from_user:
                        msg = (f'В ВК пришло новое сообщение!: "{event.message}" '
                               f'от пользователя: {event.user_id} ')
                        send_message(bot, msg)       
                        time.sleep(TIME_TO_WAIT)
        except Exception as error:
            if count < 1:
                bot.send_message(chat_id_for_error, f"Ошибка: {error}")
                count += 1

if __name__ == '__main__':
    main()

