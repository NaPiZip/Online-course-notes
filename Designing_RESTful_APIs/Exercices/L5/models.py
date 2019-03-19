from sqlalchemy import Column, Boolean, Integer, Float, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id              = Column(Integer,primary_key=True)
    password_hash   = Column(String)
    email           = Column(String, nullable=False)
    picture         = Column(String)

    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hash_password)


class MealRequest(Base):
    __tablename__ = 'request'
    id              = Column(Integer, primary_key=True)
    user_id         = Column(Integer, ForeignKey('user.id'))
    meal_type       = Column(String)
    location_name   = Column(String)
    latitude        = Column(Float)
    longitude       = Column(Float)
    appointment_date= Column(Date)
    meal_time       = Column(String)
    match_found     = Column(Boolean)



engine = create_engine('sqlite:///finalProject.db/?check_same_thread=False', echo = True)
Base.metadata.create_all(engine)
