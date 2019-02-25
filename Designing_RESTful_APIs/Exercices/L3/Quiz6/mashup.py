import os
import sys

from flask import Flask, jsonify, request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Restaurant

sys.path.append('../two/')
from Geocode import GeocodeLocation
from Places import VenueSearch

try:
    engine = create_engine('sqlite:///mashup.db?check_same_thread=False', echo=True)
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

@app.route("/restaurants", methods=['GET','POST', 'DELETE'])
def allRestaurantHandler():
    if request.method == 'POST':
        venue_location = request.args.get('location', '')
        meal_type = request.args.get('mealType', 'Pizza')
        if venue_location:
            try:
                lat_long_coordinates = geo_obj.getGeocodeLocation(venue_location)
                venue_dict = venue_obj.getVenueInfoDict(lat_long_coordinates,meal_type)
                photo_url = venue_obj.getVenuePhotoUrl(venue_dict.get('id'))
                if not photo_url:
                    photo_url = 'https://proxy.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.clker.com%2Fcliparts%2Fq%2FL%2FP%2FY%2Ft%2F6%2Fno-image-available-md.png&f=1'
                if lat_long_coordinates and venue_dict:
                    venue_address = "{} {} {}".format(venue_dict.get('location').get('address'),
                                                      venue_dict.get('location').get('postalCode'),
                                                      venue_dict.get('location').get('city'))
                    veno_dict_striped = dict(restaurant_name = venue_dict.get('name'),
                                            restaurant_address = venue_address,
                                            restaurant_image = photo_url)
                    return jsonify(addRestaurantToDB(veno_dict_striped))
                else:
                     return jsonify(dict(description='ERROR:Couldn\'t query {}!'.format(venue_location),status='404'))
            except Exception as err:
                print(err.args)
                return jsonify(dict(description='ERROR:Something went wrong!',status='404'))
        else:
            return jsonify(dict(description='ERROR:No location found!',status='404'))

    elif request.method == 'GET':
        return jsonify(getAllRestaurantsFromDB())
    elif request.method == 'DELETE':
        return jsonify(deleteAllRestaurants())

@app.route("/restaurants/<int:id>", methods=['GET', 'UPDATE', 'DELETE'])
def restaurantHandler(id):
    if request.method == 'GET':
        return jsonify(getRestaurantByIdFromDB(id))
    elif request.method == 'DELETE':
        return jsonify(deleteRestaurantFromDB(id))
    elif request.method == 'UPDATE':
        new_name = request.args.get('name','')
        new_address = request.args.get('address', '')
        new_image_url = request.args.get('imageUrl', '')
        return jsonify(updateRestaurantByIdFromDB(id, new_name, new_address, new_image_url))

def addRestaurantToDB(data_dict):
    if type(data_dict) is not dict:
        raise Exception("ERROR: Can not add data due to format error!")

    query_result = session.query(Restaurant).filter_by(address = data_dict['restaurant_address']).first()
    print(query_result)
    if not query_result:
        new_restaurant = Restaurant(name = data_dict['restaurant_name'],
                                    address = data_dict['restaurant_address'],
                                    image_url = data_dict['restaurant_image'])
        session.add(new_restaurant)
        session.commit()
        print("{} Restaurant {} added.".format(new_restaurant.id,new_restaurant.name))
        return new_restaurant.serialize
    else:
        print("Restaurant {} not added, since it already exists.".format(data_dict['restaurant_name']))
        return query_result.serialize

def deleteAllRestaurants():
    session.query(Restaurant).delete()
    session.commit()
    return 'SUCESS'

def deleteRestaurantFromDB(id):
    if not id or type(id) is not int:
        raise Exception("ERROR: Wrong input format!")
    query_result = session.query(Restaurant).filter_by(id = id).first()
    if query_result:
        session.delete(query_result)
        return query_result.serialize
    else:
        return 'FAIL'

def getRestaurantByIdFromDB(id):
    if not id or type(id) is not int:
        raise Exception("ERROR: Wrong input format!")
    query_result = session.query(Restaurant).filter_by(id = id).first()
    if query_result:
        return query_result.serialize
    else:
        return 'FAIL'

def getAllRestaurantsFromDB():
    query_results = session.query(Restaurant).all()
    return [entity.serialize for entity in query_results]


def updateRestaurantByIdFromDB(id, name, address, image_url):
    if not id or type(id) is not int:
        raise Exception("ERROR: Wrong input format!")
    query_result = session.query(Restaurant).filter_by(id = id).first()
    if query_result:
        query_result.id = id
        if loaction:
            query_result.name = name
        if address:
            query_result.address = address
        if image_url:
            query_result.image_url = image_url
        session.update(query_result)
        session.commit()
        return query_result.serialize
    else:
        new_restaurant = Restaurant(id = id,
                                    name = name,
                                    address = address,
                                    image_url = image_url)
        session.add(new_restaurant)
        session.commit()
        return new_restaurant.serialize

if __name__ == '__main__':
    app.debug  = True
    app.config['JSON_SORT_KEYS'] = False
    app.run(host='0.0.0.0', port=5000)
