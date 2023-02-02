from sqlalchemy import Column, BigInteger, Integer, Boolean, String, sql
from bot.database import TimedBaseModel

class GroupModel(TimedBaseModel):
    __tablename__ = 'Group'
    
    group_id = Column(BigInteger, primary_key = True)
    group_name = Column(String(250))
    group_rank = Column(Integer, default=0)
    group_balance = Column(Integer, default=0)
    group_power_city = Column(Integer, default=0)
    group_count_users = Column(Integer, default=0)
    group_count_users_muted = Column(Integer, default=0)
    group_count_user_toxic = Column(Integer, default=0)
    group_timeout = Column(Boolean, default=False)
    
    query: sql.select