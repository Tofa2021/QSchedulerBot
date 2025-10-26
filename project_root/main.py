import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers import main_menu, queues, options
from project_root.database import init_db

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(main_menu.router)
dp.include_router(queues.router)
dp.include_router(options.router)

async def main():
    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
