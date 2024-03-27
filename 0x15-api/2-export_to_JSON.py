#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import json
import requests
import sys


if __name__ == "__main__":
    ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    url_todos = url + '/todos'

    user_info = requests.get(url).json()
    todos_info = requests.get(url_todos).json()

    Name = user_info.get("username")

    User_Data = {
        ID: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": Name
            }
            for t in todos_info
        ]
    }

    filename = "{}.json".format(ID)
    with open(filename, "w") as jsonfile:
        json.dump(User_Data, jsonfile, indent=4)
