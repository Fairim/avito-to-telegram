from app.telegram import send_telegram_message

async def handle_avito_event(data: dict):
  # интересуют только новые сообщения
  if data.get("event") != "message.created":
    return

  message = data.get("message", {})

  # игнорируем системные сообщения (боты Авито)
  if message.get("type") == "system":
    return

  text = message.get("content", {}).get("text")
  if not text:
    return

  chat_id = data.get("chat_id")
  user_id = data.get("user_id")

  await send_telegram_message(
    f"📩 Новое сообщение Avito\n\n"
    f"👤 user_id: {user_id}\n"
    f"💬 chat_id: {chat_id}\n\n"
    f"{text}"
  )
