from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 
from markup import inline_markup as kb

import handlers

router = Router()
        
@router.message(F.text == '💝 Избранное')
@router.message(Command('favorite'))   
async def favorite(message: Message):
    favorites = db.all_favorite(message.from_user.id)
    
    if not favorites:
        img = 'https://w3-lab.com/wp-content/uploads/2022/09/FOR-WEB-404-astronaut.jpg'
        caption = 'Нет избранных аниме'
        await bot.send_photo(chat_id=message.from_user.id, photo=img, caption=caption, parse_mode='HTML')
        
    for viewed in favorites:  
        anime = db.anime_from_id(viewed[1])
        print(viewed)
        await handlers.anime_send.send_anime(anime, message.from_user.id, 'favorite')