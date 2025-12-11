from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

#engine to open a connection inside engine- args to pass into engine to connect to db. false by default thread. however fastapi its normal to check multiple thread
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread' : False})