from flask import Blueprint
from flask import redirect, request, render_template, url_for, jsonify

from models import User
from dbSession import session

from loginAPIKeyDecorator import require_api_key

app_endpoints = Blueprint('app_endpoints', __name__)

@app_endpoints.route('/v1/users', methods = ['GET', 'PUT'])
@require_api_key
def get_all_users():
    if request.method == 'GET':
        user_list = session.query(User).all()
        if user_list is not None:
            return jsonify([user.serialize for user in user_list])
        else:
            return 'None'
    elif request.method == 'PUT':
        username = request.json.get('user_name')
        new_password = request.json.get('password')
        new_token    = request.json.get('token')
        if username is not None:
            current_user = session.query(User).filter_by(user_name=username).first()
        else:
            current_user = None
        if current_user is not None:
            if new_password is not None:
                current_user.hash_password(new_password)
            if new_token is not None:
                current_user.api_key = new_token
            session.commit()
            return jsonify(dict(message="Success, updated user: {}!".format(username))),201
        else:
            return jsonify(dict(message="ERROR, not all parameter provided!")),404

@app_endpoints.route('/v1/users/<int:id>', methods=['GET'])
@require_api_key
def get_user_with_id(id):
    print("asdasdasd")
    print(id)
    return "None"
