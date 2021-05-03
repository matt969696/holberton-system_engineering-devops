#!/usr/bin/python3
"""
Task 0
"""
import requests
import sys


def main():
    """ Returns employee information TODO """
    site = "https://jsonplaceholder.typicode.com/users/"
    empl = requests.get(site + sys.argv[1]).json()['name']

    json = requests.get(site + sys.argv[1] + "/todos").json()
    nb = len(json)
    c = sum(task.get('completed') is True for task in json)
    print("Employee {} is done with tasks({}/{}):".format(empl, c, nb))

    for task in json:
        if task.get('completed') is True:
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
