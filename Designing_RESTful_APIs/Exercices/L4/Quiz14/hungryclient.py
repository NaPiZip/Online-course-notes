from __future__ import division
from time import sleep
import json
import requests

def SendRequests(url, requests_per_minute):
    print("Sending requests ...")
    requests_send = 0
    while requests_send < requests_per_minute:
        response = requests.get(url)

        if response.status_code is not requests.codes.ok:
            data = response.json()
            print("Error {} : {}".format(data['error'], data['data']))
            print("Hit rate limit waiting 5 seconds.")
            sleep(5)
        else:
            print("Number of request: {}".format(requests_send))
            #print(response.text)
        requests_send += 1
        sleep(interval)

if __name__ == '__main__':

    url = input("Please enter uri ypu want to access, \n If left blank the connection will be set to 'http://localhost:5000/catalog: ")

    if url is '':
        url = 'http://localhost:5000/catalog'

    requests_per_minute  = float(input("Please specify the number of requests per minute: ") or 1)


    interval = 60 / requests_per_minute


    SendRequests(url, requests_per_minute)
