import httplib2
import json
import sys


if __name__== '__main__':
    print("Running Endpoint Tester....\n")
    address = input("Please enter the address of the server ou want to access!")

    if address == '':
        adress = 'http://localhost:5000'

    print("Making the GET Requset for /puppies...")

    try:
        url = adress + '/puppies'
        h = httplib2.Http()
        resp, result = h.request(url, 'GET')
        if resp['result'] != '200':
            raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
    except Exception as err:
        print("Test 1 FAILED: Could not mak GET Request to web server")
        print("{}".format(err.args))
    else:
        print("Test 1 PASS: Successfully made a GET Request to puppies")
