import sys
import asyncio
import logging
#####################################################################################################################
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.mongo import MongoStorage
from aiogram.enums import ParseMode
from router import mainRouter
from config import TELEGRAM_BOT_API_KEY, MONGODB_URL
#####################################################################################################################


async def main() -> None:
    bot = Bot(token=TELEGRAM_BOT_API_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    mongodb = MongoStorage.from_url(url=MONGODB_URL)
    dp = Dispatcher(storage=mongodb)
    dp.include_router(router=mainRouter)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())