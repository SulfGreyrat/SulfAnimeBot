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

def inlinebutton(id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='💖', callback_data=f'favorite_{id}'),
            InlineKeyboardButton(text='✅', callback_data=f'viewed_{id}')
            ]
        ]
    )
    
    return kb

def delete_favorite_inlinebutton(id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='❌', callback_data=f'delete-favorite_{id}')
            ]
        ]
    )
    
    return kb

def delete_viewed_inlinebutton(id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='❌', callback_data=f'delete-viewed_{id}')
            ]
        ]
    )
    
    return kb