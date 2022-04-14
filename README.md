# api_interview
Тестовое задание на использование API

Бот получает входящее сообщение от паблика с помощью API ключа ВКонтакте и переотправляет его копию в телеграмм,
через API Telegram

Использование:

В папке проекта:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

В скрипте:

chat_id_for_error = "chat_id_for error""  укажите chat_id, куда будут приходить сообщения.
chat_id = "chat_id"  укажите chat_id для переотправки сообщений.

В вашем виртуальном окружениии экспортируйте токены:
export TOKEN: "VK_TOKEN"
export TELEGRAM_TOKEN: "TELEGRAM_TOKEN"
