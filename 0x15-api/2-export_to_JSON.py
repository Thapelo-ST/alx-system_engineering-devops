#!/usr/bin/python3
"""
   This module uses a REST API to retrieve information about an employee's
   TODO list progress and exports it to a JSON file.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ gets employee todo progress and exports JSON format data"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get('id')
        username = user_data.get('username')

        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        user_tasks = []
        for task in todo_list:
            user_tasks.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })

        json_filename = "{}.json".format(user_id)
        with open(json_filename, 'w') as json_file:
            json.dump({user_id: user_tasks}, json_file, indent=4)

        print("Data exported to {}".format(json_filename))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
