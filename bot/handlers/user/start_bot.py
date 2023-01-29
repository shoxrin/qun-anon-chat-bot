from aiogram import Dispatcher
from aiogram.types import Message

from bot.keybords import create_user_kb

hello_message = '''Привет!
Что умеет этот бот?
Ничего, пшел нахуй еблан!!!'''

def start_bot_handler(dp: Dispatcher) -> None:
    
    @dp.message_handler(commands=['start'])
    async def hello_user(message: Message):
        await message.answer(text=hello_message, reply_markup=create_user_kb())