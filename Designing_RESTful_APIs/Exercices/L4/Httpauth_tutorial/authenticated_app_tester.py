from requests.auth import HTTPDigestAuth
import requests
import httplib2

if __name__ == '__main__':
    print ("Making a GET request authenticated / with requests...")
    url = 'http://localhost:5000/'
    resp = requests.get(url, auth=HTTPDigestAuth('Time', '1234'))

    if resp.status_code == requests.codes.ok:
        print("Test PASSED!")
    else:
        print("Test FAILED!")

    print(resp.request.headers)
    print(resp.request.body)
    try:
        print("Making a GET request authenticated / with httplib2 ...")
        httplib2.debuglevel = 1
        h = httplib2.Http(".cache")
        h.add_credentials('Time','1234')
        req,cont = h.request(url, 'GET')
        if req['status'] == '200':
            print("Success")
        else:
            print('Failed')
    except Exception as err:
            print(err.args)
