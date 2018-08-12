from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


<<<<<<< HEAD
	__tablename__ = 'user'
	user_id = Column(Integer, primary_key=True)
	user_name = Column(String)
	password = Column(String)


	def __repr__(self):
		return ("User Name: {}\n"
				"Password: {} \n"
				
					self.user_name,
					self.password)
=======
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
>>>>>>> 576060a3af181bdd55038c5278386fc0efcdc97f
