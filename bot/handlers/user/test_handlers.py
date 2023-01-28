from aiogram import Dispatcher
from aiogram.types import Message

def test_handlers(dp: Dispatcher):
    
    @dp.message_handler()
    async def echo(message: Message):
        await message.answer(text=message.text)