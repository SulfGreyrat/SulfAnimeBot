from aiogram import Bot, types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging
import random
import asyncio

API_TOKEN = '6815961874:AAET9Bjt62gAtlLpk4idkbHfkXilLXfdAZE'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    await message.answer("Выберите кнопку:", reply_markup=main_keyboard)

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Экшен', callback_data='button_action'),
            InlineKeyboardButton(text='Приключение', callback_data='button_adventure'),
            InlineKeyboardButton(text='Этти', callback_data='button_etti')
        ],
        [
            InlineKeyboardButton(text='Драма', callback_data='button_drama'),
            InlineKeyboardButton(text='Комедия', callback_data='button_comedy'),
            InlineKeyboardButton(text='Романтика', callback_data='button_roman')
        ],
        [
            InlineKeyboardButton(text='Гарем', callback_data='button_harem'),
            InlineKeyboardButton(text='Школа', callback_data='button_school'),
            InlineKeyboardButton(text='Военное', callback_data='button_war')
        ]
    ]
)

# Определение состояний
CHOOSING, TYPING_REPLY = range(2)

# Обработчик команды /start
@dp.message(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    await message.reply(f"Привет, {user.first_name}! Выбери жанр книги:", reply_markup=main_keyboard)
    await CHOOSING

# Обработчик inline клавиатуры
@dp.callback_query(lambda c: c.data.startswith('button_'))
async def inline_button_callback(callback_query: types.CallbackQuery):
    user_choice = callback_query.data
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,
                                text=f"Вы выбрали: {user_choice}")
    await TYPING_REPLY

# Обработчик ввода текста
@dp.message(lambda message: message.text and not message.text.startswith('/'), state=CHOOSING)
async def received_reply(message: types.Message):
    user = message.from_user
    user_reply = message.text
    await message.reply(f"Спасибо, {user.first_name}! Вы выбрали {user_choice} и ввели: {user_reply}")
    await ConversationHandler.END

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


