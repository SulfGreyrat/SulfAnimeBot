from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.message(F.text == 'Пользователи')
async def all_users(message: Message):
    users = db.get_users()
    
    response_message = ''  
    
    if users:
        response_message = "Активные пользователи:\n"
        for user in users:
            response_message += f"- Имя: {user[2]}, ID: {user[1]}\n"
    else:
        response_message = "Нет активных пользователей."
    
    print(response_message)
    await message.answer(f"{response_message}")

   