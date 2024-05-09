#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format"""

import sys
import requests
import csv


def get_employee_info(employee_id):
    """
    Fetches employee information and TODO list from the API.

    Args:
        employee_id (int): The ID of the employee.

        Returns:
            tuple: A tuple containing user data (dict) and todos data (list).
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Failed to fetch data from the API.")
        sys.exit(1)

        user_data = user_response.json()
        todos_data = todos_response.json()

        return user_data, todos_data


def export_to_csv(user_data, todos_data):
    """
    Exports data to CSV format.

    Args:
        user_data (dict): User data fetched from the API.
        todos_data (list): TODO list data fetched from the API.
    """
    employee_id = user_data['id']
    employee_name = user_data['name']
    csv_filename = f'{employee_id}.csv'

    with open(csv_filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
                    'USER_ID',
                    'USERNAME',
                    'TASK_COMPLETED_STATUS',
                    'TASK_TITLE'
                    ])

        for task in todos_data:
            csvwriterow([
                employee_id,
                employee_name,
                str(task['completed']),
                task['title']
                ])

            print(f"Data exported to {csv_filename}")


if __name__ = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py[employee_id]")
        sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Error: Invalid employee ID. Please provide an integer ID.")
            sys.exit(1)

    user_data, todos_data = get_employee_info(employee_id)
    export_to_csv(user_data, todos_data)
