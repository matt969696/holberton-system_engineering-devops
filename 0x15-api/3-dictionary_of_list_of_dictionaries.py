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
    listemp = requests.get(site).json()
    myDict = {}
    with open("todo_all_employees.json", 'w') as outfile:
        for employee in listemp:
            taskl = requests.get(site + str(employee["id"]) + "/todos").json()
            mylist = []

            for task in taskl:
                taskdic = {"task": task['title'],
                           "completed": task['completed'],
                           "username": employee["username"]}
                mylist.append(taskdic)

            json.dump({employee["id"]: mylist}, outfile)


if __name__ == "__main__":
    main()
