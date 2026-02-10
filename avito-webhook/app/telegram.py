import httpx
from app.config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

async def send_telegram_message(text: str):
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

  payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": text
  }

  async with httpx.AsyncClient(timeout=5) as client:
    await client.post(url, json=payload)
