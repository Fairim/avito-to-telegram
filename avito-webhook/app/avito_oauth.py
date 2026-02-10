import httpx
from app.config import (
  AVITO_CLIENT_ID,
  AVITO_CLIENT_SECRET
)

TOKEN_URL = "https://api.avito.ru/token"

async def get_access_token() -> str:
  data = {
    "grant_type": "client_credentials",
    "client_id": AVITO_CLIENT_ID,
    "client_secret": AVITO_CLIENT_SECRET
  }

  async with httpx.AsyncClient(timeout=10) as client:
    r = await client.post(TOKEN_URL, data=data)
    r.raise_for_status()
    return r.json()["access_token"]
