#!/usr/bin/python3
"""
Script to export data in JSON format with records of all
tasks from all employees
"""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()

    # Create a dictionary to store tasks by user ID
    tasks_by_user = {}

    for task in data:
        task_entry = {
                "username": task["username"],
                "task": task["titke"],
                "completed": task["completed"]
                }

        # Check if user ID already exists in dictionary
        if task["userId"] in tasks_by_user:
            tasks_by_user[task["userId"]].append(task_entry)
        else:
            tasks_by_user[task["userId"]] = [task_entry]

    # Export data to JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks_by_user, file)
