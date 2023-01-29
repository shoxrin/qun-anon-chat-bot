import sqlalchemy as sa
from gino import Gino
from sqlalchemy import Column, String, BigInteger, sql

from bot.database import BaseModel

    
class TestModel(BaseModel):
    __tablename__ = 'testModel'
    
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    
    query: sql.select
    
print(TestModel())