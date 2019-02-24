import httplib2
import sys

def MakeRequestToUrl(url, request_type):
    if not url and type(url) is not str:
        raise Exception("Error wrong input: Please enter string as url!")
        return
    if type(request_type) is not str:
        raise Exception("Error wrong input: Please enter a string as request type!!")
        return
    try:
        print("Trying to make a {} Request to {}".format(request_type, url))
        h = httplib2.Http()
        resp,req = h.request(url, method=request_type)
        if resp['status'] != '200':
            raise Exception("Recieved an unsuccessful status code of {}".format(resp['status']))
    except Exception as err:
        print("Test FAILED: Could not make GET Request to url {}.".format(url))
        print(err.args)
    else:
        print("Test PASS: Successfully made a GET Request to {}.".format(url))


if __name__ == '__main__':
    print("Running mashup tester file!")
    address = 'http://localhost:5000'
    MakeRequestToUrl(address + '/restaurants', 'GET')
    #assert(False), "Shit happend"
