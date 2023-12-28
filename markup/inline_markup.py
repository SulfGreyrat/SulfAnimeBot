from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup 
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='💖', callback_data='favorite'),
            InlineKeyboardButton(text='✅', callback_data='viewed')
        ]
    ]
)