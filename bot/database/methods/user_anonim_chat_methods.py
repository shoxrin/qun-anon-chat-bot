from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserChatModel


async def add_user_chat(user_id: int, chat_id: int):
    try:
        user = UserChatModel(chat_id=chat_id, user_id=user_id)
        await user.create()
    except UniqueViolationError as ex:
        print('Пользовательский чат не добавлен!', ex)
        
async def select_chat_id(user_id):
    chat_id = await UserChatModel.query.where(UserChatModel.user_id == user_id).gino.first()
    return chat_id