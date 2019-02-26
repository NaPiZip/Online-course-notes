import httplib2


import sys
import json




if __name__ == '__main__':
    h = httplib2.Http()
    h.add_credentials(r"Nawin",r"1234")
    resp = h.request('http://localhost:5000/','GET')
    print(resp)
