from sqlalchemy import Column, Integer, String
from database import Base

class TaskBase(Base):
    __tablename__='task'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(20))
    subTitle = Column(String(20))
    description = Column(String(200))
    priority = Column(Integer)
    status_id = Column(Integer)