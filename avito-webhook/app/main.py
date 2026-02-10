from fastapi import FastAPI, Request
from app.avito_events import handle_avito_event
from app.avito_webhooks import subscribe_webhook

app = FastAPI()

@app.on_event("startup")
async def startup():
  await subscribe_webhook()

@app.post("/webhook/avito")
async def avito_webhook(request: Request):
  data = await request.json()
  await handle_avito_event(data)
  return {"ok": True}
