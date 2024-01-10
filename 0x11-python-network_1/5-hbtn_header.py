#!/usr/bin/python3
'''Module to fetch request id'''
import requests
import sys


def fetch_request_id(url):
    '''Function to fetch url'''
    header = "X-Request-Id"
    response = requests.get(url)
    req_id = response.headers.get(header)
    print(req_id)


if __name__ == "__main__":
    '''Get body response'''
    fetch_request_id(sys.argv[1])
