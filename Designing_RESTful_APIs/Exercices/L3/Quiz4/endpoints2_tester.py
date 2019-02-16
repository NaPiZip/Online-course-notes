import httplib2
import json
import sys


if __name__== '__main__':
    print("Running Endpoint Tester....\n")
    address = input("Please enter the address of the server ou want to access!")

    if address == '':
        address = 'http://localhost:5000'

    print("Making the GET Request for /puppies...")
    try:
        url = address + '/puppies'
        h = httplib2.Http()
        print(url)
        resp, result = h.request(url, 'GET')
        if resp['result'] != '200':
            raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
    except Exception as err:
        print("Test 1 FAILED: Could not make GET Request to web server")
        print(err.args)
    else:
        print("Test 1 PASS: Successfully made a GET Request to puppies")

    print("Making a POST Request to /puppies...")
    try:
        url = address + '/puppies'
        h = httplib2.Http()
        resp, result = h.request(url, 'POST')
        if resp['status'] != '200':
            raise Exception("Recieved an unsuccessful status code {}".format(resp['status']))
    except Exception as err:
        print("Test 2 FAILED: Could not make POST Request to web server")
        print(err.args)
        sys.exit()
    else:
        print("Test 2 PASS: Successfully made POST Request to /puppies")

    print("Making GET Request to /puppies/id")

    try:
        id = 1
        while id <=10:
            url = address + '/puppies/{}'.format(id)
            h = httplib2.Http()
            resp,result = h.request(url, 'GET')
            if resp['status'] != '200':
                raise Exception("Recieved an unsuccessful status code {}".format(resp['status']))
            id = id +1
    except Exception as err:
        print("Test 3 FAILED: Could not make GET Request to /puppies/id")
        print(err.args)
        sys.exit()
    else:
        print("Test 3 PASS: Successfully made GET Request to /puppies/id")

    print("Making PUT Request to /puppies/id")

    try:
        id = 1
        while id <=10:
            url = address + '/puppies/{}'.format(id)
            h = httplib2.Http()
            resp,result = h.request(url, 'PUT')
            if resp['status'] != '200':
                raise Exception("Recieved an unsuccessful status code {}".format(resp['status']))
            id = id +1
    except Exception as err:
        print("Test 4 FAILED: Could not make PUT Request to /puppies/id")
        print(err.args)
    else:
        print("Test 4 PASSED: Successfully made a PUT Request to /puppies/id")

    print("Making DELETE Request to puppies/id")

    try:
        id = 1
        while id<=10:
            url = address + '/puppies/{}'.format(id)
            h = httplib2.Http()
            resp,result = h.request(url, 'DELETE')
            if resp['status'] != '200':
                raise Exception("Recieved an unsuccessful status code {}".format(resp['stauts']))
            id = id +1
    except Exception as err:
        print("Test 5 FAILED: Could not make a DELETE Request to /puppies/id")
        print(err.args)
    else:
        print("Test 5 PASS: Successfully made a DELETE Request to /puppies/id")

    print("HURRAY, ALL TEST PASSED!!")
