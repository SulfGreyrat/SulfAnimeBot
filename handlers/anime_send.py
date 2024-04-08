from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import random
from datetime import datetime

from markup import inline_markup as kb
from main import bot, db 
from handlers.random_anime import send_anime_random

router = Router()

async def send_anime(anime, user_id, mode='usually'):
    print(f"Fybvt {anime}")
    viewed = db.is_viewed(anime[0], user_id)
    if mode == 'viewed':
        if viewed:
            if anime[11] == 'jutsu':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>'''
                keyboard = kb.delete_viewed_inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)

            if anime[11] == 'animego':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
                keyboard = kb.delete_viewed_inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)

            if anime[11] == 'multi':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
                keyboard = kb.delete_viewed_inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)
        else:
            await send_anime_random(user_id)
            
    if mode == 'usually':
        if not viewed:
            if anime[11] == 'jutsu':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>'''
                keyboard = kb.inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)

            if anime[11] == 'animego':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
                keyboard = kb.inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)

            if anime[11] == 'multi':
                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
                keyboard = kb.inlinebutton(anime[0])
                try:
                    await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                         reply_markup=keyboard)
                except Exception as e:
                    print(e)
        else:
            await send_anime_random(user_id)
    
    if mode == 'favorite':
        if anime[11] == 'jutsu':
            caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>'''
            keyboard = kb.delete_favorite_inlinebutton(anime[0])
            try:
                await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                     reply_markup=keyboard)
            except Exception as e:
                print(e)        
        if anime[11] == 'animego':
            caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
            keyboard = kb.delete_favorite_inlinebutton(anime[0])
            try:
                await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                     reply_markup=keyboard)
            except Exception as e:
                print(e)        
        if anime[11] == 'multi':
            caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
            keyboard = kb.delete_favorite_inlinebutton(anime[0])
            try:
                await bot.send_photo(chat_id=user_id, photo=anime[6], caption=caption, parse_mode='HTML',
                                     reply_markup=keyboard)
            except Exception as e:
                print(e)