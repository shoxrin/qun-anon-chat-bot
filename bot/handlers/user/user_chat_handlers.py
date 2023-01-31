from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text

from bot.keybords import create_user_kb
from bot.keybords import create_user_balance_kb
from bot.database.methods import user_methods as commands

def user_chat_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Закрыть меню'))
    async def show_top_groups(message: Message):
        await message.answer(text='/menu - чтобы снова отктрыть меню', reply_markup=ReplyKeyboardRemove())
        
    @dp.message_handler(commands=['menu'])
    async def show_menu(message: Message):
        await message.answer(text='Что тебя интересует?', reply_markup=create_user_kb())
        
    @dp.message_handler(Text('Команды'))
    async def send_list_bot_commands(message: Message):
        await message.answer(text=f'Список команд бота:\n'
                             f'/start - запускает бота,\n'
                             f'/menu - открывает меню бота\n',
                             reply_markup=create_user_kb()
                            )
        
    @dp.message_handler(Text('Профиль'))
    async def show_user_info(message: Message):
        user = await commands.select_user(message.from_user.id)

        await message.answer(
            f'Имя: {user.user_firstname}\n'
            f'Место в рейтинге: {user.user_rank}\n'
            f'Баланс: {user.user_balance}\n'
            f'Кол-во отправленных сообщений: {user.count_words}\n'
            f'Кол-во отправленных не культурных сообщений: {user.count_toxic_words}\n'
        )
        
    @dp.message_handler(Text('Инфо'))
    async def show_bot_info(message: Message):
        user = await commands.select_user(message.from_user.id)

        await message.answer(
            f'Привет, {user.user_firstname}! Меня зовут Leskod. Я постараюсь облегчить '
            f'твое времяпровждение в телеграм!\n'
            f'С помощью меня ты сможешь:\n'
            f'-завести новые знакомства, как анонимно так и нет,\n'
            f'-найти чат для общения с кол-вом людей, которое постчитаешь нужным\n'
            f'И многое другое.'
        )