from model import Base, Column, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def check_user_name_available(user_name):
    if session.query(User).filter_by(user_name=user_name).first()!=None:
        return True
    else:
        return False

########################################################################################## Dont care about the above !



# 1) add a user to the database ! (PES: gets called in the SIGN UP)


def add_user(user_name, password):

    if check_user_name_available(user_name):
        return False
        #put java script for let another option of writing

    else:
        new_user = User(user_name = user_name, password = password)
        session.add(new_user)
        session.commit()
        return True


# 2) check if a user exists in the database ! (PES: gets called in the LOG IN)


def check_user(user_name, password):
    if session.query(User).filter_by(user_name=user_name,password=password).first()!=None:
        return True
    else:
        return False


# 3) get all the users from the database ! (PES: gets passed to login.html to check if the user exists in the database when logging in)


def get_all_users():
    users = session.query(User).all()
    return users


# 4) get a user from the database ! (PES: gets passed to profile.html to display the user info)


def get_by_user_name(user_name):
    user = session.query(User).filter_by(user_name=user_name).first()
    return user


# 5) get the post of the other users (THE FEED) PES: gets passed to home.html


def get_posts():


# 6) edit the image of the user


def edit_image(user_name):
	



