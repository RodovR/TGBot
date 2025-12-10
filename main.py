# 837384034
import requests
import asyncio
from aiogram import Bot, Dispatcher, types

# TOKEN = "5796916709:AAHix0lHDYj6xVjOb2QhKH3NszL1y2WfxxM"
# CHAT_ID = "837384034"  # Вставь полученный номер

# response = requests.post(
#     f"https://api.telegram.org/bot{TOKEN}/sendMessage",
#     json={
#         "chat_id": CHAT_ID,
#         "text": "✅ Бот работает!",
#         "parse_mode": "HTML"
#     }
# )
#
# print("Статус:", response.status_code)
# print("Ответ:", response.json())

class CreateBot:
    def __init__(self):
        self.bot = Bot(token='')

class User:
    pass

class GetCards:
    pass

class Manager:
    pass

class Notification:
    pass