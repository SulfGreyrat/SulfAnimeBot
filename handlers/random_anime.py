from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import random
from datetime import datetime

from markup import inline_markup as kb
from main import bot, db 
import handlers

router = Router()
todays_user = []

def check_array_in_array(arr, search_arr):
    main_array = [tup[8] for tup in arr]    

    # Преобразование кортежей в список строк
    check_words = [word[0] for word in search_arr] 

    # Получение массивов, в которых присутствуют все слова из второго массива
    matching_arrays = [item for item in main_array if all(word in item for word in check_words)]    

    if matching_arrays:
        result = []
        for array in matching_arrays:
            result.extend([tup for tup in arr if tup[8] == array])
        # Исключение повторяющихся кортежей
        unique_result = list(set(result))
        return unique_result
    else:
        return

async def send_anime_random(user_id):
    genres = db.get_genres(user_id)
    animes = db.all_anime()
    
    if not genres:
        anime = random.choice(animes)
        await handlers.anime_send.send_anime(anime, user_id)
    else:
        result = check_array_in_array(animes, genres)
        
        if result:
            anime = random.choice(result)
            await handlers.anime_send.send_anime(anime, user_id)
        else:
            await bot.send_message(user_id, "Нет аниме, в которых присутствуют все жанры из выбранных вами.")
            
@router.message(F.text == '💫 Рандом')
@router.message(Command('random'))   
async def random_anime(message: Message):
    print(message.from_user.full_name)
    user_id = message.from_user.id
    
    await send_anime_random(user_id)
           
    if not message.from_user.id in todays_user:
        await bot.send_message("-1002127891707", f'<a href="tg://openmessage?user_id={message.from_user.id}">{message.from_user.full_name}</a>\n{datetime.now().strftime("%H:%M:%S")}\n---------------\n{datetime.now().strftime("%Y-%m-%d")}', parse_mode='HTML')
        todays_user.append(message.from_user.id)

    #db.new_user(user_id, message.from_user.full_name)
            
        
    