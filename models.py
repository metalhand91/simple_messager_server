from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    register_date =  Column(DateTime, default=datetime.now())
    access_token = Column(String(64), nullable=True)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender = Column(ForeignKey("users.id"))
    reciver = Column(ForeignKey("users.id"))
    text = Column(Text, nullable=False)
    date_time = Column(DateTime, default=datetime.now())

#engine = create_engine('sqlite:///simple_messeger.db')
#metadata = Base.metadata
#metadata.create_all(engine)
