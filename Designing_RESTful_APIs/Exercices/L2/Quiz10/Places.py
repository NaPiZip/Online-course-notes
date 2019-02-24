'''
Places.py


This module is used to find a Place arround the provided latitudinal and longitudinal coordinates. The module is using various Foursquare API's in order to query venue's or photos of venue's, for details see https://developer.foursquare.com/docs/api .


Example getVenueInfoDict:<br>
        obj = VenueSearch(client_id='ID' ,client_secret='secret' )
        information_dict = obj.getVenueInfoDict({'lat': 35.680071, 'lng': 139.768522}, 'Pizza')

The return value is a dictionary containing information about the query result.

Example getVenuePhotoUrl:<br>
        obj = VenueSearch(client_id='ID' ,client_secret='secret' )
        image_url = obj.getVenuePhotoUrl('597185d60802d42bc89acd2f')

The return value is a url of the first found photo of the venue query result.


Todo:
    * Add return values for more information of what went wrong during a api call.
'''
import unittest
import json, requests

class VenueSearch(object):
    client_id = ''
    client_secret = ''
    url = 'https://api.foursquare.com/v2/venues/'
    status_code=[]
    image_size='300x300'

    def __init__(self, id = '', secret = ''):
        self.client_id = id
        self.client_secret = secret
        self.status_code = dict(SUCESS = 200)

    def getVenueInfoDict(self, location, food):
        if type(location) is not dict:
            return[]
        elif location.get('lat') == None or \
             location.get('lng') == None:
            return[]

        params = dict(client_id=self.client_id,
                      client_secret= self.client_secret,
                      v='20180323',
                      ll="{},{}".format(location['lat'],location['lng']),
                      query=food,
                      limit=1)

        response = requests.get(self.url+'search', params=params)
        if (response.status_code == requests.codes.ok):
            response_dict = json.loads(response.text)
            if(response_dict.get('meta').get('code') == self.status_code['SUCESS']):
                return response_dict.get('response').get('venues')[0]
            else:
                return[]
        else:
            return[]

    def getVenuePhotoUrl(self, venue_id):
        if type(venue_id) is not str or not venue_id:
            return[]

        params = dict(client_id=self.client_id,
                      client_secret= self.client_secret,
                      v='20180323',
                      limit=1)

        response = requests.get(self.url+ venue_id+'/photos?', params=params)
        if(response.status_code == requests.codes.ok):
            response_dict = json.loads(response.text)

            if(response_dict.get('response').get('photos').get('count') != 0):
                prefix = response_dict.get('response').get('photos').get('items')[0].get('prefix')
                suffix = response_dict.get('response').get('photos').get('items')[0].get('suffix')
                return prefix + self.image_size + suffix
            else:
                return []
        return []

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.client_id = ''
        self.client_secret = ''

    # getVenueInfo api test
    def test_getVenueInfo_empty_key_and_input(self):
        obj = VenueSearch()
        self.assertEqual(obj.getVenueInfoDict('',''),[])

    def test_getVenueInfo_empty_imput(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenueInfoDict('',''),[])

    def test_getVenueInfo_no_valid_dictionary(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenueInfoDict('','pizza'),[])

    def test_getVenueInfo_no_valid_location_type(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenueInfoDict(dict(banana=1),'pizza'),[])

    def test_getVenueInfo_valid_call(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenueInfoDict({'lat': 35.680071, 'lng': 139.768522},'pizza').get('id'), '4b85ba2bf964a520666f31e3')

    # getVenuePhoto api test
    def test_getVenuePhoto_empty_venue_id(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenuePhotoUrl(''),[])

    def test_getVenuePhoto_wrong_venue_id_type(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenuePhotoUrl(54),[])

    def test_getVenuePhoto_valid_call(self):
        obj = VenueSearch(id=self.client_id, secret=self.client_secret)
        self.assertEqual(obj.getVenuePhotoUrl('4b85ba2bf964a520666f31e3'),'https://fastly.4sqi.net/img/general/300x300/25792726_zrv8o6q_RXhJSr3DpdMblFJqSYamLRSEEJb6EIhmWn4.jpg')


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=1, exit=False)
