from flask import request, jsonify

from models import  User
from dbSession import session


def get_api_key_user_from_db(key):
    return session.query(User).filter_by(api_key=key).first()


def require_api_key(f):
    def decorate(*args, **kwargs):
        if get_api_key_user_from_db(request.args.get('token')) is not None:
            return f(*args, **kwargs)
        else:
            return (jsonify({'data':'Unauthorized address trying to use API: {}'.format(request.remote_addr),
                            'error':'401'}), 401)
    return decorate
