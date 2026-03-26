# Пересылка сообщений работает только при работе с авито с оплатой за просмотры.
## На пустом сервере:
### Установка всех необходимых пакетов
- `sudo apt update && sudo apt upgrade -y` - обновление всех инструментов для загрузки
- `sudo apt install -y python3 python3-pip python3-venv` - установка пакетов Python
- `git clone https://github.com/Fairim/avito-to-telegram.git` - клонирование репозитория на сервер

## Основные действия  
1. Переходим в папку для работы с сервером `cd avito-to-telegram/avito-webhook/`
2. Разворачиваем виртуальное окружение `python3 -m venv venv`
3. Активируем виртуальное окружение `source venv/bin/activate`
4. Устанавливаем все необходимые библиотеки в окружение `pip install -r requirements.txt`
5. Создаем файл `.env`, который будет хранить наши секреты `touch .env`
6. Входим в редактор файла `nano .env` вставляем следующие строки
  
AVITO_CLIENT_ID={ID клиента в личном кабинете авито}  
AVITO_CLIENT_SECRET={secret клиента в личном кабинете авито}  
AVITO_OAUTH_SCOPE=messenger:read  
TELEGRAM_BOT_TOKEN={API бота в BotFather}  
TELEGRAM_CHAT_ID={Личный токен, для отправки сообщения именно вам}  
  
8. Заполняем все данные, нажимаем комбинации клавиш и enter для каждой комбинации `ctrl+o`, `ctrl+x`
9. Настроем автозапуск, откроем файл `sudo nano /etc/systemd/system/telegram-bot.service` и вставим следующее:
  
[Unit]  
Description=My Telegram Bot  
After=network.target  
  
[Service]  
Type=simple  
User=root  
WorkingDirectory=/root/avito-to-telegram/avito-webhook  
Environment="PATH=/root/avito-to-telegram/avito-webhook/venv/bin"  
EnvironmentFile=/root/avito-to-telegram/avito-webhook/.env  
ExecStart=/root/avito-to-telegram/avito-webhook/venv/bin/pyhon3 /root/avito-to-telegram/avito-webhook/main.py  
Restart=always  
RestartSec=10  
  
[Install]  
WantedBy=multi-user.target  

10. Сохраняем изменения, нажимаем комбинации клавиш и enter для каждой комбинации `ctrl+o`, `ctrl+x`
11. Запустим сервис и добавим его в автозагрузку
12. `sudo systemctl daemon-reload`
13. `sudo systemctl enable telegram-bot.service`
14. `sudo systemctl start telegram-bot.service`

## Проверка 
