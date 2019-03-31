from flask import Blueprint
from flask import redirect, request, render_template, url_for, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from models import User
from dbSession import session

login_api = Blueprint('login_api', __name__)

try:
    login_manager = LoginManager()
except  Exception as err:
    print("Error creating login manaer {}".format(err.args))
    system.exit()

@login_manager.user_loader
def load_user(id):
    return session.query(User).filter_by(id=id).first()

@login_api.route('/login', methods=['GET','POST'])
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
            return redirect(url_for('apiKey'))
        else:
            error = 'Invalid Credentials'
    return render_template('login.html', error = error)

@login_api.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    session.add(user)
    session.commit()
    logout_user()
    return jsonify(dict(message="User has been loged out successfully!")),200
