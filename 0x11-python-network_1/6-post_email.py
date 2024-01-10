#!/usr/bin/python3
'''Module to post email'''
import requests
import sys


def post_email(url, email):
    '''Function to post email'''
    data = {'email': email}
    response = requests.post(url, data)
    html = response.text
    print(html)


if __name__ == "__main__":
    '''Post email'''
    post_email(sys.argv[1], sys.argv[2])
