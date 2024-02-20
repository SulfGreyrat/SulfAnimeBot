from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 
from markup import inline_markup as kb

router = Router()

@router.message(F.text == '💊 Просмотренные')
async def view(message: Message):
    vieweds = db.all_viewed(message.from_user.id)
    for viewed in vieweds:
        viewed_anime = db.anime_from_id(viewed[1])
        print(viewed, viewed_anime)
        if viewed:
            keyb = kb.delete_viewed_inlinebutton(viewed_anime[0])
            caption = f'''✨{viewed_anime[1]}✨\n\n{viewed_anime[4]}\n\n{viewed_anime[3]}\n\n<a href='{viewed_anime[2]}'>Ссылка</a>'''
            await bot.send_photo(chat_id=message.from_user.id, photo=viewed_anime[6], caption=caption, parse_mode='HTML', reply_markup=keyb)
        elif viewed == []:
            img = 'https://avatanplus.com/files/resources/mid/5b9ff52133591165e8d589ba.png'
            caption = 'Нет просмотренных аниме'
            await bot.send_photo(chat_id=message.from_user.id, photo=img, caption='Нет избранных аниме', parse_mode='HTML')
        