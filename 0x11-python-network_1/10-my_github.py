#!/usr/bin/python3
'''Module to get github id'''
import requests
import sys


def get_github(username, password):
    '''Function to get github id'''
    url = ' https://api.github.com/user'
    data = (username, password)
    response = requests.get(url, auth=data)
    html = response.json()
    print(html.get('id'))


if __name__ == "__main__":
    '''get github id'''
    get_github(sys.argv[1], sys.argv[2])
