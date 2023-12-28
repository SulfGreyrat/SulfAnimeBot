from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.message(F.text == 'Пользователи')
async def all_users(message: Message):
    users = db.get_users()
    
    if users:
        message = "Активные пользователи:\n"
        for user in users:
            message += f"- Имя: {user[0]}, ID: {user[1]}"
    else:
        message = "Нет активных пользователей."
        
    await message.answer(message)
   