from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from main import bot, db 
from parser import parsing
from markup import reply_markup as kb

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    await message.answer(f"Добро пожаловать! {user_full_name}", reply_markup=kb.main)
    db.new_user(user_id, user_full_name)

@router.message(F.text == "🔄 Обновить")
@router.message(Command('update'))
async def update(message: Message):
    users = db.get_users()
    
    for user in users:
        await bot.send_message(user[1],"🔧 Начали техработы для улучшения нашего бота. Возможны кратковременные сбои, но мы уже работаем над минимизацией. 💼 Приносим извинения за временные неудобства! \n\nЕсли есть вопросы или проблемы, дайте знать. 🚀 Спасибо за терпение! 🙏")
    
    await message.answer('🔄 Обновление....')
    db.delete_null()
    await parsing.main()

@router.message(Command('delete_null'))
async def update(message: Message):
    users = db.get_users()
    
    for user in users:
        await bot.send_message(user[1],"🔧 Начали техработы для улучшения нашего бота. Возможны кратковременные сбои, но мы уже работаем над минимизацией. 💼 Приносим извинения за временные неудобства! \n\nЕсли есть вопросы или проблемы, дайте знать. 🚀 Спасибо за терпение! 🙏")
    
    await message.answer('🔄 Обновление....')
    db.delete_null()