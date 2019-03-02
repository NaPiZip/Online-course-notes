from models import Base, User, Product

from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
import sys

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///regalTree.db/?check_same_thread=False')

try:
    DBSession = sessionmaker(bind = engine)
    session = DBSession()
except:
    sys.exit()


app = Flask(__name__)


@app.route('/users', methods = ['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print("Missing arguments")
        abort(400)

    username_query = session.query(User).filter_by(username = username).first()
    if username_query is not None:
        print("Existing user found")
        return jsonify({'message':'user already exists'}),200

    user = User(username = username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify({'username:':user.username}),201

@app.route('/user/<int:id>')
def get_user(id):
    user_query = session.query(User).filter_by(id=id).first()
    if user is None:
        abort(400)
    return jsonify({'username':user_query.username})

@app.route('/resource')
@auth.login_required
def showAllProducts():
    if request.method == 'GET':
        products_query = session.query(Products).all()
        return jsonify(products = [p.serialize for p in products_query])
    elif request.method == 'POST':
        name = request.json.get('name')
        category = request.json.get('category')
        price = request.json.get('price')
        new_item = Product(name = name, category = category, price = price)
        session.add(new_item)
        session.commit()
        return jsonify(new_item.serialize)

@app.route('/products/<category>')
@auth.login_required
def showCategoriedProducts(category):
    existing_categories_list = ['fruit', 'legume', 'vegetable']
    if category in  existing_categories_list:
        item_query = session.query(Product).filter_by(category = category).all()
        return jsonify(products = [p.serialize for p in item_query])
    else:
        return jsonify({'message':'category not found'}),400

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
