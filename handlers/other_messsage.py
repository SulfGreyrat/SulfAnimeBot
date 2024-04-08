from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from main import bot, db 
from parser import parsing
from markup import reply_markup as kb
from markup import inline_markup as ikb
import logging
import asyncio
import random
from handlers import anime_send

router = Router()

def search(search_arr):
    animes = db.all_anime()
    main_array = [tup[1] for tup in animes]    

    # Преобразование строки в список слов
    check_words = search_arr.split()
    print(check_words)

    # Получение массивов, в которых присутствуют все слова из второго массива
    matching_arrays = [item for item in main_array if all(word in item for word in check_words)]    

    if matching_arrays:
        result = []
        for array in matching_arrays:
            result.extend([tup for tup in animes if tup[1] == array])
        # Исключение повторяющихся кортежей
        unique_result = list(set(result))
        return unique_result
    else:
        return []


@router.message(Command('newslatter'))
async def update(message: Message):
    user_id = message.from_user.id
    is_admin = db.is_admin(user_id)
    if is_admin:
        users = db.get_users()

        msg = message.text
        text = msg.replace('/newslatter', '')
        
        for user in users:
            try:
                await bot.send_message(user[1], text)
            except:
                await bot.send_message(user_id, f'Ошибка при отпрвления: {user[2]}')
                
        await message.answer('🔄 Отправка....')

@router.message(CommandStart())
async def start_cmd(message: Message):
    user_full_name = message.from_user.full_name
    user_id = message.from_user.id
    is_admin = db.is_admin(user_id)
    
    if is_admin:
        await message.answer(f"Добро пожаловать! {user_full_name}", reply_markup=kb.main_admin)
    else:
        photo = 'https://i.pinimg.com/originals/e2/c7/61/e2c7615dbc25056e057f49fb37d19752.jpg'
        caption = 'Добро пожаловать в @SulfAnimeBot\n\n🌟 Используйте команду /help  для того что бы ознакомиться с имеющимися командой а также 📊Системой рангов\n\n💫 Рандом - Для того что бы бот отправил вам аниме карточку с аниме которым вы не смотрели. Жанры который будут присутствовать в аниме можно настроить с помощью команды /filtration\n\n💊 Просмотренные - Команда создает диаграмму на основе просмотренных аниме которые вы отметили. Также вы можете получить 1/5 - первые 5 просмотренных аниме 2/5 - последние 5 аниме txt - для того что бы получить список всех просмотренных аниме в одном текстовом файле\n\n💝 Избранное - Это команда используется для того что бы получить все аниме храняшимися у вас в Избранном\n\n⚙️ Настройки - Позволяет вам настроить жанры аниме а также отправляет список аниме которые выйдут сегодня.\n\n🌟 Если у вас возникли пожелания или запросы, просто отправьте сообщение волшебному боту по ссылке: @SulfGreyratDeveloperBot.\n\nРазработчик: @SulfGreyratDeveloper'
        
        await message.answer(f"Добро пожаловать! {user_full_name}", reply_markup=kb.main)
        await bot.send_photo(user_id, photo=photo, caption=caption, reply_markup=ikb.dop_info)
        
    db.new_user(user_id, user_full_name)

@router.message(F.text == "🔄 Обновить")
@router.message(Command('update'))
async def update(message: Message):
    users = db.get_users()
    
    for user in users:
        try:
            await bot.send_message(user[1],"🔧 Начали техработы для улучшения нашего бота. Возможны кратковременные сбои, но мы уже работаем над минимизацией. 💼 Приносим извинения за временные неудобства! \n\nЕсли есть вопросы или проблемы, дайте знать. 🚀 Спасибо за терпение! 🙏")
        except Exception as e:
            logging.error('EROR WHILE SEND INFO')
            
    await message.answer('🔄 Обновление....')
    
    await parsing.main()
    await parsing.anime_go()
    
#@router.message(F.text == "⚙️ Настройки")
#@router.message(Command('settings'))
#async def settings(message: Message):
#        
#    await message.answer('Здесь скоро появится настройка фильтрации и подписка по получения новых серий аниме (онгоингов) для того что бы оставить предложения или запросы используйте: @SulfGreyratDeveloperBot', reply_markup=ikb.genres)
#    

@router.message(Command('delete_null'))
async def update(message: Message):
    users = db.get_users()
    
    for user in users:
        await bot.send_message(user[1],"🔧 Начали техработы для улучшения нашего бота. Возможны кратковременные сбои, но мы уже работаем над минимизацией. 💼 Приносим извинения за временные неудобства! \n\nЕсли есть вопросы или проблемы, дайте знать. 🚀 Спасибо за терпение! 🙏")
    
    await message.answer('🔄 Обновление....')
    db.delete_null()
    
