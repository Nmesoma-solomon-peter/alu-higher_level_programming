#!/usr/bin/python3
"""Fetches a URL and displays its content."""

import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf-8 content:", content.decode("utf-8"))

