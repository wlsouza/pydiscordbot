from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()



def init_app():
    Base.metadata.create_all(engine)

