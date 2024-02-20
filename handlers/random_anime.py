from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
import random

from markup import inline_markup as kb
from main import bot, db 

router = Router()

@router.message(F.text == '💫 Рандом')
async def random_anime(message: Message):
    animes = db.all_anime()
    anime = random.choice(animes)
    viewed = db.is_viewed(anime[0], message.from_user.id)
    if not viewed:
        caption = f'''✨{anime[1]}✨\n\n{anime[4]}\n\n{anime[3]}\n\n<a href='{anime[2]}'>Ссылка</a>'''
        keyboard = kb.inlinebutton(anime[0])
        try:
            await bot.send_message(message.from_user.id, anime[5])
            await bot.send_photo(chat_id=message.from_user.id, photo=anime[6], caption=caption, parse_mode='HTML',
                                 reply_markup=keyboard)
        except Exception as e:
            print(e)