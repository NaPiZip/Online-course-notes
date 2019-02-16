from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key = True)
    name  = Column(String(80), nullable = False)
    description = Column(String(250))

    def serialize(cls):
        return [cls.id, cls.name, cls.description] 

engine = create_engine('sqlite:///pupies.db', echo=True)
Base.metadata.create_all(engine)