@router.message(Command('help'))
async def help(message: Message):
    photo = 'https://www.forbesindia.com/media/images/2023/May/img_207055_animebg.jpg'
    caption = 'Добро пожаловать в @SulfGreyrat_Bot\n\nЕсли у вас возникли пожелания или запросы, просто отправьте сообщение боту по ссылке: @SulfGreyratDeveloperBot.'
    
    await message.answer_photo(photo=photo, caption=caption, reply_markup=ikb.dop_info)

@router.message(Command('admin_panel_sulf_4985_greyrat'))
async def admin(message: Message):
    user_id = message.from_user.id
    name = message.from_user.full_name
    db.new_admin(name, user_id)
    
@router.callback_query(F.data == 'commands')
async def commands(call: types.CallbackQuery):
    photo = 'https://www.goha.ru/s/f/Co/tN/7sAIdtbxDA.jpg'
    caption = '💫 Рандом - Для того что бы бот отправил вам аниме карточку с аниме которым вы не смотрели. Жанры который будут присутствовать в аниме можно настроить с помощью команды /filtration\n\n💊 Просмотренные - Команда создает диаграмму на основе просмотренных аниме которые вы отметили. Также вы можете получить 1/5 - первые 5 просмотренных аниме 2/5 - последние 5 аниме txt - для того что бы получить список всех просмотренных аниме в одном текстовом файле\n\n💝 Избранное - Это команда используется для того что бы получить все аниме храняшимися у вас в Избранном\n\n⚙️ Настройки - Позволяет вам настроить жанры аниме а также отправляет список аниме которые выйдут сегодня.\n\n🔎Для того что бы использовать поиск аниме по названию просто впишите название аниме которое в хотите найти.'
    
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=caption)
    await call.answer()
    
@router.callback_query(F.data == 'rang')
async def commands(call: types.CallbackQuery):
    photo = 'https://pw.artfile.me/wallpaper/13-06-2017/650x366/anime-no-game-no-life-personazhi-1178599.jpg'
    caption = "Команда показывает ваш ранг, основанный на количестве просмотренных аниме. Вот как работает система ранжирования:\n\n" \
                   "⭐️До 20 просмотренных аниме: ранг 'E'\n" \
                   "⭐️20-30 просмотренных аниме: ранг 'E+'\n" \
                   "⭐️30-50 просмотренных аниме: ранг 'D'\n" \
                   "⭐️50-80 просмотренных аниме: ранг 'D+'\n" \
                   "⭐️80-100 просмотренных аниме: ранг 'C'\n" \
                   "⭐️100-120 просмотренных аниме: ранг 'C+'\n" \
                   "⭐️120-140 просмотренных аниме: ранг 'B'\n" \
                   "⭐️140-160 просмотренных аниме: ранг 'B+'\n" \
                   "⭐️160-180 просмотренных аниме: ранг 'A'\n" \
                   "⭐️180-200 просмотренных аниме: ранг 'A+'\n" \
                   "⭐️200-220 просмотренных аниме: ранг 'Железный ранг'\n" \
                   "⭐️220-240 просмотренных аниме: ранг 'Бронзовый ранг'\n" \
                   "⭐️240-250 просмотренных аниме: ранг 'Серебряный ранг'\n" \
                   "⭐️250-300 просмотренных аниме: ранг 'Золотой ранг'\n" \
                   "⭐️300-350 просмотренных аниме: ранг 'Платиновый ранг'\n" \
                   "⭐️Более 350 просмотренных аниме: ранг 'Мифриловый ранг'"
        
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=caption)
    await call.answer()
    
@router.callback_query(F.data == 'about')
async def about(call: types.CallbackQuery):
    photo = 'https://abrakadabra.fun/uploads/posts/2022-02/1645999613_2-abrakadabra-fun-p-oboi-na-pk-estetichnie-anime-2.jpg'
    caption = 'дай денег'
        
    await bot.send_photo(chat_id=call.from_user.id, photo=photo, caption=caption)
    
    
    
@router.message()
async def messages(message: Message):
    user_id = message.from_user.id
    msg = message.text
    try:
        animes_result = search(msg)
        if len(animes_result) > 0:
            await message.answer(f'найдено {len(animes_result)} аниме')
            try:
                while True:
                    try:
                        anime = random.choice(animes_result)
                        await anime_send.send_anime(anime, user_id, 'usually')
                        break
                    except Exception as e:
                        print(e)
            except Exception as e:
                await message.answer(f'Аниме с таким названием не найдено')
        else:
            await message.answer(f'Аниме с таким названием не найдено')
            
    except Exception as e:
        await message.answer('Произошла ошибка повторите запрос.') 