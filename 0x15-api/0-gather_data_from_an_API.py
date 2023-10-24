#!/usr/bin/python3
"""
    this module using this REST API, for a given employee ID,
    returns information about his/her to-do list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
        this function is the rest api to gather data
    """
    # Define the API URL
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # fetch user's todo list
        todo_response = requests.get(todo_url)
        todo_list = todo_response.json()

        # calculate progress
        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])

        # display the progress information
        print("Employee {} is done with tasks ({}/{}):".format(
            employee_name, completed_tasks, total_tasks))
        for task in todo_list:
            if task['completed']:
                print("\t{}".format(task['title']))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
