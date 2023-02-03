from sqlalchemy import Column, BigInteger, Integer, Boolean, String, sql
from bot.database import TimedBaseModel

class UserChatModel(TimedBaseModel):
    __tablename__ = 'UserChat'
    
    chat_id = Column(BigInteger, primary_key=True)
    chat_name = Column(String(250))
    first_user_id = Column(BigInteger)
    second_user_id = Column(BigInteger)
    chat_status = Column(Boolean, default=False)
    chat_on_hold = Column(Boolean, default=False)
    
    query: sql.select