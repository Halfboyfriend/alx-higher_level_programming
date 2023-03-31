#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    arg = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": arg}

    response = requests.post(url="http://0.0.0.0:5000/search_user", data=arg)
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print('Not a valid JSON')

