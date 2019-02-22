import httplib2
import sys


if __name__ == '__main__':
    print("Running mashup tester file!")
    address = 'http://localhost:5000'
    try:
        url = address + '/restaurants'
        h = httplib2.Http()
        resp,req = h.request(url=url, method='GET')

        if resp['status'] != '200':
            raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
    except Exception as err:
        print("Test 1 FAILED: Could not make GET Request to web server")
        print(err.args)
    else:
        print("Test 1 PASS: Successfully made a GET Request to puppies")
