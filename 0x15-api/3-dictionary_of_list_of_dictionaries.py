#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
from sys import argv


def main():
    """main function"""

    usersUrl = "https://jsonplaceholder.typicode.com/users/"

    usersReq = requests.get(usersUrl)
    users = json.loads(usersReq.text)

    masterDict = {}
    for user in users:
        todoUrl = ("https://jsonplaceholder.typicode.com/"
                   "users/{:s}/todos".format(str(user['id'])))
        todoReq = requests.get(todoUrl)
        todo = json.loads(todoReq.text)

        taskList = []
        for task in todo:
            formattedTask = {"task": task['title'],
                             "completed": task['completed'],
                             "username": user['username']}
            # print(formattedTask)
            taskList.append(formattedTask)
        masterDict.update({user['id']: taskList})

    masterJSON = json.dumps(masterDict)
    with open("todo_all_employees.json", "w") as file:
        file.write(masterJSON)


if __name__ == "__main__":
    main()
