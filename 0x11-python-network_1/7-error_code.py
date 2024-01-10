#!/usr/bin/python3
'''Module to handle http error'''
import requests
import sys


def handle_http_error(url):
    '''Function to handle http error'''
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except Exception:
        print('Error code:', response.status_code)


if __name__ == "__main__":
    '''Handle http errors'''
    handle_http_error(sys.argv[1])
