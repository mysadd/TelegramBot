from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keywords as kb

router = Router()

class Converter(StatesGroup):
    currency = State()
    value = State()
    convert = State()





@router.message(CommandStart())
async def cmd_start(message: Message):
    await state.set_state(Converter.currency)
    await message.answer('Привет! Вы обратились к боту по конвертации валюты.', reply_markup=main)

@router.message(Converter.currency)
async def Converter_currency(message: Message):
    await state.set_state(Converter.value)
    await message.answer('Введите сумму:')
    
@router.message(Converter.value)
async def Converter_value(message: Message):
    await state.set_state(Converter.convert)
    await message.answer('Выберите валюту', reply_markup="")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('')


@router.message(F.text('asd'))
async def cmd_nice(message: Message):
    await message.answer('Рад слышать')

