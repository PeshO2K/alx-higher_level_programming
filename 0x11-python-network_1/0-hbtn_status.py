#!/usr/bin/python3
'''Module the fetches https://alx-intranet.hbtn.io/status'''
import urllib.request


def fetch_url():
    '''Function to fetch url'''
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    '''Get body response'''
    fetch_url()
