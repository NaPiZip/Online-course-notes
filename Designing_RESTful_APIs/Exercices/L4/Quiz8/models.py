from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string

from itsdangerous import (TimedJSONWebSignatureSerializer  as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

secret_key = ''.join(random.choice(
                                    string.ascii_uppercase +
                                    string.digits +
                                    string.ascii_lowercase) for x in range(32))
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(32), index = True)
    password_hash = Column(String(150))
    token = Column(String(32))

    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    #Add method to generate tokens
    def generate_token(self):
        self.token = ''.join(random.choice(
                                    string.ascii_uppercase +
                                    string.ascii_lowercase +
                                    string.digits) for x in range(32))
        return self.token

    #Add method to verify auth tokens
    def verify_token(self, token):
        return self.token == token

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    category = Column(String)
    price = Column(String)

    @property
    def serialize(self):
        return dict(name=  self.name,
                    category = self.category,
                    price = self.price)

engine = create_engine('sqlite:///regalTree.db/?check_same_thread=False', echo = True)

Base.metadata.create_all(engine)
