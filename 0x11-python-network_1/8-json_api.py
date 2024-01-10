#!/usr/bin/python3
'''Module to post letter'''
import requests
import sys


def post_letter(letter=""):
    '''Function to post letter'''
    url = 'http://0.0.0.0:5000/search_user'
    lett = {'q': letter}
    response = requests.post(url, data=lett)
    try:
        html = response.json()
        if html:
            print("[{}] {}".format(html.get('id'), html.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    '''Post letter'''
    post_letter(sys.argv[1] if len(sys.argv) > 1 else "")
