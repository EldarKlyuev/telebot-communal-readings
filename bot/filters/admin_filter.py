from aiogram.filters import BaseFilter
from aiogram.types import Message

from decouple import config

from main import bot

ADMIN_TELEGRAM = config('ADMIN_TELEGRAM')

PERMISSION_ID = [ADMIN_TELEGRAM]

class AdminCreatorFilter(BaseFilter):
    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.is_admin, bool):
            user_id = message.from_user.id

            if str(user_id) in PERMISSION_ID:
                return True
            else:
                await message.answer("У тебя нет прав!")
                await bot.send_message(chat_id=ADMIN_TELEGRAM, 
                                       text=f"Привет чел! Кто-то без прав пытался выполнить команду {message.text}. Это происходило в группе {message.chat.full_name}. Его зовут {message.from_user.first_name}, его тэг @{message.from_user.username}")
                return False
        else:
            return message.chat.type in self.is_admin
