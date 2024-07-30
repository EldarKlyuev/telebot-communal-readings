import datetime

from aiogram import Router, F
from aiogram import types
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from filters.admin_filter import AdminCreatorFilter
from filters.chat_type import GroupTypeFilter
from aiogram.types import Message, ReplyKeyboardRemove

router = Router()


@router.message(
    Command(commands=['start']),
    AdminCreatorFilter(is_admin=True)
)
async def cmd_start(message: Message):
    """Start command"""

    buttons = [
        [InlineKeyboardButton(text="Подать Школьную", callback_data="post_shk")],
        [InlineKeyboardButton(text="Подать Зиповскую", callback_data="post_zip")],
        [InlineKeyboardButton(text="Отчет PDF", callback_data="get_all_pdf")],
        [InlineKeyboardButton(text="Отчет в сообщении", callback_data="get_all")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        f'@{message.from_user.username}, привет! Ты хочешь подать показания?',
        reply_markup=keyboard
    )


@router.message(
    Command(commands=["test"])
)
async def cmd_test(message: Message):
    """Проверка работоспособности"""
    await message.answer(f"@{message.from_user.username}, я работаю!")


@router.message(
    Command(commands=["getmyid"]),
)
async def cmd_get_chat_id(message: Message):
    """Получение свое ChatID"""
    user_id = message.from_user
    await message.answer(f"""@{user_id.username}, привет!\nТвой chatId = {user_id.id}""")


@router.message(Command(commands=["cancel"]))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )