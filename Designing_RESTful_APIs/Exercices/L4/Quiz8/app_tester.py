from urllib.parse import urlencode
from httplib2 import Http
import json
import sys
import base64

if __name__ == '__main__':
    print("Running Endpoint Tester ...\n")
    address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")

    if address is '':
        address = 'http://localhost:5000'

    try:
        h = Http()
        url = address + '/users'
        data = json.dumps(dict(username="Peter", password="Pan"))
        resp, content = h.request(url, 'POST', body = data, headers = {"Content-Type":"application/json"})
        if resp['status'] != '201' and resp['status'] != '200':
            raise Exception('Recieved an unsuccessful status code of {}'.format(resp['status']))
    except Exception as err:
        print("Test 1 FAILED: Could not make a new user")
        print(err.args)
        sys.exit()
    else:
        print("Test 1 PASS: Successfully mate a new user")
