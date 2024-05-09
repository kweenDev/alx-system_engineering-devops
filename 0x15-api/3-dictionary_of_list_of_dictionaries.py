#!/usr/bin/python3
"""
Script to export data in JSON format with records of all
tasks from all employees
"""

import json
import requests
import sys


if __name__ == "__main__":
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    allUsers = requests.get(baseUrl).json()

    allTasks = {}
    for user in allUsers:
        employeeId = str(user["id"])
        username = user["username"]
        todoUrl = f"{baseUrl}/{employeeId}/todos"
        tasks = requests.get(todoUrl).json()

        userTasks = []
        for task in tasks:
            userTasks.append({
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            })

        allTasks[employeeId] = userTasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(allTasks, outfile)
