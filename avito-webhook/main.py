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
