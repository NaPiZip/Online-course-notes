from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, MealRequest

import requests

engine = create_engine('sqlite:///finalProject.db/?check_same_thread=False')

try:
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
except Exception as err:
    print("Error createing DB session: {}".format(err.args))
    sys.exit()


def add_user_to_database(name, password):
    if session.query(User).filter_by(user_name=name).first() is not None:
        return
    else:
        new_user = User(user_name=name, email = "something@google.de")
        new_user.hash_password(password)
        new_user.generate_api_key()
        session.add(new_user)
        session.commit()

def print_user_data(ID):
    user_query = session.query(User).filter_by(user_name=ID).first()
    if user_query is not None:
        print(user_query.serialize)
    else:
        print("Error: Could not find user with ID {} !".format(ID))

def make_unauthorized_request(url):
    response = requests.get(url)
    print(response)

if __name__=='__main__':
    #Adding user in order to start test
    add_user_to_database('Nawin','1234')
    print_user_data("Nawin")
    make_unauthorized_request('http://localhost:5000/')
