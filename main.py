from aiogram import Bot, Dispatcher
from data.database import BotDB

from decouple import config
import multiprocessing
import asyncio
import logging

from parser. which_anime_will_release import which_anime_will_enter

bot = Bot(token=config('TOKEN'))
dp = Dispatcher()

db = BotDB()

from handlers import all_users, favorites, other_messsage, random_anime, viewed_animes, setting, callback, anime_send

logging.basicConfig(level=logging.INFO)
                                                                                       
async def main():
    dp.include_routers(setting.router, all_users.router, favorites.router, random_anime.router, viewed_animes.router, other_messsage.router, callback.router, anime_send.router)
    await dp.start_polling(bot) 

if __name__ == '__main__':
    which_anime_will_enter()
    db.create_table()
    asyncio.run(main())