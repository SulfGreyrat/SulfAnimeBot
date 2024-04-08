from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 
from markup import inline_markup as kb

from handlers import anime_send as a

router = Router()

@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery):
    text = callback_query.data
    print(text) 
    
    if text.startswith('viewed'):
        anime_id = text.split("_")
        db.add_to_viewed(anime_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'ADDED TO VIEWED ✅')
        
    if text.startswith('favorite'):
        favorite_id = text.split("_")
        db.add_to_favorite(favorite_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'ADDED TO FAVORITE ❣️')
        
    if text.startswith('delete-favorite'):
        favorite_id = text.split("_")
        db.delete_favorite(favorite_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'DELETED FROM FAVORITE ❣️')
    
    if text.startswith('delete-viewed'):
        anime_id = text.split('_')
        db.delete_viewed(anime_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'DELETED FROM VIEWED ✅')
    
    if text == 'oneoffive_viewed':
        vieweds = db.all_viewed(callback_query.from_user.id)
        for viewed in vieweds[:5]:  
            anime = db.anime_from_id(viewed[1])
            await a.send_anime(anime, callback_query.from_user.id, 'viewed')

    await bot.answer_callback_query(callback_query.id)
    
    if text == 'twooffive_viewed':
        vieweds = db.all_viewed(callback_query.from_user.id)
        for viewed in vieweds[-5:]:  
            anime = db.anime_from_id(viewed[1])
            await a.send_anime(anime, callback_query.from_user.id, 'viewed')
                            
    if text == 'txt_viewed':
        vieweds = db.all_viewed(callback_query.from_user.id)
        
        with open(f'files/{callback_query.from_user.id}_viewed_anime.txt', 'w') as file:
            for viewed in vieweds:
                anime = db.anime_from_id(viewed[1])
                file.write(str(anime[1]) + '\n')
                    
        await bot.send_document(callback_query.from_user.id, document=types.FSInputFile(path=f'files/{callback_query.from_user.id}_viewed_anime.txt'))
    
    await bot.answer_callback_query(callback_query.id)
