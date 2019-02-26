from flask import Flask, jsonify, request
from flask_httpauth import HTTPDigestAuth


app = Flask(__name__)
app.config['SECRET_KEY'] = "asasdasd"
auth = HTTPDigestAuth()

users = {
    "Nawin":"1234",
    "Susan": "bye"
    }


@app.route('/i')
def greeting():
    return "<h1>Welcome to Flask-HTTPAuth’s</h1>"

@app.route('/')
@auth.login_required
def index():
    return "Hello"

@app.route('/lol')
@auth.login_required
def auth_route():
    return "Hello, {}".format(auth.username())

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
