from asyncpg import UniqueViolationError

from bot.database import db
from bot.database.models import UserModel

async def add_user(user_id: int, user_firstname: str, user_lastname: str):
    try:
        user = UserModel(user_id=user_id, user_role='user', user_firstname=user_firstname, 
                        user_lastname=user_lastname, user_rank=0, user_balance=0, status='Active', status_anonim=False, name_anonim_chat=None,
                        staus_muted=False, status_toxic=False, count_words=0, count_toxic_words=0
                    )
        await user.create()
    except UniqueViolationError as ex:
        print('Пользователь не добавлен!', ex)
        
async def select_all_users():
    users = await UserModel.query.gino.all()
    return users

async def get_user_id_anonim():
    users = await UserModel.query.where(UserModel.status_anonim == True).gino.all()
    return users

async def count_users():
    count = await db.func.count(UserModel.user_id).gino.scalar()
    return count

async def select_user(user_id: int):
    user = await UserModel.query.where(UserModel.user_id == user_id).gino.first()
    return user

async def select_user_by_name_chat(anon_name_chat: str):
    user = await UserModel.query.where(UserModel.name_anonim_chat == anon_name_chat).gino.first()
    return user

async def update_status_anonim(user_id: int, status: bool):
    user = await select_user(user_id)
    await user.update(status_anonim=status).apply()
    
async def set_name_anonim_chat(user_id: int, name_anonim_chat: str):
    user = await select_user(user_id)
    await user.update(name_anonim_chat=name_anonim_chat).apply()