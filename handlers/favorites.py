from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 
from markup import inline_markup as kb

router = Router()

@router.message(F.text == '💝 Избранное')
async def favorite(message: Message):
    favorites = db.all_favorite(message.from_user.id)
    print(favorites)
    for favorite in favorites:
        favorite_anime = db.anime_from_id(favorite[1])
        print(favorite, favorite_anime)
        if favorite:
            keyb = kb.delete_favorite_inlinebutton(favorite_anime[0])
            caption = f'''✨{favorite_anime[1]}✨\n\n{favorite_anime[4]}\n\n{favorite_anime[3]}\n\n<a href='{favorite_anime[2]}'>Ссылка</a>'''
            await bot.send_photo(chat_id=message.from_user.id, photo=favorite_anime[6], caption=caption, parse_mode='HTML', reply_markup=keyb)
        elif favorite == []:
            img = 'https://avatanplus.com/files/resources/mid/5b9ff52133591165e8d589ba.png'
            caption = 'Нет избранных аниме'
            await bot.send_photo(chat_id=message.from_user.id, photo=img, caption='Нет избранных аниме', parse_mode='HTML')
        