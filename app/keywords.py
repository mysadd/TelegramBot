from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Список валют
currencies = {
    "rubble": "RUB",
    "dollar": "USD",
    "euro": "EUR",
    "yen": "JPY",
    "som": "KGS"
}

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
