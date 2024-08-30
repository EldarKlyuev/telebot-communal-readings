import datetime
import requests
from decouple import config

from aiogram import Router, F
from aiogram import types
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from filters.admin_filter import AdminCreatorFilter
from filters.chat_type import GroupTypeFilter
from keyboards.keyboards import get_start_keyboard


router = Router()

SERVER_API = config('SERVER_API')


@router.message(
    Command(commands=['start']),
    AdminCreatorFilter(is_admin=True)
)
async def cmd_start(message: Message):
    """Start command"""

    await message.answer(
        f'@{message.from_user.username}, привет! Ты хочешь подать показания?',
        reply_markup=get_start_keyboard()
    )


@router.message(
    Command(commands=["test"])
)
async def cmd_test(message: Message):
    r = requests.get(SERVER_API)
    if r.status_code == 200:
        await message.answer('Бек работает')
    await message.answer(f"@{message.from_user.username}, я работаю!")


@router.message(
    Command(commands=["getmyid"]),
)
async def cmd_get_chat_id(message: Message):
    """Получение свое ChatID"""
    user_id = message.from_user
    await message.answer(f"""@{user_id.username}, привет!\nТвой chatId = {user_id.id}""")


@router.callback_query(
    F.data == 'cancel'
)
async def cmd_cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )