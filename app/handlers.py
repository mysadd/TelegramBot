from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keywords as kb
from app.currencies_api import get_exchange_rate  # Импортируем функцию

router = Router()

class Converter(StatesGroup):
    currency_from = State()
    value = State()
    currency_to = State()
    result = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Converter.currency_from)
    await message.answer('Привет! Выберите валюту, из которой хотите конвертировать:', reply_markup=kb.main)

@router.message(Converter.currency_from)
async def converter_currency_from(message: Message, state: FSMContext):
    await state.update_data(currency_from=message.text)
    await state.set_state(Converter.value)
    await message.answer('Введите сумму для конвертации:')

@router.message(Converter.value)
async def converter_value(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    user_data = await state.get_data()
    currency_from = user_data.get('currency_from')
    new_keyboard = kb.create_currency_keyboard(exclude_currency=currency_from)
    await state.set_state(Converter.currency_to)
    await message.answer(f"Вы выбрали {currency_from}. Теперь выберите валюту для конвертации:", reply_markup=new_keyboard)

@router.message(Converter.currency_to)
async def converter_currency_to(message: Message, state: FSMContext):
    await state.update_data(currency_to=message.text)
    user_data = await state.get_data()
    currency_from = user_data.get('currency_from')
    amount = user_data.get('amount')
    currency_to = user_data.get('currency_to')

    # Получаем актуальный курс через API
    rate = get_exchange_rate(currency_from, currency_to)
    
    if isinstance(rate, str):
        await message.answer(f"Ошибка: {rate}")
    else:
        converted_amount = float(amount) * rate
        await state.set_state(Converter.result)
        await message.answer(f"Конвертация {amount} {currency_from} в {currency_to}:\nРезультат: {converted_amount:.2f} {currency_to}.")
    
    await state.clear()
