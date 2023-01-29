from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserModel

async def add_user(user_id: int, name: str, balance: int, update_name: str):
    try:
        user = UserModel(user_id=user_id, name=name, update_name=update_name, balance=balance)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен!')
        
async def select_all_users():
    users = await UserModel.query.gino.all()
    return users

async def count_users():
    count = await db.func.count(UserModel.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await UserModel.query.where(UserModel.user_id == user_id).gino.first()
    return user

async def update_user_name(user_id, new_name):
    user = await select_user(user_id)
    await user.update(update_name=new_name).apply()