from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
# Список валют
currencies = {
    "rubble": "RUB",
    "dollar": "USD",
    "euro": "EUR",
    "yen": "JPY",
    "som": "KGS"
}
"""
# Основная клавиатура для выбора первой валюты
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="RUB")],
        [KeyboardButton(text="USD")],
        [KeyboardButton(text="EUR")],
        [KeyboardButton(text="JPY")],
        [KeyboardButton(text="KGS")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите валюту для конвертации..."
)

# Функция для создания клавиатуры с исключением выбранной валюты
def create_currency_keyboard(exclude_currency=None):
    keyboard = []
    
    for key, value in currencies.items():
        if value != exclude_currency:
            keyboard.append([KeyboardButton(text=value)])
    
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите валюту для конвертации..."
    )
"""
mains = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="RUB", callback_data="RUB")],
    [InlineKeyboardButton(text="USD", callback_data="USD")],
    [InlineKeyboardButton(text="EUR", callback_data="EUR")],
    [InlineKeyboardButton(text="JPY", callback_data="JPY")],
    [InlineKeyboardButton(text="KGS", callback_data="KGS")]])

def create_currency_Inlinekeyboard(exclude_currency=None):
    inline_keyboard = []
    
    for key, value in currencies.items():
        if value != exclude_currency:
            inline_keyboard.append([InlineKeyboardButton(text=value, callback_data=value)])
    
    return InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )