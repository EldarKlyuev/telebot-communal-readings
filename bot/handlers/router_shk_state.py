from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.enums import ParseMode

router = Router()


class Form(StatesGroup):
    cold_bath = State()
    warm_bath = State()
    cold_kich = State()
    warm_kich = State()
    electr = State()


@router.callback_query(F.data == 'post_shk_all')
async def process_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Form.cold_bath)
    await callback.message.answer("Введите показания холодной в ванной:")


@router.message(StateFilter(Form.cold_bath))
async def process_cold_bath(message: types.Message, state: FSMContext):
    await state.update_data(cold_bath=message.text)
    await state.set_state(Form.warm_bath)
    await message.answer("Введите показания горячей в ванной:")


@router.message(StateFilter(Form.warm_bath))
async def process_warm_bath(message: types.Message, state: FSMContext):
    await state.update_data(warm_bath=message.text)
    await state.set_state(Form.cold_kich)
    await message.answer("Введите показания холодной на кухне:")


@router.message(StateFilter(Form.cold_kich))
async def process_cold_kich(message: types.Message, state: FSMContext):
    await state.update_data(cold_kich=message.text)
    await state.set_state(Form.warm_kich)
    await message.answer("Введите показания горячей на кухне:")


@router.message(StateFilter(Form.warm_kich))
async def process_warm_kich(message: types.Message, state: FSMContext):
    await state.update_data(warm_kich=message.text)
    await state.set_state(Form.electr)
    await message.answer("Введите показания электричества:")


@router.message(StateFilter(Form.electr))
async def process_electr(message: types.Message, state: FSMContext):
    await state.update_data(electr=message.text)

    user_data = await state.get_data()
    await message.answer(f"""Полные ваши показания:\n\nХолодная в ванной: {user_data['cold_bath']}\nГорячая в ванной: {user_data['warm_bath']}\nХолодная на кухне: {user_data['cold_kich']}\nГорячая на кухне: {user_data['warm_kich']}\nЭлетричество: {user_data['electr']}""",
                         parse_mode=ParseMode.MARKDOWN)
    
    # TODO: запрос на поные данные для шк
    await state.clear()