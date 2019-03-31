import sys, os

#change cwd and append path in order to find modules
os.chdir('../')
sys.path.append(os.getcwd())

from models import User
from dbSession import session

import requests

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

if __name__=='__main__':
    #Adding user in order to start test
    add_user_to_database('Nawin','1234')
    print_user_data("Nawin")
