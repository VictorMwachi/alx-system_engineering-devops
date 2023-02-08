#!/usr/bin/python3
"""Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    site_url = 'https://jsonplaceholder.typicode.com/'
    to_do_url = site_url + f"user/{argv[1]}/todos"
    name_url = site_url + f"users/{argv[1]}"
    emp_dict = get(name_url).json()
    to_do_dict = get(to_do_url).json()
    name = emp_dict.get('name')
    total_tasks = len(to_do_dict)
    tasks_done = sum([i['completed'] for i in to_do_dict])
    print("Employee {} is done with tasks({}/{}):"
          .formart(name, tasks_done, total_tasks))
    for task in to_do_dict:
        if task.get('completed'):
            print('\t {}'.formart(task['title']))
