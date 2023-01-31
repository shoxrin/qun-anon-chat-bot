from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.keybords import create_find_partner
from bot.misc import get_random_anonim_userid
from bot.database.methods import user_methods as methods_db


def find_partner_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Найти собеседника'))
    async def find_chat(message: Message):
        await message.answer(text='Выберите как искать собеседника', reply_markup=create_find_partner())
        
    @dp.callback_query_handler(text='find_anonim_chat')
    async def find_anonim_chat(callback: CallbackQuery):
        await methods_db.update_status_anonim(callback.from_user.id, True)
        await callback.message.answer(text='Идет поиск! Подождите немного.')
        
        users = await methods_db.get_user_id_anonim()
        user_id = get_random_anonim_userid(users).user_id     
        if user_id != callback.from_user.id:
            await callback.message.answer(text=f'Собеседник найден!')
        else:
            await callback.message.answer(text=f'На данный момент собеседников нет!')
            
        await callback.answer(show_alert=False)
        
    #@dp.callback_query_handler(text='find_anonim')
    #async def find_anonim(callback: CallbackQuery):
    #    await callback.message.answer(text='Идет поиск! Подождите немного.')
    #    await callback.answer(show_alert=False)