import httplib2


import sys
import json




if __name__ == '__main__':
    h = httplib2.Http()
    h.add_credentials(b"Nawin",b"1234")
    resp = h.request('http://localhost:5000/','GET')
    print(resp)
