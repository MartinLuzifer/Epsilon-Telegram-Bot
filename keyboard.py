from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

mainKeys = [
    KeyboardButton(text='/start'),
    KeyboardButton(text='/help')
]

mainKeyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        mainKeys,
        *[]
    ]
)
