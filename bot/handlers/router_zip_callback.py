from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode

from keyboards.keyboards import get_zip_keyboard

router = Router()


@router.callback_query(F.data == 'post_zip')
async def callback_zip_start(callback: types.CallbackQuery):
    await callback.message.answer(
        "Что хотите подать?",
        reply_markup=get_zip_keyboard()
    )


@router.callback_query(F.data.startswith('post_zip_'))
async def callbacks_post_zip(callback: types.CallbackQuery):
    action = callback.data.split('_')[2]

    if action == 'cold':
        # TODO: запрос на добавление холодной
        await callback.message.answer('cold')
    elif action == 'warm':
        # TODO: запрос на добавление горячей
        await callback.message.answer('warm')
    elif action == 'electr':
        # TODO: запрос на добавление электричества
        await callback.message.answer('electr')

    await callback.answer()