from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.keybords import create_find_partner
from bot.keybords import create_join_partner
from bot.keybords import create_conn_anon_chat
from bot.misc import get_random_anonim_userid
from bot.database.methods import user_methods as methods_db
from bot.database.methods import user_anonim_chat_methods as anonimchat_commands


def find_partner_handlers(dp: Dispatcher, b: Bot):
    
    @dp.message_handler(Text('Найти собеседника'))
    async def find_chat(message: Message):
        await message.answer(text='Выберите удобный для себя вариант!', reply_markup=create_find_partner())

    @dp.callback_query_handler(text='find_anonim_chat')
    async def find_anonim_chat(callback: CallbackQuery):
        await methods_db.update_status_anonim(callback.from_user.id, True)
        await callback.message.answer(text='Идет поиск! Подождите немного.')
        
        chats_id = await anonimchat_commands.find_anon_chat()
        chat_id = get_random_anonim_userid(chats_id)
        
        if chat_id[1]:
            await anonimchat_commands.add_second_user(user_id=callback.from_user.id, chat_id=chat_id[0].chat_id)
            await callback.message.answer(text=f'Собеседник найден!\n'
                                                f'Соеденить?', reply_markup=create_join_partner())
        else:
            await callback.message.answer(text=f'На данный момент собеседников нет!')
            
        await callback.answer(show_alert=False)
        
        
    @dp.callback_query_handler(text='join_anonim_chat')
    async def join_anonim_chat(callback: CallbackQuery):
        await callback.message.answer(text='Ожидаем ответа!')
        chat_id = await anonimchat_commands.select_chat_id(user_id=callback.from_user.id)
        await b.send_message(chat_id=chat_id.chat_id, text='Вам пришел запрос!', reply_markup=create_conn_anon_chat())
        
        await callback.answer(show_alert=False)
        
    @dp.callback_query_handler(text='create_anonim_chat')
    async def create_anonim_chat(callback: CallbackQuery):
        await anonimchat_commands.create_anon_chat(first_user_id=callback.from_user.id, second_user_id=0)
        await callback.answer(text='Чат был создан. Ожидайте заявок на подключение!')
        await anonimchat_commands.update_chat_on_hold(chat_on_hold=True, chat_name=f'anon_chat_{round(callback.from_user.id/2)}')
        
        await callback.answer(show_alert=False)
        
    @dp.callback_query_handler(text='connect_anon_chat')
    async def connect_anon_chat(callback: CallbackQuery):
        await callback.answer('Вы ввошли в анонимный чат. Приятного общения!')
        chat_id = await anonimchat_commands.select_chat_id(chat_name=f'anon_chat_{round(callback.from_user.id/2)}')
        await b.send_message(chat_id=chat_id.second_user_id, text='Вы ввошли в анонимный чат. Приятного общения!')
        
        await callback.answer(show_alert=False)
        
    @dp.message_handler()
    async def send_anon_message(message: Message):
        
        await b.send_message(chat_id=chat_id, text=message.text)