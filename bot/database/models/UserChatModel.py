from sqlalchemy import Column, BigInteger, Integer, Boolean, String, sql
from bot.database import TimedBaseModel

class UserChatModel(TimedBaseModel):
    __tablename__ = 'UserChat'
    
    chat_id = Column(BigInteger)
    user_id = Column(BigInteger)
    
    query: sql.select