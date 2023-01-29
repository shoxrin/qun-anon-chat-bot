from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

def opros_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('.опрос'))
    async def start_opros(message: Message):
        for word in message.text.strip(' '):
            await message.answer(text=word)