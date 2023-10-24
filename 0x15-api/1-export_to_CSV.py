#!/usr/bin/python3
"""
   This module uses a REST API to retrieve information about an employee's
   TODO list progress and exports it to a CSV file.
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ gets the employee to do progress but modified"""
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

        total_tasks = len(todo_list)
        completed_tasks = sum(1 for task in todo_list if task['completed'])

        print("Employee {} is done with tasks ({}/{}):"
              .format(username, completed_tasks, total_tasks))
        for task in todo_list:
            if task['completed']:
                print("\t{}".format(task['title']))

        csv_filename = "{}.csv".format(user_id)
        with open(csv_filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME",
                                 "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todo_list:
                csv_writer.writerow([user_id, username,
                                     task['completed'], task['title'])

        print("Data exported to {}".format(csv_filename))

    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
