import os
import sys

from flask import Flask, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant

sys.path.append('../two/')
from Geocode import GeocodeLocation
from Places import VenueSearch

try:
    engine = create_engine('sqlite:///mashup.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
except Exception as err:
    print("ERROR: Could not create database session!")
    print(err.args)
    sys.exit()

try:
    geo_obj = GeocodeLocation(key='')
    venue_obj = VenueSearch(id='',
                            secret='')
except Exception as err:
    print("ERROR: Could not create API helper!")
    print(err.args)
    sys.exit()

app = Flask(__name__)

@app.route("/restaurants", methods=['GET','POST'])
def allRestaurantHandler():
    return jsonify(geo_obj.getGeocodeLocation('Tokyo, Japan'))

@app.route("/restaurants/<int:id>", methods=['GET', 'UPDATE', 'DELETE'])
def restaurantHandler(id):
    return ''



if __name__ == '__main__':
    app.debug  = True
    app.run(host='0.0.0.0', port=5000)
