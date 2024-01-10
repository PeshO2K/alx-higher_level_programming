#!/usr/bin/python3
import urllib.request as urlreq
'''Module the fetches https://alx-intranet.hbtn.io/status'''


def fetch_url():
    '''Function to fetch url'''
    with urlreq.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html.decode('utf-8')))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_url()
