from gino import Gino
from aiogram.utils import executor
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# bot.filters import register_all_filtres
from bot.misc import settings
from bot.handlers import register_all_handlers
from bot.database import db
from bot.database.models import register_models
from bot.database import on_startup


async def __on_start_up(dp: Dispatcher) -> None:
    await on_startup()
    register_models()
    #register_all_filtres(dp)
    register_all_handlers(dp)
    
def start_bot():
    bot = Bot(token=settings.TGTOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)