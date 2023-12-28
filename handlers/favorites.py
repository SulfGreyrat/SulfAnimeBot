from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.message(F.text == '💝 Избранное')
async def favorite(message: Message):
    favorites = db.all_favorite()
    print(favorites)
    if favorites:
        for favorite in favorites:
            caption = f'''✨{favorite[1]}✨\n\n{favorite[4]}\n\n{favorite[3]}\n\n{favorite[5]}\n\n<a href='{favorite[2]}'>Ссылка</a>'''
            await bot.send_photo(message.from_user.id, favorite[6], caption, parse_mode='HTML')
    elif favorites == []:
        img = 'https://avatanplus.com/files/resources/mid/5b9ff52133591165e8d589ba.png'
        caption = 'Нет избранных аниме'
        await bot.send_photo(chat_id=message.from_user.id, photo=img, caption='Нет избранных аниме', parse_mode='HTML')
        