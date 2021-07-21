from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..config import settings

Base = declarative_base()

engine = create_engine(settings.sqlalchemy_database_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def init_app():
    Base.metadata.create_all(engine)
