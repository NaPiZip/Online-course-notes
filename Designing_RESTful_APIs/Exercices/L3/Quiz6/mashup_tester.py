import httplib2
import sys
import json

def makeRequestToUrl(url, request_type):
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
        return req
    except Exception as err:
        print("Test FAILED: Could not make GET Request to url {}.".format(url))
        print(err.args)

def evaluateRequest(address, method, predicate):
    request = makeRequestToUrl(address , method)
    assert(eval(predicate)), "Test FAILED: No successful {} Request to {}".format(method,address)
    print("Test PASS: Successfully made a {} Request to {}".format(method,address))

if __name__ == '__main__':
    print("Running mashup tester file!")
    address = 'http://localhost:5000'

    evaluateRequest(address + '/restaurants', 'DELETE',
                    "json.loads(request) == 'SUCESS'")

    evaluateRequest(address + '/restaurants?location=New+York&mealType=Steak', 'POST',
                    "json.loads(request)['id']!= None")

    evaluateRequest(address + '/restaurants?location=Ann+Arbor&mealType=Indian', 'POST',
                    "json.loads(request)['id']!= None")

    evaluateRequest(address + '/restaurants', 'GET',
                "len(json.loads(request)[0]) >=1")

    evaluateRequest(address + '/restaurants/99', 'GET',
                    "json.loads(request) == 'FAIL'")

    evaluateRequest(address + '/restaurants/1', 'GET',
                    "json.loads(request)['id'] == 1")

    evaluateRequest(address + '/restaurants/1', 'DELETE',
                    "json.loads(request)['id'] == 1")

    evaluateRequest(address + '/restaurants/1', 'DELETE',
                    "json.loads(request) == 'FAIL'")

    evaluateRequest(address + '/restaurants/1?name=Doener&address=Sersheim+GER&imageUrl=www.google.de', 'UPDATE',
                    "json.loads(request)['name'] == 'Doener'")

    print("ALL TESTS PASSED!!!")
