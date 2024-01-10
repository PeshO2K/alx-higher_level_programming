#!/usr/bin/python3
'''Module the fetches https://alx-intranet.hbtn.io/status'''
import requests


def fetch_status():
    '''Function to fetch url'''
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url).text

    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))


if __name__ == "__main__":
    '''Get body response'''
    fetch_status()
