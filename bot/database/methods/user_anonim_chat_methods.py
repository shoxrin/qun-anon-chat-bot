from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserChatModel


async def create_anon_chat(first_user_id: int, second_user_id: int):
    try:
        user = UserChatModel(chat_id=round(first_user_id/2), chat_name=f'anon_chat_{round(first_user_id / 2)}', first_user_id=first_user_id, second_user_id=second_user_id)
        await user.create()
    except UniqueViolationError as ex:
        print('Пользовательский чат не добавлен!', ex)

async def update_chat_status(chat_status: bool, chat_id: int):
    chat = await select_chat_id(chat_id)
    return chat.update(chat_status=chat_status).apply()

async def update_chat_on_hold(chat_on_hold: bool, chat_id: int):
    chat = await select_chat_id(chat_id)
    return chat.update(chat_on_hold=chat_on_hold).apply()

async def add_second_user(user_id: int, chat_id: int):
    chat = await select_chat_id(chat_id)
    return chat.update(second_user_id=user_id)

async def find_anon_chat():
    chats_id = await UserChatModel.query.where(UserChatModel.chat_on_hold == True).gino.all()
    return chats_id

async def select_chat_id(chat_id):
    chat_id = await UserChatModel.query.where(UserChatModel.chat_id == chat_id).gino.first()
    return chat_id