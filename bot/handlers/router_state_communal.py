from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode

router = Router()


class Form(StatesGroup):
    cold = State()
    warm = State()
    electric = State()


@router.callback_query(F.data == 'post_shk')
async def process_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.cold)
    await callback.message.answer("Введите показания холодной:")


@router.message(StateFilter(Form.cold))
async def process_cold(message: types.Message, state: FSMContext):
    await state.update_data(cold=message.text)
    await state.set_state(Form.warm)
    await message.answer("Введите показания горячей:")


@router.message(StateFilter(Form.warm))
async def process_warm(message: types.Message, state: FSMContext):
    await state.update_data(warm=message.text)
    await state.set_state(Form.electric)
    await message.answer("Введите показания электричества:")


@router.message(StateFilter(Form.electric))
async def process_electric(message: types.Message, state: FSMContext):
    await state.update_data(electric=message.text)

    user_data = await state.get_data()
    await message.answer(f"Полные ваши показания:\nХолодная: {user_data['cold']}\nГорячая: {user_data['warm']}\nЭлетричество: {user_data['electric']}", parse_mode=ParseMode.MARKDOWN)
    
    # Тут обращение к app
    await state.clear()