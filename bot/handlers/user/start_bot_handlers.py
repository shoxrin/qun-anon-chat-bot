from aiogram import Dispatcher
from aiogram.types import Message

from bot.keybords import create_user_kb
from bot.database.methods import user_methods


def start_bot_handler(dp: Dispatcher) -> None:
    
    @dp.message_handler(commands=['start'])
    async def hello_user(message: Message):
        try:
            user = await user_methods.select_user(message.from_user.id)
            if user.status == 'Active':
                await message.answer(text=f'Привет, {user.user_firstname}!\n'
                                    f'Что умеет этот бот?\n'
                                    f'Ничего, пшел нахуй еблан!!!', reply_markup=create_user_kb())
        except Exception:
            await user_methods.add_user(message.from_user.id, str(message.from_user.first_name), 
                                        str(message.from_user.last_name)
                                    )
            await message.answer(text=f'Привет!'
                                f'Что умеет этот бот?'
                                f'Ничего, пшел нахуй еблан!!!', reply_markup=create_user_kb())