#record inside DB table
#TABLE - EACH RECORD 
from database import Base #imported DB. creating this model for our db.py file . impr
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True )
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name= Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)



class Todos(Base): #inherits base from db.py file
    __tablename__ = 'todos' #CREATE NEW TABLEsql to know what to name table in db later on 

    id = Column(Integer, primary_key= True, index=True) #it will be an int this col. its indexable. its unuqie. increase perm
    title = Column(String)
    description = Column(String)
    priority = Column(Integer) #these will all default as null
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))