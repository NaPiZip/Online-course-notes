import httplib2
import json
import sys


if __name__=='__main__':
    print ("Running Endpoint Tester ...\n")
    address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':   ")
    if address == '':
        address = 'http://localhost:5000'

    print("Making a GET Request for /puppies....\n")
    try:
        url = address + '/puppies'
        h = httplib2.Http()
        resp, result = h.request(url, 'GET')
        if resp['status'] != '200':
            raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
    except Exception as err:
        print("Test 1 FAILED: Could not make GET Request to the web server")
        print(err.args)
    else:
        print("Test 1 PASS: Successfully made GET Request to /puppies")

    print("Making GET Request to /puppies/id ...\n")

    try:
        id = 1
        while id <=10:
            url = address + '/puppies/{}'.format(id)
            h = httplib2.Http()
            resp, result = h.request(url, 'GET')
            if resp['status'] !=  '200':
                raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
            id = id +1
    except Exception as err:
        print("Test 2 FAILED: Could not make GET Request to /puppies/id")
        print(err.args)
        sys.exit()
    else:
        print("Test 2 PASS: Successfully made GET Request to /puppies/id")
        print("All TESTS PASSED")
