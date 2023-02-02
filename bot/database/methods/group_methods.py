from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import GroupModel


async def add_group_chat(group_id: int, group_name: str):
    try:
        group = GroupModel(group_id=group_id, group_name=group_name)
        await group.create()
    except UniqueViolationError:
        print('Чат не добавлен!')
        
async def select_all_users():
    groups = await GroupModel.query.gino.all()
    return groups