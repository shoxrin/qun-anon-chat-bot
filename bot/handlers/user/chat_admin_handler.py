from aiogram import Dispatcher, Bot
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, Message

def chat_admin_handlers(dp: Dispatcher, b: Bot):#, chatAdminMenu: ReplyKeyboardMarkup, inlineChatAdminMenu: InlineKeyboardMarkup):
    
    @dp.message_handler(commands=['start'])
    async def start_use(message: Message):
        if message.chat.id > 0:
            await message.answer(text='Привет')