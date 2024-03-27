#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import requests
import sys

if __name__ == "__main__":
    ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    url_todos = url + "/todos"

    user_info = request.get(url).json()
    todos_info = request.get(url_todos).json()

    Name = user_info.get("name")
    DoneTasks = [t.get("title") for t in todos_info if t.get("completed")]

    Done = len(DoneTasks)
    Tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".format(Name, Done, Tasks))

    for element in DoneTasks:
        print("\t{}".format(element))
