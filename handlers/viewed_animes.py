from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 

router = Router()

@router.message(F.text == '💊 Просмотренные')
async def view(message: Message):
    viewed = db.all_viewed()
    if viewed:
        for view in viewed:
            caption = f'''✨{view[1]}✨\n\n{view[4]}\n\n{view[3]}\n\n{view[5]}\n\n<a href='{view[2]}'>Ссылка</a>'''
            await bot.send_photo(message.from_user.id, view[6], caption, parse_mode='HTML')
    else:
        img = 'https://avatanplus.com/files/resources/mid/5b9ff52133591165e8d589ba.png'
        await bot.send_photo(message.from_user.id, img, caption='Нет просмотренных аниме', parse_mode='HTML')
        