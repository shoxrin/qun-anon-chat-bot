from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from bot.database.methods import user_methods as commands

def user_info_handlers(dp: Dispatcher):
    
    @dp.message_handler(Text('Инфо'))
    async def show_info(message: Message):
        user = await commands.select_user(message.from_user.id)

        await message.answer(
            f'Имя: {user.user_firstname}\n'
            f'Место в рейтинге: {user.user_rank}\n'
            f'Баланс: {user.user_balance}\n'
            f'Кол-во отправленных сообщений: {user.count_words}\n'
            f'Кол-во отправленных не культурных сообщений: {user.count_toxic_words}\n'
        )