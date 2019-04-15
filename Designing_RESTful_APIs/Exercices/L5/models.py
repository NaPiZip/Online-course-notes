from sqlalchemy import Column, Boolean, Integer, Float, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from passlib.hash import sha512_crypt
import random, string

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id              = Column(Integer,primary_key=True)
    password_hash   = Column(String(512))
    email           = Column(String, nullable=False)
    user_name       = Column(String, nullable=False, unique=True)
    picture         = Column(String)
    authenticated   = Column(Boolean, default=False)
    api_key         = Column(String(64))

    meal_requests = relationship("MealRequest")

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def print_hash(self):
        print(self.password_hash)

    def hash_password(self, password):
        self.password_hash = sha512_crypt.hash(password)

    def verify_password(self, password):
        return sha512_crypt.verify(password, self.password_hash)

    def generate_api_key(self):
        self.api_key = ''.join(random.choice(
                                            string.ascii_uppercase +
                                            string.digits +
                                            string.ascii_lowercase) for x in range(64))
    def verify_api_key(self, key):
        return self.api_key == key


    @property
    def serialize(self):
        return dict(id = self.id,
                    user_name = self.user_name,
                    email = self.email,
                    token = self.api_key)


class MealRequest(Base):
    __tablename__ = 'request'
    id              = Column(Integer, primary_key=True)
    user_id         = Column(Integer, ForeignKey('user.id'))

    meal_type       = Column(String, nullable=False)
    appointment_date= Column(String, nullable=False)
    meal_time       = Column(String, nullable=False)
    location_area   = Column(String, nullable=False)
    latitude        = Column(Float)
    longitude       = Column(Float)
    match_found     = Column(Boolean)

    def __init__(self, **kwargs):
        if  'meal_type'          not in kwargs or \
            'location_area'      not in kwargs or \
            'appointment_date'   not in kwargs:
           raise ValueError('Error some input arguments are missing!')
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def __repr__(self):
        return "<request {}>".format(self.id)

    @property
    def serialize(self):
        return dict(id = self.id,
                    user_id = self.user_id,
                    meal_type = self.meal_type,
                    appointment_date = self.appointment_date,
                    meal_time = self.meal_time,
                    location_area = self.location_area,
                    latitude = self.latitude,
                    longitude = self.longitude,
                    match_found = self.match_found)



class Proposal(Base):
    __tablename__ = 'proposal'
    user_porposed_from = Column(String)
    user_porposed_to   = Column(String)
    request_id         = Column(String, ForeignKey('request.id'), primary_key=True)
    filled             = Column(Boolean)
    meal_request       = relationship("MealRequest")

class Appointment(Base):
    __tablename__       = 'appointment'
    user_1              = Column(String)
    user_2              = Column(String)
    restaurant_name     = Column(String)
    restaurant_address  = Column(String)
    restaurant_picture  = Column(String)
    meal_time           = Column(String)
    id                  = Column(Integer, primary_key=True)
