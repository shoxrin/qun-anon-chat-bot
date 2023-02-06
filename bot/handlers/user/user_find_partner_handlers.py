from aiogram import Dispatcher, Bot
from asyncpg import UniqueViolationError
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.misc.settings import bot
from bot.keybords import create_user_kb
from bot.keybords import create_find_partner
from bot.keybords import create_join_partner
from bot.keybords import create_conn_anon_chat
from bot.misc import get_random_anonim_userid
from bot.database.methods import user_methods as methods_db
from bot.database.methods import user_anonim_chat_methods as anonimchat_commands


def user_find_partner_handlers(dp: Dispatcher):
    
    #Anonymous chat button handler
    @dp.message_handler(Text('Найти собеседника'))
    async def find_chat(message: Message):
        await message.answer(text='Выберите удобный для себя вариант!', reply_markup=create_find_partner())
    
    #Handler for creating an anonymous chat entry in the chat table
    @dp.callback_query_handler(text='create_anonim_chat')
    async def create_anonim_chat(callback: CallbackQuery):
        user_id = callback.from_user.id
        try:
            await anonimchat_commands.create_anon_chat(first_user_id=user_id)
            chat = await anonimchat_commands.select_chat_id(chat_id=round(user_id/2))
            
            await methods_db.set_name_anonim_chat(user_id=user_id, name_anonim_chat=chat.chat_name)
            await anonimchat_commands.update_chat_on_hold(chat_on_hold=True, chat_name=chat.chat_name)
            
            await callback.message.answer(text='Чат был создан! Ищем собеседника.')
            
        except UniqueViolationError:
            await callback.message.answer(text='Чат уже был создан! Ищем собеседника.')
            
            chat = await anonimchat_commands.select_chat_id(chat_id=round(user_id/2))
            await methods_db.set_name_anonim_chat(user_id=user_id, name_anonim_chat=chat.chat_name)
            await anonimchat_commands.update_chat_on_hold(chat_on_hold=True, chat_name=chat.chat_name)
            await anonimchat_commands.add_second_user(user_id=0, chat_id=chat.chat_id)
            
        await callback.answer(show_alert=False)
    
    #Search for anonymous chats to which you can connect and select a random one
    @dp.callback_query_handler(text='find_anonim_chat')
    async def find_anonim_chat(callback: CallbackQuery):
        user_id = callback.from_user.id
        chats = await anonimchat_commands.find_anon_chat()
        chat = get_random_anonim_userid(chats, user_id)        
        if chat[1]:
            await callback.message.answer(text='Собеседник найден, подключиться?', reply_markup=create_join_partner())
            await methods_db.set_name_anonim_chat(user_id=user_id, name_anonim_chat=chat[0].chat_name)
        else:
            await callback.message.answer(text='На данный момент активных чатов нет!')
            
        await callback.answer(show_alert=False)

    #Sending a connection request to the selected anonymous chat
    @dp.callback_query_handler(text='join_anonim_chat')
    async def join_anonim_chat(callback: CallbackQuery):
        user = await methods_db.select_user(user_id=callback.from_user.id)
        chat = await anonimchat_commands.select_chat_by_name(chat_name=user.name_anonim_chat)
        await anonimchat_commands.add_second_user(user_id=user.user_id, chat_id=chat.chat_id)
        await bot.send_message(chat_id=chat.first_user_id, text='Вам пришел запрос! Подключить?', reply_markup=create_conn_anon_chat())
        await callback.message.answer(text='Запрос отправлен! Ждите ответа.')
        
        await callback.answer(show_alert=False)
    
    #Positive response to connection request
    @dp.callback_query_handler(text='connect_anon_chat')
    async def connect_anon_chat(callback: CallbackQuery):
        await callback.message.answer(text='Вы подключены к чату! Можете начинать общение.')
        chat = await anonimchat_commands.select_chat_id(chat_id=round(callback.from_user.id/2))
        await anonimchat_commands.update_chat_on_hold(chat_on_hold=False, chat_name=chat.chat_name)
        await anonimchat_commands.update_chat_status(chat_status=True, chat_id=chat.chat_id)
        
        await bot.send_message(chat_id=chat.second_user_id, text='Вы подключены к чату! Можете начинать общение.')
        
        await callback.answer(show_alert=False)
    
    #Handler for the /stop command, which exits the anonymous chat
    @dp.message_handler(commands=['stop'])
    async def exit_anon_chat(message: Message):
        user_id = message.from_user.id
        user = await methods_db.select_user(user_id=user_id)
        chat = await anonimchat_commands.select_chat_by_name(chat_name=user.name_anonim_chat)
        if user_id == chat.second_user_id:
            await methods_db.set_name_anonim_chat(user_id=user_id, name_anonim_chat=None)
            await anonimchat_commands.update_chat_status(chat_status=False, chat_id=chat.chat_id)
            await message.answer(text='Вы вышли из чата. Собираетесь продолжить?', reply_markup=create_find_partner())
            await bot.send_message(chat_id=chat.first_user_id, text='Собеседник вышел из чата. Собираетесь продолжить?', reply_markup=create_find_partner())
        elif user_id == chat.first_user_id:
            await methods_db.set_name_anonim_chat(user_id=user_id, name_anonim_chat=None)
            await anonimchat_commands.update_chat_status(chat_status=False, chat_id=chat.chat_id)
            await message.answer(text='Вы вышли из чата. Собираетесь продолжить?', reply_markup=create_find_partner())
            await bot.send_message(chat_id=chat.second_user_id, text='Собеседник вышел из чата. Собираетесь продолжить?', reply_markup=create_find_partner())
        
    #Anonymous chat message handler
    @dp.message_handler()
    async def send_anon_message(message: Message):
        chat_name = await methods_db.select_user(user_id=message.from_user.id)
        chat = await anonimchat_commands.select_chat_by_name(chat_name=chat_name.name_anonim_chat)
        if chat.chat_status:
            if message.from_user.id == chat.first_user_id:
                await bot.send_message(chat_id=chat.second_user_id, text=message.text)
            else:
                await bot.send_message(chat_id=chat.first_user_id, text=message.text)
                
    @dp.callback_query_handler(text='cancel_search_anon_chat')
    async def cancel_search_anon_chat(callback: CallbackQuery):
        await callback.message.answer(text='Чем собираетесь заняться?', reply_markup=create_user_kb())
        await callback.answer(show_alert=False)