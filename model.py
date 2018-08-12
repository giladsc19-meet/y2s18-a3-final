from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


	__tablename__ = 'user'
	user_id = Column(Integer, primary_key=True)
	user_name = Column(String)
	password = Column(String)


	def __repr__(self):
		return ("User Name: {}\n"
				"Password: {} \n"
				
					self.user_name,
					self.password)