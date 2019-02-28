from requests.auth import HTTPDigestAuth
import requests

if __name__ == '__main__':
     url = 'http://localhost:5000/'
     requests.get(url, auth=HTTPDigestAuth('Time', '1234'))
