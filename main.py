from aiogram import Bot, Dispatcher
from data.database import BotDB

from decouple import config
import multiprocessing
import asyncio
import logging

bot = Bot(token=config('TOKEN'))
dp = Dispatcher()

db = BotDB()

from handlers import all_users, favorites, other_messsage, random_anime, viewed_animes, callback

logging.basicConfig(level=logging.INFO)

                                                                                            
async def main():
    dp.include_routers(all_users.router, favorites.router, other_messsage.router, random_anime.router, viewed_animes.router, callback.router)
    await dp.start_polling(bot) 

if __name__ == '__main__':
    db.create_table()
    asyncio.run(main())