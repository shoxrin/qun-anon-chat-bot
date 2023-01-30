from sqlalchemy import Column, Integer, Boolean, String, sql

from bot.database import TimedBaseModel

    
class UserModel(TimedBaseModel):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    user_role = Column(String(100))
    user_firstname = Column(String(250))
    user_lastname = Column(String(250))
    user_rank = Column(Integer)
    user_balance = Column(Integer)
    status = Column(String(30))
    staus_muted = Column(Boolean)
    status_toxic = Column(Boolean)
    count_words = Column(Integer)
    count_toxic_words = Column(Integer)
    
    query: sql.select
    