import asyncio
import logging
import sys

from decouple import config
from aiogram import Bot, Dispatcher, html
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from commands import setup_bot_command

TOKEN = config('BOT_TOKEN')
storage = MemoryStorage()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


async def main() -> None:
    dp = Dispatcher(storage=storage)

    # Можно ещё добавлять роутеры
    from handlers import (
        routers_index,
        router_callback,
        router_zip_state,
        router_zip_callback,
    )

    dp.include_router(routers_index.router)
    dp.include_router(router_callback.router)
    dp.include_router(router_zip_state.router)
    dp.include_router(router_zip_callback.router)

    await setup_bot_command(bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())