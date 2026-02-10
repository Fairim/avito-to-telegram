import httpx
from app.avito_oauth import get_access_token
from app.config import AVITO_WEBHOOK_URL

SUBSCRIBE_URL = "https://api.avito.ru/messenger/v3/webhook"

async def subscribe_webhook():
  token = await get_access_token()

  headers = {
    "Authorization": f"Bearer {token}"
  }

  payload = {
    "url": AVITO_WEBHOOK_URL
  }

  async with httpx.AsyncClient(timeout=10) as client:
    r = await client.post(
      SUBSCRIBE_URL,
      json=payload,
      headers=headers
    )

    if r.status_code not in (200, 201):
      raise RuntimeError(
        f"Webhook subscribe failed: {r.status_code} {r.text}"
      )
