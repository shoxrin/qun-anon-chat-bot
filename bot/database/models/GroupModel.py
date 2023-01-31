from sqlalchemy import Column, Integer, Boolean, String, sql
from bot.database import TimedBaseModel

class GroupModel(TimedBaseModel):
    __tablename__ = 'Group'
    
    group_id = Column(Integer, primary_key = True)
    group_name = Column(String(250))
    group_rank = Column(Integer)
    group_balance = Column(Integer)
    group_power_city = Column(Integer)
    group_count_users = Column(Integer)
    group_count_users_muted = Column(Integer)
    group_count_user_toxic = Column(Integer)
    group_timeout = Column(Boolean, default=False)
    
    query: sql.select