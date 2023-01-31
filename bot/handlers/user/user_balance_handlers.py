from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.database.methods import user_methods
from bot.keybords import create_user_balance_kb

def user_balnce_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Баланс'))
    async def show_balance(message: Message):
        user_balance = await user_methods.select_user(message.from_user.id)
        
        await message.answer(text=f'Ваш баланс: {user_balance.user_balance}', reply_markup=create_user_balance_kb())
        
    @dp.callback_query_handler(text='send_money_friend')
    async def send_money(callback: CallbackQuery):
        await callback.answer(text='Отправленно', show_alert=True)
        
    @dp.callback_query_handler(text='get_money_info')
    async def get_money_info(callback: CallbackQuery):
        await callback.message.answer(text='Писать сообщения?')
        await callback.answer(show_alert=False)