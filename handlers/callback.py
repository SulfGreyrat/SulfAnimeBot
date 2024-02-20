from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery):
    text = callback_query.data
    print(text) 
    if text.startswith('delete-favorite'):
        favorite_id = text.split("_")
        db.delete_favorite(favorite_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'DELETED FROM FAVORITE ❣️')
    if text.startswith('favorite'):
        favorite_id = text.split("_")
        db.add_to_favorite(favorite_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'ADDED TO FAVORITE ❣️')
    if text.startswith('delete-viewed'):
        anime_id = text.split('_')
        db.delete_viewed(anime_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'DELETED FROM VIEWED ✅')
    if text.startswith('viewed'):
        anime_id = text.split("_")
        db.add_to_viewed(anime_id[1], callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, 'ADDED TO VIEWED ✅')
        
    await bot.answer_callback_query(callback_query.id)
        