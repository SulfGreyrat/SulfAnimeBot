from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton 
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💫 Рандом")
        ],
        [
            KeyboardButton(text="💊 Просмотренные"),
            KeyboardButton(text="💝 Избранное")
        ],
        [
            KeyboardButton(text="🔄 Обновить")
        ]
    ],
    resize_keyboard=True
)