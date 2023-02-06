from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from bot.keybords import create_group_kb


def user_group_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Топ чатов'))
    async def show_top_groups(message: Message):
        await message.answer(text='Выберите фильтр!', reply_markup=create_group_kb())
    
    @dp.callback_query_handler(text='find_top_fifteen')
    async def find_top_fifteen(callback: CallbackQuery):
        await callback.message.answer(text='njg')
        await callback.answer(show_alert=False)
        
    @dp.callback_query_handler(text='find_top_on_leskod')
    async def find_top_on_leskod(callback: CallbackQuery):
        await callback.message.answer(text='njg')
        await callback.answer(show_alert=False)
        
    @dp.callback_query_handler(text='find_top_active_users')
    async def find_top_active_users(callback: CallbackQuery):
        await callback.message.answer(text='njg')
        await callback.answer(show_alert=False)