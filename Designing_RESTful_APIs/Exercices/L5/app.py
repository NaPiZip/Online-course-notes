#!/usr/bin/env python

import sys
import requests

from flask import Flask
from flask import request, jsonify, render_template
from flask_login import current_user

from models import User, MealRequest, Proposal, Appointment, Base
from dbSession import session, engine

from loginAPI import login_api, login_manager, login_required
from loginAPIKeyDecorator import require_api_key
from appEndpoints import app_endpoints

app = Flask(__name__)

app.register_blueprint(login_api)
app.register_blueprint(app_endpoints)

Base.metadata.create_all(engine)

@app.route('/', methods = ['GET'])
def welcomePage():
    return render_template('welcome.html')

@app.route('/apiKey', methods = ['GET'])
@login_required
def apiKey():
    user = current_user
    return jsonify(dict(token=current_user.api_key)),200

##Dev routes
@app.route('/dev')
def dev_route():
    user = session.query(User).first()
    if user is not None:
        new_meal_request = MealRequest(user_id=user.get_id(), meal_type = 'Shit')
        user.meal_requests.append(new_meal_request)
        session.commit()
        return jsonify(dict(tesxt='Something')),301
    else:
        return 'Error'

@app.route('/debug')
def debug():
    meal_request = session.query(MealRequest).first()
    return jsonify(dict(id=meal_request.user_id, meal=meal_request.meal_type))

@app.route('/ping')
def ping():
    #todo add secrets loader
    parameter = dict(client_id='',
                     client_secret='',
                     v="20180323",
                     near="Ann Arbor", query="Tacos",limit=10)
    response = requests.get('https://api.foursquare.com/v2/venues/search',params=parameter)
    return jsonify(response.json())

if __name__ == '__main__':
    login_manager.init_app(app)
    login_manager.login_view = 'login_api.login'
    app.config['JSON_SORT_KEYS'] = False
    app.secret_key="Something"
    app.run(host='0.0.0.0', port = 5000, debug=True)

    #tutorial http://www.patricksoftwareblog.com/tag/flask-login/
