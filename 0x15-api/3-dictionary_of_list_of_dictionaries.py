#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users_url = url + '/users'

    user_info = requests.get(users_url).json

    All_user_data = {}

    for user in user_info:
        user_id = user["id"]
        user_url = users_url + "/{}/todos".format(user_id)
        todo_list = requests.get(user_url).json()

        All_user_data[user_id] = [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user.get("username")
            }
            for t in todo_list
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(All_user_data, jsonfile, indent=4)
