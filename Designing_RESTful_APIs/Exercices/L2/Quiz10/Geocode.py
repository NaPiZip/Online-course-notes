'''
Geocode.py


This module is used to find a Geocode locataion based on a provided input string. The module is using the MapQuest API in order to query the location, for details see https://developer.mapquest.com/documentation/ .

Example:<br>
        obj = GeocodeLocation('api_key')
        coordinates = obj.getGeocodeLocation('Tokyo, Japan')

The return value is a dictionary of latitued and longitude coordinates.

        {'lat': 35.680071, 'lng': 139.768522}


Todo:
    * Implementing a proper unit test as well as a object based implementation of the function.
'''
import unittest
import json, requests

class GeocodeLocation(object):
    mapquest_key = ''
    mapquest_url = 'http://www.mapquestapi.com/geocoding/v1/address'
    status_code = dict(SUCESS = 0,
                   ERROR_WITH_INPUT = 400,
                   KEY_RELATED_ERROR = 403,
                   UNKNOWN_ERROR = 500)

    def __init__(self, key = ''):
        self.mapquest_key = key

    def getGeocodeLocation(self,address):
        if not address:
            return[]

        params = dict(key = self.mapquest_key,
                      location = address);

        response = requests.get(self.mapquest_url, params=params)
        if (response.status_code == requests.codes.ok):
            response_dict = json.loads(response.text)

            if(response_dict.get('info').get('statuscode') == self.status_code['SUCESS']):
               return (response_dict.get('results')[0].get('locations')[0].get('latLng'))
            else:
               return[]
        else:
            return[]

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.valid_key = 'MY_KEY'

    def test_empty_key_and_imput(self):
        obj = GeocodeLocation()
        self.assertEqual(obj.getGeocodeLocation(''),[])

    def test_empty_input(self):
        obj = GeocodeLocation(self.valid_key)
        self.assertEqual(obj.getGeocodeLocation(''),[])

    def test_empty_key(self):
        obj = GeocodeLocation('')
        self.assertEqual(obj.getGeocodeLocation('Spain'),[])

    def test_valid_location(self):
        obj = GeocodeLocation(self.valid_key)
        self.assertEqual(obj.getGeocodeLocation('Tokyo, Japan'),{'lat': 35.680071, 'lng': 139.768522})

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=1, exit=False)
