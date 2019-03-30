#!/usr/bin/env python

import sys

from flask import Flask
from flask import request, jsonify, render_template
from flask_login import current_user

from models import Base, User, MealRequest
from dbSession import session

from loginAPI import login_api, login_manager, login_required

app = Flask(__name__)
app.register_blueprint(login_api)


@app.route('/', methods = ['GET'])
def welcomePage():
    return render_template('welcome.html')


@app.route('/apiKey', methods = ['GET'])
@login_required
def apiKey():
    user = current_user
    return jsonify(dict(api_key=current_user.api_key)),200


if __name__ == '__main__':
    login_manager.init_app(app)
    login_manager.login_view = 'login_api.login'
    app.secret_key="Something"
    app.run(host='0.0.0.0', port = 5000, debug=True)

    #tutorial http://www.patricksoftwareblog.com/tag/flask-login/
