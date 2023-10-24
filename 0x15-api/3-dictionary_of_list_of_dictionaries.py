#!/usr/bin/python3
"""
   This module uses a REST API to retrieve information about all employees' TODO
   list progress and exports it to a JSON file.
"""

import requests
import json


def get_all_employee_todo_progress():
    """
        This module uses a REST API to retrieve information
        about all employees' TODO list progress and exports it to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_employee_data = {}

        for user in users_data:
            user_id = user.get('id')
            username = user.get('username')

            todo_url = "{}/todos?userId={}".format(base_url, user_id)
            todo_response = requests.get(todo_url)
            todo_list = todo_response.json()

            user_tasks = []
            for task in todo_list:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

            all_employee_data[user_id] = user_tasks

        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_employee_data, json_file, indent=4)

        print("Data exported to {}".format(json_filename))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    get_all_employee_todo_progress()
