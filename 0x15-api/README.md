# Python Scripts for API Interaction and JSON Export
### 0x15-api

This project contains Python scripts for interacting with APIs, processing JSON data, and exporting data to JSON format. The tasks are based on the JSONPlaceholder API and involve retrieving and processing task data for users.

## Table of Contents

- [Tasks Overview](#tasks-overview)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [How to Run](#how-to-run)
- [Task Descriptions](#task-descriptions)
	- [Task 0](#task-0)
	- [Task 1](#task-1)
	- [Task 2](#task-2)
	- [Task 3](#task-3)
- [Author](#author)

# Tasks Overview

The project covers the following tasks:
- Task 0: Pythjon script to gather data from an API and export it to JSON format.
- Task 1: Python script to gather data from an API and filter it based on user ID, then export to JSON format.
- Task 2: Python script to gather data from an API and export it to JSON format with records filtered based on user ID.
- Task 3: Python script to gather data from an API and export it to JSON format with records of all tasks from all employees.

## Project Structure
```bash
	0x15-api/
		- 0-gather_data_from_an_API.py
		- 1-export_to_CSV.py
		- 2-export_to_JSON.py
		- 3-dictionary_of_list_dictionaries.py
		- README.md
```

## Dependencies

- Python 3.x
- requests library (for making HTTP requests)

Install the `requests` library using pip3:

```bash
pip3 install requests
```

## How to Run
1. Clone the repository to your local machine:
```bash
git clone https://github.com/kweendev/alx-system_engineering-devops/0x15-api.git
```

2. Navigate to the project directory:
```bash
cd alx-system_engineering-devops/0x15-api
```

3. Run each script individually based on the task requirements:
```bash
python3 0-gather_data_from_an_API.py
python3 1-export_to_CSV.py
python3 2-export_to_JSON.py
python3 3-dictionary_of_list_dictionaries.py
```

## Task Descriptions
### Task 0
- Script: `0-gather_data_from_an_API.py`
- Description: Python script to gather data from the JSONPlaceholder API regarding a specified employee ID and export it to JSON format.
- Output: Creates a JSON file named `todo_all_employees.json` containing tasks for the specified user.

### Task 1
- Script: `1-export_to_CSV.py`
- Description: Python script to gather data from the JSONPlaceholder API regarding a specified employee ID, filter the data, and export it to CSV format.
- Output: Creates a CSV file named `USER_ID.csv` containing tasks for the specified user.

### Task 2
- Script: `2-export_to_JSON.py`
- Desription: Python script to gather data from the JSONPlaceholder API regarding all employee IDs and export it to JSON format.
- Output: Creates a JSON file named `todo_all_employees.json` containing tasks for all users.

### Task 3
- Script: `3-dictionary_of_list_dictionaries.py`
- Description: Python script to gather data from the JSONPlaceholder API regarding all employee IDs, organise tasks by user ID in a dictionary of lists of dictionaries, and export it to JSON format.
- Output: Creates a JSON file named `todo_all_employees.json` containing tasks for all users in a structured format.

## Author
Refiloe Radebe (_kweenDev_)
