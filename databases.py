# Database related imports
# Make sure to import your tables!
from model import Base, Column, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# You can change the name of your database, just change project.db to whatever you want (make sure to include .db at the end!)
# Make sure you have the same name for the database in the app.py file!
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

###add & delete
def add_user(self, user_name, password, birthday):
    print("Add a User!")
    user = User(user_name = user_name, password = password, birthdat = birthday)
    session.add(user)
    session.commit()

def delete_user_by_user_name(user_name):
    session.query(User).filter_by(user_name = user_name).delete().first()
    session.commit()
###check user (exsist?)
def check_user(user_name,password):
    session.query(User).filter_by(user_name=user_name,password=password).first()
###reaching users
def get_all_users():
    users = session.query(User).all()
    return users

def get_user_by_user_name(user_name):
    user = session.query(User).filter_by(user_name=user_name).first()
    return user
