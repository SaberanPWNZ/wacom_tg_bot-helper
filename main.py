import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher

from bot.handlers import router
from bot.models import TelegramBot

logger = logging.getLogger('tg')
logger.setLevel(logging.INFO)
bot = Bot(token=TelegramBot.token)
dp = Dispatcher()

dp.include_router(router=router)


async def main():
    try:
        polling_task = asyncio.create_task(dp.start_polling(bot))
        await polling_task

    except Exception as e:
        logger.exception("Error starting bot: %s", e)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
