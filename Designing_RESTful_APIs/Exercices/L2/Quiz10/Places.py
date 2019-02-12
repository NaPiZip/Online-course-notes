'''
Places.py


This module is used to find a Place arround the provided latitudinal and longitudinal coordinates. The module is using the Foursquare API in order to query the venue, for details see https://developer.foursquare.com/docs/api .  

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

class VenueSearch(object):
    client_id = ''
    client_secret = ''
    url = 'https://api.foursquare.com/v2/venues/search'
    status_code=[]
       
    def __init__(self, id = '', secret = ''):
        self.client_id = id
        self.client_secret = secret
        self.status_code = dict(SUCESS = 200)
        
    def getVenueInfo(self, location, food):
        if type(location) is not dict:
            return[]
        elif location.get('lat') == None or \
             location.get('lng') == None:
            return[]
        
        params = dict(client_id=self.client_id,
                      client_secret= self.client_secret,
                      v='20180323',
                      ll="{},{}".format(location['lat'],location['lng']),
                      query='coffee',
                      limit=1
                    )
        
        response = requests.get(self.url, params=params) 
        if (response.status_code == requests.codes.ok):
            response_dict = json.loads(response.text)
            if(response_dict.get('meta').get('code') == self.status_code['SUCESS']):
                return response_dict.get('response').get('venues')[0]
            else:
               return[]        
        else:
            return[]  
        
class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.client_id = ''
        self.client_secret = ''
    
    def test_empty_key_and_imput(self):
        obj = VenueSearch()        
        self.assertEqual(obj.getVenueInfo('',''),[])
        
    def test_empty_imput(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)        
        self.assertEqual(obj.getVenueInfo('',''),[])
    
    def test_no_valid_location_type(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)         
        self.assertEqual(obj.getVenueInfo(dict(banana=1),'pizza'),[])
        
    def test_valid_call(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)           
        self.assertEqual(obj.getVenueInfo({'lat': 35.680071, 'lng': 139.768522},'pizza').get('id'), '597185d60802d42bc89acd2f') 
        
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=3, exit=False)