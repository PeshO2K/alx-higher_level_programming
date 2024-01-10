#!/usr/bin/python3
'''Module to post email'''
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


def handle_http_error(url):
    '''Function to post email'''
    req = Request(url)
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
    else:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    '''Handle http errors'''
    handle_http_error(sys.argv[1])
