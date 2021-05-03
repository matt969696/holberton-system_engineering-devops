#!/usr/bin/python3
"""
Module that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


def main():
    """ Returns employee information TODO """
    site = "https://jsonplaceholder.typicode.com/users/"
    empl = requests.get(site + sys.argv[1]).json()['username']
    taskl = requests.get(site + sys.argv[1] + "/todos").json()
    with open(sys.argv[1] + '.json', 'w') as outfile:
        mylist = []

        for task in taskl:
            taskdic = {"task": task['title'],
                       "completed": task['completed'],
                       "username": empl}
            mylist.append(taskdic)
        json.dump({sys.argv[1]: mylist}, outfile)


if __name__ == "__main__":
    main()
