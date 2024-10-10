from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import app.keywords as kb
from app.currencies_api import get_exchange_rate  # Импортируем функцию

router = Router()

# Валюты, которые можно использовать
valid_currencies = {"RUB", "USD", "EUR", "JPY", "KGS"}

class Converter(StatesGroup):
    currency_from = State()
    value = State()
    currency_to = State()
    result = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(Converter.currency_from)
    await message.answer('Привет! Выберите валюту, из которой хотите конвертировать:', reply_markup=kb.mains)

@router.callback_query(Converter.currency_from)
async def converter_currency_from(callback: CallbackQuery, state: FSMContext):
    currency_from = callback.data.upper()

    # Проверяем, что валюта введена корректно
    if currency_from not in valid_currencies:
        await callback.message.answer('Ошибка: Введите корректную валюту. Доступные валюты: RUB, USD, EUR, JPY, KGS.')
        return

    await state.update_data(currency_from=currency_from)
    await state.set_state(Converter.value)
    await callback.answer(f'Вы выбрали {currency_from}', show_alert=True)
    await callback.message.answer('Введите сумму для конвертации:')

@router.message(Converter.value)
async def converter_value(message: Message, state: FSMContext):
    try:
        amount = float(message.text)

        if amount <= 0:
            raise ValueError  # Если введено отрицательное число или 0

    except ValueError:
        await message.answer('Ошибка: Введите корректное положительное число для суммы.')
        return

    await state.update_data(amount=amount)
    user_data = await state.get_data()
    currency_from = user_data.get('currency_from')

    # Создаем клавиатуру с исключением выбранной валюты
    new_inline_keyboard = kb.create_currency_Inlinekeyboard(exclude_currency=currency_from)
    await state.set_state(Converter.currency_to)
    await message.answer(f"Вы выбрали {currency_from}. Теперь выберите валюту для конвертации:", reply_markup=new_inline_keyboard)

@router.callback_query(Converter.currency_to)
async def converter_currency_to(callback: CallbackQuery, state: FSMContext):
    currency_to = callback.data.upper()

    user_data = await state.get_data()
    currency_from = user_data.get('currency_from')

    # Проверяем, что валюта введена корректно
    if currency_to not in valid_currencies:
        await callback.answer('Ошибка: Введите корректную валюту. Доступные валюты: RUB, USD, EUR, JPY, KGS.', show_alert=True)
        return

    # Проверка на одинаковые валюты
    if currency_from == currency_to:
        await callback.answer('Ошибка: Вы не можете конвертировать одну валюту в ту же самую. Пожалуйста, выберите другую валюту.', show_alert=True)
        return

    amount = user_data.get('amount')

    # Проверяем, что сумма введена корректно
    if not isinstance(amount, (int, float)) or amount <= 0:
        await callback.answer('Ошибка: Некорректная сумма. Пожалуйста, введите положительное число.', show_alert=True)
        return

    # Получаем актуальный курс через API
    rate = get_exchange_rate(currency_from, currency_to)

    if isinstance(rate, str):
        await callback.answer(f"Ошибка: {rate}", show_alert=True)
    else:
        converted_amount = float(amount) * rate
        await state.set_state(Converter.result)
        await callback.answer(f'Ответ получен')
        await callback.message.answer(f"Конвертация {amount} {currency_from} в {currency_to}:\nРезультат: {converted_amount:.2f} {currency_to}.")

    await state.clear()
