from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from bot.keybords import return_kb
from bot.keybords import create_group_kb

def user_group_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Топ чатов'))
    async def show_top_groups(message: Message):
        await message.answer(text='Выберите фильтр!', reply_markup=create_group_kb())
    
    @dp.callback_query_handler(text='show_top')
    async def show_top(callback: CallbackQuery):
        await callback.message.answer(text='njg', reply_markup=return_kb)