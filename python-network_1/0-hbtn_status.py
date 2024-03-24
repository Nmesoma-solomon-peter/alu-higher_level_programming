#!/usr/bin/python3
"""A script that
- fetches https://alu-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as res:
        custom_status = b'Custom status'
        print("Body response:")
        print("\t- type: {}".format(type(custom_status))
        print("\t- content: {}".format(custom_status))
        print("\t- utf8 content: {}".format(custom_status.decode('utf-8')))
