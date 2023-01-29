from gino import Gino
from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# bot.filters import register_all_filtres
from bot.misc import TgKeys, DBConfig
from bot.handlers import register_all_handlers
from bot.database.models import register_models


async def __on_start_up(dp: Dispatcher) -> None:
    db = Gino()
    await db.set_bind(DBConfig.postgres_url)
    #register_all_filtres(dp)
    register_all_handlers(dp)
    register_models()

def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)