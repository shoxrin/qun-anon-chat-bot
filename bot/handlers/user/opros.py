from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from bot.keybords import create_user_kb

def opros_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('.опрос'))
    async def start_opros(message: Message):
        await message.answer(text=message.text, reply_markup=create_user_kb())