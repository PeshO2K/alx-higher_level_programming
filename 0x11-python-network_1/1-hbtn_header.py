#!/usr/bin/python3
'''Module to fetch request id'''
import urllib.request
import sys


def fetch_request_id(url):
    '''Function to fetch url'''
    header = "X-Request-Id"
    with urllib.request.urlopen(url) as response:
        html = response.getheader(header)
        print(html)


if __name__ == "__main__":
    '''Get body response'''
    fetch_request_id(sys.argv[1])
