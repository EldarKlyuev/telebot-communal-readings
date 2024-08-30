from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode

from keyboards.keyboards import get_shk_keyboard

router = Router()

@router.callback_query(F.data == 'post_shk')
async def callback_zip_start(callback: types.CallbackQuery):
    await callback.message.answer(
        "Что хотите подать?",
        reply_markup=get_shk_keyboard()
    )
