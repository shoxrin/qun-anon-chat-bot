from sqlalchemy import Column, BigInteger, Boolean, String, sql

from bot.database import TimedBaseModel

    
class UserModel(TimedBaseModel):
    __tablename__ = 'users'
    
    user_id = Column(BigInteger, primary_key=True)
    admin = Column(Boolean)
    name = Column(String(200), primary_key=True)
    update_name = Column(String(50), primary_key = True)
    balance = Column(BigInteger)
    toxic = Column(Boolean)
    word_count = Column(BigInteger)
    toxic_word_count = Column(BigInteger)
    mute = Column(Boolean)
    
    query: sql.select
    