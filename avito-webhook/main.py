from fastapi import FastAPI, Request
from app.avito_events import handle_avito_event
from app.avito_webhooks import subscribe_webhook
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
print("🔥🔥🔥 APP STARTED 🔥🔥🔥")


@app.on_event("startup")
async def startup():
  await subscribe_webhook()

@app.post("/webhook/avito")
async def avito_webhook(request: Request):
  logger.warning("🔥 AVITO WEBHOOK RECEIVED 🔥")
  logger.warning(request)
  data = await request.json()
  try:
    await send_telegram(f"Webhook test: {request}")
  except Exception:
    logger.exception("Telegram send failed")
  await handle_avito_event(data)
  return {"ok": True}

@app.get("/check-webhook")
async def check_webhook():
    token = await get_access_token()

    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://api.avito.ru/messenger/v3/webhook",
            headers={"Authorization": f"Bearer {token}"}
        )

    return r.json()

