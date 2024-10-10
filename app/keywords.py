from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = 'Рубль', callback_data = "rubble")],
    [KeyboardButton(text = 'Доллар', callback_data = "dollar")],
    [KeyboardButton(text = 'Евро', callback_data = "euro")],
    [KeyboardButton(text = 'Йена', callback_data = "yen")],
    [KeyboardButton(text = 'Сом', callback_data = "som")]], 
    resize_keyboard=True, input_field_placeholder="Выберите валюту для конвертации...")
