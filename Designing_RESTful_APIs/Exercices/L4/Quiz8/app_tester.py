from urllib.parse import urlencode
import json
import sys
import base64
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    print("Running Endpoint Tester ...\n")
    address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")

    if address is '':
        address = 'http://localhost:5000'
    print("TEST 1: Try to register a new user")
    try:
        url = address + '/users'
        data = dict(username='nawin',password='Huh?')
        resp = requests.post(url, data =json.dumps(data), headers = {"Content-Type":"application/json"})
        if resp.status_code != requests.codes.ok:
            raise Exception("Recieved an unsuccessful status code of {}".format(resp.status_code))
    except Exception as err:
        print("Test 1 FAILED: Could not make a new user")
        print(err.args)
        sys.exit()
    else:
        print("Test 1 PASS: Successfully made a new user")
    print("TEST 2: Obtain a token")
    try:
        url = address + '/token'
        resp = requests.get(url, headers = {"Content-Type":"application/json"}, auth=HTTPBasicAuth('nawin','Huh?'))
        if resp.status_code != requests.codes.created:
            raise Exception("Recieved an unsuccessful status code of {}".format(resp.status_code))
        new_content = resp.json()
        if new_content['token'] is None:
            raise Exception("No token recieved!")
        else:
            token = new_content['token']
    except Exception as err:
        print(err.args)
        sys.exit()
    else:
        print("Test 2 PASS: Successfully request a token")

    print("TEST 3: Try to add products to the database")
    try:
        url = address + '/products'
        data = dict(name = 'apple', category = 'fruit', price = '$0.99')
        resp = requests.post(url, data = json.dumps(data),  headers = {"Content-Type":"application/json"}, auth=HTTPBasicAuth(token,''))
        if resp.status_code != requests.codes.created:
            raise Exception("Recieved an unsuccessful status code of {}".format(resp.status_code))

        for key in resp.json():
            if data[key] == None:
                raise Exception("Error JSON return keys not matching")

    except Exception as err:
        print("TETS 3 FAILED: Could not add new products")
        print(err.args)
        sys.exit()
    else:
        print("TEST 3 PASSED: Successfully added a new product")

    print("TEST 4: Accessing endpoint with invalid token")
    try:
        url = address + '/products'
        resp = requests.get(url, headers = {"Content-Type":"application/json"}, auth = HTTPBasicAuth("loqwjdajfdo2r",''))
        if resp.status_code != requests.codes.unauthorized:
            raise Exception("Recieved a wrong status code of {} instead of 401".format(resp.status_code))
    except Exception as err:
        print("TEST 4 FAILED: Could not make request in order to access endpoint")
        print(err.args)
        sys.exit()
    else:
        print("TEST 4 PASSED: Prevented accessing endpoint with invalid token")

    print("TEST 5: View all products")
    try:
        url = address + '/products'
        resp = requests.get(url, headers = {"Content-Type":"application/json"}, auth = HTTPBasicAuth(token,''))
        if resp.status_code != requests.codes.ok:
            raise Exception("Recieved a wrong status code of {} ".format(resp.status_code))
        for key in resp.json().get('products')[0]:
            if data[key] == None:
                raise Exception("Error JSON return keys not matching")

    except Exception as err:
        print("TEST 5 FAILED: Could not view all products")
        print(err.args)
        sys.exit()
    else:
        print("TEST 5 PASSED: Could view all product")

    print("TEST 6: View specific category of products")
    try:
        url = address + '/products/fruit'
        resp = requests.get(url, headers = {"Content-Type":"application/json"}, auth = HTTPBasicAuth(token,''))
        if resp.status_code != requests.codes.ok:
            raise Exception("Recieved a wrong status code of {} ".format(resp.status_code))
        for key in resp.json().get('products')[0]:
            if data[key] == None:
                raise Exception("Error JSON return keys not matching")
    except Exception as err:
        print("TEST 6 FAILED: View specific category of products")
        print(err.args)
        sys.exit()
    else:
        print("TEST 6 PASSED: View specific category of products")

    print("TEST 7: Try to view added user")
    try:
        url = address + '/users/1'
        resp = requests.get(url)
        if resp.status_code != requests.codes.ok:
            raise Exception("Recieved a wrong status code of {} ".format(resp.status_code))
        if resp.json().get('username') != 'nawin':
            raise Exception("Could not find user nawin")
    except Exception as err:
        print("TEST 7 FAILED: Try to view added user")
        print(err.args)
    else:
        print("TEST 7 PASSED: Try to view added user")
