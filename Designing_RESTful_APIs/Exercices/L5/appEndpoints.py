from flask import Blueprint
from flask import redirect, request, render_template, url_for, jsonify

from models import User
from dbSession import session

from loginAPIKeyDecorator import require_api_key

app_endpoints = Blueprint('app_endpoints', __name__)

@app_endpoints.route('/v1/users')
@require_api_key
def get_all_users():
    user_list = session.query(User).all()
    if user_list is not None:
        return jsonify([user.serialize for user in user_list])
    else:
        return 'None'
