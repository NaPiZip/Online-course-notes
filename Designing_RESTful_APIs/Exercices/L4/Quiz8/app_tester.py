from urllib.parse import urlencode
from httplib2 import Http
import json
import sys
import base64
import httplib2
import requests
from requests.auth import HTTPDigestAuth

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

    try:
        h = Http('.cache')
        httplib2.debuglevel = 1
        h.follow_all_redirects = True
        h.add_credentials('Peter','Pan')
        url = address + '/resource'
        resp,content = h.request(url, 'GET')
        print(resp['status'])
        print(resp.reason)
        print(content)
    except Exception as err:
        print(err.args)

    try:
        url = address + '/resource'
        resp = requests.get(url, auth=HTTPDigestAuth('Peter', 'Pan'))
        print(resp.request.headers)
        print(resp.request.body)
        print("Recieved status code {}".format(resp.status_code))
    except Exception as err:
        print(err.args)
