import os
import time

import vk_api
import telegram

from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TOKEN = os.getenv('TOKEN')
TIME_TO_WAIT = 900

os.times_result

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)

def send_message(bot, message):
    """Функция отправки сообщений."""
    bot.send_message(-266756348, message)

def check_tokens():
    """Проверка получения токенов."""
    if not TELEGRAM_TOKEN or not TOKEN:
        return False
    else:
        return True

def main():
    check_tokens()
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    count = 0
    while True:
        try:
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.from_user:
                        msg = (f'В ВК пришло новое сообщение!: "{event.message}" '
                               f'от пользователя: {event.user_id}'
                               f'Ссылка: https://vk.com/gim25105787')
                        send_message(bot, msg)       
                        time.sleep(TIME_TO_WAIT)
        except Exception as error:
            if count < 1:
                print(error)
                send_message(bot,'Ошибка!')
                count += 1

if __name__ == '__main__':
    main()

