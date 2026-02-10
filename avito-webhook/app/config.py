import os
from dotenv import load_dotenv

load_dotenv()

AVITO_CLIENT_ID = os.getenv("AVITO_CLIENT_ID")
AVITO_CLIENT_SECRET = os.getenv("AVITO_CLIENT_SECRET")
AVITO_OAUTH_SCOPE = os.getenv("AVITO_OAUTH_SCOPE")

AVITO_WEBHOOK_URL = os.getenv("AVITO_WEBHOOK_URL")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
