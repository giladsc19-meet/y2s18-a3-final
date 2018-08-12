from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Place your database schema code here

# Example code:
class User(Base):
    __tablename__= users
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(String)
#   birthday = Column(String)
    posts = Column(object)

    def __repr__(self):
        return ("User_name: {}, Password:{}, birthday:{}".format(self.user_name, self.password, self.birthday))