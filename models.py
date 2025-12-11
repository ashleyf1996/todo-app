#record inside DB table
#TABLE - EACH RECORD 
from database import Base #creating this model for our db.py file 
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base): #inherits base from db.py file
    __tablename__ = 'todos' #sql to know what to name table in db later on 

    id = Column(Integer, primary_key= True, index=True) #it will be an int this col. its indexable. its unuqie. increase perm
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean)


