from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# this is the user object model

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(String)
    user_name = Column(String)
    password = Column(String)
    bio = Column(String)
    image_url = Column(String)
    user_posts = relationship("Post", back_populates="user")
    # badges = Column(list)

# this is the post object model

class Post(Base):
    __tablename__= "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user_posts")
    # badge = Column(String)
