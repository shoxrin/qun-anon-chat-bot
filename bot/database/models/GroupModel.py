from sqlalchemy import Column, BigInteger, Boolean, String, sql
from bot.database import TimedBaseModel

class GroupModel(TimedBaseModel):
    __tablename__ = 'group'
    
    group_id = Column(BigInteger, primary_key = True)
    group_name = Column(String(250), primary_key = True)
    #group_img = Column()
    toxic_count = Column(BigInteger)
    
    
    query: sql.select