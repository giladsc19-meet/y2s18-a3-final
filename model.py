from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# this is the user object model

class User(Base):
    __tablename__= "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birthdate = Column(String)
    user_name = Column(String)
    password = Column(String)
    bio = Column(String)
    image_url = Column(String)
    # posts = Column(list)
    # badges = Column(list)

# this is the post object model

class Post(Base):
    __tablename__= "posts"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    text = Column(String)
    image_url = Column(String)
    claps_num = Column(Integer)
    # badge = Column(String)


# <!-- {% for post in user_posts %} -->

#   <!-- {% endfor %} -->

#       <!-- <blockquote class="quote-box">
#                                     <p class="quotation-mark"></p>
#                                     <p class="quote-text">
#                                         {{post.text}}} 
#                                     </p>
#                                     <hr>
#                                     <div class="blog-post-actions">
#                                         <p class="blog-post-bottom pull-left">
#                                             {{post.user_name}}
#                                         </p>
#                                         <p class="blog-post-bottom pull-right">
#                                             <span class="badge quote-badge">{{post.claps_num}}</span>
#                                             <p><button type="button" class="btn btn-outline-primary">Clap</button></p> 
#                                         </p>
#                                     </div>
#                                 </blockquote> -->