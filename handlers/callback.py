from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.callback_query()
async def callback_query_handler(callback_query: types.CallbackQuery):
    text = callback_query.data
    if 'favorite' in text:
        await bot.send_message(callback_query.from_user.id, 'FAVORITE ❣️')
    elif 'viewed' in text:
        await bot.send_message(callback_query.from_user.id, 'VIEWED ✅')
    await bot.answer_callback_query(callback_query.id)
        