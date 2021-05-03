#!/usr/bin/python3
"""
Module that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import csv
import requests
import sys


def main():
    """ Returns employee information TODO """
    site = "https://jsonplaceholder.typicode.com/users/"
    empl = requests.get(site + sys.argv[1]).json()['username']
    json = requests.get(site + sys.argv[1] + "/todos").json()

    with open("{}.csv".format(sys.argv[1]), 'w') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in json:
            row = [task['userId'], empl, task['completed'], task['title']]
            write.writerow(row)


if __name__ == "__main__":
    main()
