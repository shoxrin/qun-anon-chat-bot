from sqlalchemy import Column, Integer, Boolean, String, sql
from bot.database import TimedBaseModel

class UserChatModel(TimedBaseModel):
    __tablename__ = 'UserChat'
    
    user_id = Column(Integer)
    chat_id = Column(Integer)
    
    query: sql.select