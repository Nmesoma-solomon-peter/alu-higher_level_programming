#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    import urllib.request
    
    username = "ed757ca7f0b2"
    password = "1251b956dca70ce1b90a"

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status', auth=HTTPBasicAuth(username, password)) as response: 
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8", "replace")))
