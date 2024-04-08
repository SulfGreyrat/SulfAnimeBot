from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import random
from datetime import datetime

from parser import which_anime_will_release
from markup import inline_markup as kb
from main import bot, db 
import handlers
from collections import Counter


router = Router()

def top_genres(vieweds):
    animes = []
    
    word_counts = Counter()
    
    for viewed in vieweds:
        anime = db.anime_from_id(viewed[1])
        animes.append(anime[8])

    for item in animes:
        words = item.split(', ')
        word_counts.update(words)
    
    top_words = word_counts.most_common(3)
    return [word for word, _ in top_words]


def get_rang(num):
    print(num)
    if num < 20:
        return "E"
    if num < 30:
        return "E+"
    if num < 50:
        return "D"
    if num < 80:
        return "D+"
    if num < 100:
        return "C"
    if num < 120:
        return "C+"
    if num < 140:
        return "B"
    if num < 160:
        return "B+"
    if num < 180:
        return "A"
    if num < 200:
        return "A+"
    if num < 220:
        return "Железный ранг"
    if num < 240:
        return "Бронзовый ранг"
    if num < 250:
        return "Серебряный ранг"
    if num < 300:
        return "Золотой ранг"
    if num < 350:
        return "Платиновый ранг"
    if num < 400:
        return "Мифриловый ранг"
    else:
        rank = "E- ранг"
        return rank



@router.callback_query(F.data == 'which_anime_will_enter')
async def which_anime_will_enter(callback: types.CallbackQuery):
    await callback.answer()
    animes = db.todays_anime()
    for anime in animes: 
        await bot.send_message(callback.from_user.id,f"📆{str(anime[0])}")

@router.callback_query(F.data.startswith('genre'))
async def filtr(callback: types.CallbackQuery):
    text = callback.data
    genre = text.split('_')
    print(genre[1])
    genres = db.set_genres(genre[1], callback.from_user.id)
    
    if genres:
        selected = [genre[0] for genre in genres]
        genres = ', '.join(selected)      
    else:
        text = 'Выберите жанры'         
    
    genres = f"Филтр по жанрам: {genres}"   
    try:
        await bot.edit_message_text(message_id = callback.message.message_id, chat_id = callback.message.chat.id, text = genres, reply_markup=kb.genres)
    except:
        await bot.edit_message_text(message_id = callback.message.message_id, chat_id = callback.message.chat.id, text='Нет выбранных жанров', reply_markup=kb.genres)
    await callback.answer()
    
@router.message(Command('filtration'))      
@router.callback_query(F.data == 'filtr')
async def filtr(callback: types.CallbackQuery):
    filtr_genres = db.get_genres(callback.from_user.id)
    genres = ''
    
    if filtr_genres:
        selected = [genre[0] for genre in filtr_genres]
        genres = ', '.join(selected)      
    else:
        text = 'Выберите жанры'         
    
    text = f"Филтр по жанрам: {genres}"
    await bot.send_message(chat_id=callback.from_user.id, text=text, reply_markup=kb.genres)
    await callback.answer()

@router.message(F.text == "⚙️ Настройки")
@router.message(Command('settings'))
async def settings(message: Message):
    #await message.answer('Здесь скоро появится настройка фильтрации и подписка по получения новых серий аниме (онгоингов) для того что бы оставить предложения или запросы используйте: @SulfGreyratDeveloperBot', reply_markup=ikb.genres)
    vieweds = db.all_viewed(message.from_user.id)
    favorites = db.all_favorite(message.from_user.id)
    num_of_vieweds = len(vieweds)
    rang = get_rang(num_of_vieweds)
    num_of_favorites = len(favorites)
    topgenres = top_genres(vieweds)
    genres = '\n         '.join(topgenres)

    filtr_genre = db.get_genres(message.from_user.id)
    
    if filtr_genre:
        selected = [genre[0] for genre in filtr_genre]
        filtr_genres = ' \t\n         \t'.join(selected)      
    else:
        filtr_genres = 'отключена'
    
    if not genres:
        genres = '\nДобавьте аниме которые вы посмотрели для того что бы составить статистику.'
    
    caption = f'🗂ID: {message.from_user.id}\n🫶Имя: {message.from_user.full_name}\n👾Просмотренных аниме: {num_of_vieweds}\n💖Аниме добавленных в избранное: {num_of_favorites}\n📊Ранг: {rang}\n\n🧬Любимые жанры:\n         {genres}\n\n🗄Фильтрация:\n         {filtr_genres}'
    
    user_profile_photo = await bot.get_user_profile_photos(message.from_user.id)
    
    if len(user_profile_photo.photos) > 0:
        await bot.send_photo(chat_id=message.from_user.id, photo=user_profile_photo.photos[0][0].file_id, caption=caption, reply_markup=kb.settings)
    else:
       await bot.send_message(message.from_user.id, caption, reply_markup=kb.settings)