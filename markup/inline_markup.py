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

viewed = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1/5', callback_data='oneoffive_viewed'),
            InlineKeyboardButton(text='2/5', callback_data='twooffive_viewed')
        ],
        [
            InlineKeyboardButton(text='txt', callback_data='txt_viewed')
        ]
    ]
)

genres = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Экшен', callback_data='genre_Экшен'),
            InlineKeyboardButton(text='Фантастика', callback_data='genre_Фантастика'),
            InlineKeyboardButton(text='Драма', callback_data='genre_Драма'),
        ],
        [
            InlineKeyboardButton(text='Романтика', callback_data='genre_Романтика'),
            InlineKeyboardButton(text='Этти', callback_data='genre_Этти'),
            InlineKeyboardButton(text='Военное', callback_data='genre_Военное'),
        ],
        [
            InlineKeyboardButton(text='Комедия', callback_data='genre_Комедия'),
            InlineKeyboardButton(text='Сёнэн', callback_data='genre_Сёнэн'),
            InlineKeyboardButton(text='Школа', callback_data='genre_Школа'),
        ],
        [
            InlineKeyboardButton(text='Приключения', callback_data='genre_Приключения'),
            InlineKeyboardButton(text='Магия', callback_data='genre_Магия'),
            InlineKeyboardButton(text='Демоны', callback_data='genre_Демоны'),
        ],
        [
            InlineKeyboardButton(text='Гарем', callback_data='genre_Гарем'),
            InlineKeyboardButton(text='Детектив', callback_data='genre_Детектив'),
            InlineKeyboardButton(text='Спорт', callback_data='genre_Спорт'),
        ]
    ]
)

dop_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Система рангов', callback_data='rang')
        ],
                [
            InlineKeyboardButton(text='Команды', callback_data='commands'),
            InlineKeyboardButton(text='О проекте', callback_data='about')
            
        ]
    ]
)

settings = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Фильтрация', callback_data='filtr')
        ],
        [
            InlineKeyboardButton(text='Какие аниме выйдут сегодня?', callback_data='which_anime_will_enter')
        ]
    ]
)

donate = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Privacy Policy', url='https://sulfgreyrat.godaddysites.com/privacy-policy'),
            InlineKeyboardButton(text='О проекте', url='https://sulfgreyrat.godaddysites.com/')
        ],
        [
            InlineKeyboardButton(text='Donate', url='https://www.donationalerts.com/r/sulfgreyrat')
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

