#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def main():
    """main function"""
    if len(argv) < 2:
        return

    userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todoUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    userReq = requests.get(userUrl)
    user = json.loads(userReq.text)
    todoReq = requests.get(todoUrl)
    todo = json.loads(todoReq.text)

    numTasks = len(todo)
    numComplete = 0
    for task in todo:
        if task['completed']:
            numComplete += 1

    print("Employee {} is done with tasks({}/{}):".format(user['name'],
                                                          numComplete,
                                                          numTasks))
    for task in todo:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    main()
