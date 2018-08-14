from model import Base, Column, User, Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

###add & delete
# 1) add a user to the database ! (PES: gets called in the SIGN UP)
def add_user(user_name, password):
    print("Add a User!")
    if check_user_name_available(user_name)==True:
        print ("cant use")
        return False
    else:
        user = User(user_name = user_name, password = password)
        session.add(user)
        session.commit()
        return True

def delete_user_by_user_name(user_name):
    session.query(User).filter_by(user_name = user_name).delete().first()
    session.commit()

def check_user_name_available(user_name):
    if session.query(User).filter_by(user_name=user_name).first()!=None:
        return True
    else:
        return False

# 2) check if a user exists in the database ! (PES: gets called in the LOG IN)

def check_user(user_name, password):
    if session.query(User).filter_by(user_name=user_name,password=password).first()!=None:
        return True
    else:
        return False        
###reaching users

# 3) get all the users from the database ! (PES: gets passed to login.html to check if the user exists in the database when logging in)

def get_all_users():
    users = session.query(User).all()
    return users


# 4) get a user from the database ! (PES: gets passed to profile.html to display the user info)


def get_by_user_name(user_name):
    user = session.query(User).filter_by(user_name=user_name).first()
    return user

########################################################################################################

def make_post(user_id, text, image_url):
    post = Post(user_id = user_id,text = text, image_url = image_url)
    session.add(post)
    session.commit()
    return post
# 5) get the post of the other users (THE FEED) PES: gets passed to home.html


def get_posts():
    posts = session.query(Post).all()
    print("get posts")
    return posts

# 6) edit the image of the user


def edit_image(user_name):
    pass
	



