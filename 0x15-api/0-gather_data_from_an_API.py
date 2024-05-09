#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""

import sys
import requests


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


def display_employee_progress(user_data, todos_data):
    """
    Displays the employee's progress with tasks.

    Args:
        user_data (dict): User data fetched from the API.
        todos_data (list): TODO list data fetched from the API.
    """
    employee_name = user_data['name']
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)} /
                                                        {total_tasks}): ")
    for task in done_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py [employee_id]")
        sys.exit(1)

        try:
            employee_id = int(sys.argv[1])
        except ValueError:
            print("Error: Invalid employee ID. Please provide an integer ID.")
            sys.exit(1)

        user_data, todos_data = get_employee_info(employee_id)
        display_employee_progress(user_data, todos_data)
