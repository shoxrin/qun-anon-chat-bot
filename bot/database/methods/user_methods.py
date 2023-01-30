from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserModel

async def add_user(user_id: int, user_firstname: str, user_lastname: str):
    try:
        user = UserModel(user_id=user_id, user_role='user', user_firstname=user_firstname, 
                        user_lastname=user_lastname, user_balance=0, status='Active',
                        staus_muted=False, status_toxic=False
                    )
        await user.create()
    except UniqueViolationError as ex:
        print('Пользователь не добавлен!', ex)
        
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