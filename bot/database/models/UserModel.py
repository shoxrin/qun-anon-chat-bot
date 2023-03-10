from sqlalchemy import Column, Integer, Boolean, String, sql, BigInteger

from bot.database import TimedBaseModel

    
class UserModel(TimedBaseModel):
    __tablename__ = 'Users'
    
    user_id = Column(BigInteger, primary_key=True)
    user_role = Column(String(100))
    user_firstname = Column(String(250))
    user_lastname = Column(String(250))
    user_rank = Column(Integer)
    user_balance = Column(Integer, default = 0)
    status = Column(String(30))
    status_anonim = Column(Boolean)
    name_anonim_chat = Column(String(250))
    staus_muted = Column(Boolean)
    status_toxic = Column(Boolean)
    count_words = Column(Integer)
    count_toxic_words = Column(Integer)
    
    query: sql.select
    