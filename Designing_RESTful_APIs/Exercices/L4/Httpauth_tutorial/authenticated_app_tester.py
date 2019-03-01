from requests.auth import HTTPDigestAuth
import requests

if __name__ == '__main__':

     print ("Making a GET request to authenticated /...")
     url = 'http://localhost:5000/'
     resp = requests.get(url, auth=HTTPDigestAuth('Time', '1234'))
     if resp.status_code == requests.codes.ok:
         print("Test PASSED!")
     else:
        print("Test FAILED!")
