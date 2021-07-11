from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ext.config import settings

Base = declarative_base()

engine = create_engine(settings.sqlalchemy_database_url, echo=True)
Session = sessionmaker(bind=engine)
session = Session()



def init_app():
    Base.metadata.create_all(engine)

