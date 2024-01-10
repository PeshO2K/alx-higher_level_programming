#!/usr/bin/python3
'''Module to post email'''
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    '''Function to post email'''
    email = urllib.parse.urlencode({'email': email})
    email = email.encode('ascii')
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    '''Post email'''
    post_email(sys.argv[1], sys.argv[2])
