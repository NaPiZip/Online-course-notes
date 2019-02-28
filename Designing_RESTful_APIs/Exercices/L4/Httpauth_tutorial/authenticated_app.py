from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = "asasdasd"
auth = HTTPDigestAuth()

users = {
    "Time":"1234",
    "Nawin":"1234",
    "Susan": "bye"
    }


@app.route('/greeting')
def greeting():
    return "<h1>Welcome to Flask-HTTPAuth’s</h1>"

@app.route('/', methods = ['GET'])
@auth.login_required
def index():
    return "Hello"

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
