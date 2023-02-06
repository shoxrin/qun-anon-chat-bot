from aiogram import Dispatcher, Bot
from aiogram.types import Message

from bot.keybords import create_user_kb
from bot.database.methods import user_methods


def start_bot_handler(dp: Dispatcher) -> None:
    
    @dp.message_handler(commands=['start'])
    async def hello_user(message: Message):
        if message.chat.id > 0:
            try:
                user = await user_methods.select_user(message.from_user.id)
                if user.status == 'Active':
                    await message.answer(
                        f'Привет, {user.user_firstname}! Меня зовут Leskod. На данный момент ты можешь пользоваться '
                        f'анонимным чатом\n'
                        f'В будущем я собираюсь помогать тебе:\n'
                        f'-Анонимно находить собеседников\n'
                        f'-Находить чат для общения с кол-вом людей, которое постчитаешь нужным\n',
                        #f'-Если у тебя есть групповой чат, то можешь добавлять меня туда', 
                        reply_markup=create_user_kb()
                    )
            except Exception:
                await user_methods.add_user(
                    message.from_user.id, 
                    str(message.from_user.first_name), 
                    str(message.from_user.last_name)
                )
                
                await message.answer(
                    f'Привет, {user.user_firstname}! Меня зовут Leskod. На данный момент ты можешь пользоваться '
                    f'анонимным чатом\n'
                    f'В будущем я собираюсь помогать тебе:\n'
                    f'-Анонимно находить собеседников\n'
                    f'-Находить чат для общения с кол-вом людей, которое постчитаешь нужным\n',
                    #f'-Если у тебя есть групповой чат, то можешь добавлять меня туда', 
                    reply_markup=create_user_kb()
                )