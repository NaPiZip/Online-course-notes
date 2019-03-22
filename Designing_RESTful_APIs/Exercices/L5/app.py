import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import request, g
from flask import Flask, jsonify, render_template

from models import Base, User, MealRequest

from flask_httpauth import HTTPBasicAuth

engine = create_engine('sqlite:///finalProject.db/?check_same_thread=False', echo = True)

try:
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
except Exception as err:
    print("Error createing DB session: {}".format(err.args))
    sys.exit()

auth = HTTPBasicAuth()
app = Flask(__name__)


def Verify_pw(username_or_token,password):
    print("Verifying")
    return None

@app.route('/', methods = ['GET'])
@auth.login_required
def index():
    return jsonify(dict(content='content 12')),200

@app.route('/welcome', methods = ['GET'])
def welcomePage():
    return render_template('welcome.html')


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.headers)
        if request.form['username'] != 'admin' or request.form['password'] != '1234':
            error = 'Invalid Credentials'
        else:
            print('redirect')
            return jsonify(dict(redirect='/')),200
    print(error)
    return render_template('login.html',error=error)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'some_wierd_secret_key'
    app.run(host='0.0.0.0', port = 5000)

    ##TODO: https://scotch.io/tutorials/authentication-and-authorization-with-flask-login
