#!/usr/bin/env python

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import request, g, redirect, flash, url_for
from flask import Flask, jsonify, render_template

from models import Base, User, MealRequest

from flask_login import LoginManager, login_required, login_user, current_user

engine = create_engine('sqlite:///finalProject.db/?check_same_thread=False', echo = True)

try:
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
except Exception as err:
    print("Error createing DB session: {}".format(err.args))
    sys.exit()

try:
    login_manager = LoginManager()
except  Exception as err:
    print("Error creating login manaer {}".format(err.args))
    system.exit()

app = Flask(__name__)

@login_manager.user_loader
def load_user(id):
    return session.query(User).filter_by(id=id).first()

@app.route('/', methods = ['GET'])
@login_required
def index():
    return jsonify(dict(content='content 12')),200

@app.route('/welcome', methods = ['GET'])
def welcomePage():
    return render_template('welcome.html')


@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = session.query(User).filter_by(user_name=request.form['username']).first()
        if user is not None and user.verify_password(request.form['password']):
            user.authenticated = True;
            session.add(user)
            session.commit()

            print('Success')
            login_user(user)
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error = error)

@app.route('/logout')
@login_required
def logout():
    print(current_user.user_name)
    return 'asd'

if __name__ == '__main__':
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    app.secret_key="Something"
    app.run(host='0.0.0.0', port = 5000, debug=True)

    #tutorial http://www.patricksoftwareblog.com/tag/flask-login/
