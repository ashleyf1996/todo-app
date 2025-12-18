from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

#engine to open a connection inside engine- args to pass into engine to connect to db. false by default thread. however fastapi its normal to check multiple thread
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread' : False})

#db session. will be come db we want session local . we want to bind to engine we just created. autocommits are false. we wanna be incontrol 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#create db object we can interact with
#call our db, be able ot create a base which is object of db to conrol db. creating tables ect.. 
#in py we will interact with db 
Base = declarative_base()
