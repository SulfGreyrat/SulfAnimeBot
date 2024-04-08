from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
from main import bot, db 
from markup import inline_markup as kb

from collections import Counter
import matplotlib.pyplot as plt

router = Router()

def top_genres(vieweds, user_id):
    animes = []
    
    for viewed in vieweds:
        anime = db.anime_from_id(viewed[1])
        animes.append(anime[8])
    
    words = [word for line in animes for word in line.split(', ')]
    word_counts = Counter(words)
    top_words = word_counts.most_common(5)
    labels, counts = zip(*top_words)
    
    # Создание диаграммы
    plt.bar(labels, counts, color='#03c2fc')
    plt.ylabel('Частота встречаемых жанров в аниме')
    plt.title('Топ жанров которые вам нравятся')

    # Сохранение диаграммы в файл
    plt.savefig(f'images/{user_id}_viewed.png')

    plt.clf()

@router.message(F.text == '💊 Просмотренные')
@router.message(Command('viewed'))   
async def view(message: Message):

    vieweds = db.all_viewed(message.from_user.id)
    user_id = message.from_user.id
    
    if not vieweds:
        img = 'https://yoast.com/app/uploads/2016/10/404_error_checking_FI.jpg'
        caption = 'Нет просмотренных аниме'
        await bot.send_photo(chat_id=message.from_user.id, photo=img, caption=caption, parse_mode='HTML')
        return
    
    msg = await bot.send_message(message.from_user.id, "Секунду создается диаграмма.....")
    top_genres(vieweds, user_id)
    
    num_of = len(vieweds)

    await bot.send_photo(user_id, photo=types.FSInputFile(
        path=f'images/{user_id}_viewed.png',
    ), caption=f'Статистика\n\nПросмотренных аниме: {num_of}', reply_markup=kb.viewed)
    
    await bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)

    #for viewed in vieweds:  
    #    anime = db.anime_from_id(viewed[1])
    #    print(viewed)
    #    if anime[11] == 'jutsu':
    #                caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>'''
    #                keyboard = kb.delete_viewed_inlinebutton(viewed[1])
    #                try:
    #                    await bot.send_photo(chat_id=message.from_user.id, photo=anime[6], caption=caption, parse_mode='HTML',
    #                                         reply_markup=keyboard)
    #                except Exception as e:
    #                    print(e)

    #    if anime[11] == 'animego':
    #            caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
    #            keyboard = kb.delete_viewed_inlinebutton(viewed[1])
    #            try:
    #                await bot.send_photo(chat_id=message.from_user.id, photo=anime[6], caption=caption, parse_mode='HTML',
    #                                     reply_markup=keyboard)
    #            except Exception as e:
    #                print(e)

    #    if anime[11] == 'multi':
    #            caption = f'''✨{anime[1]}✨\n\nГод выхода: {anime[7]}\nЖанр: {anime[8]}\nОригинальное название: {anime[2]}\nРейтинг: {anime[9]}\n\n{anime[4]}\n\n<a href='{anime[3]}'>Ссылка на Jutsu</a>\n<a href='{anime[10]}'>Ссылка на AnimeGo</a>'''
    #            keyboard = kb.delete_viewed_inlinebutton(viewed[1])
    #            try:
    #                await bot.send_photo(chat_id=message.from_user.id, photo=anime[6], caption=caption, parse_mode='HTML',
    #                                     reply_markup=keyboard)
    #            except Exception as e:
    #                print(e)
