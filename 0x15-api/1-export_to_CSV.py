#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import csv
import requests
import sys


if __name__ == "__main__":
    ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    url_todos = url + '/todos'

    user_info = requests.get(url).json()
    todos_info = requests.get(url_todos).json()

    Name = user_info.get("username")

    filename = "{}.csv".format(ID)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for t in todos_info:
            comp_status = t.get("completed")
            writer.writerow([ID, Name, comp_status, t.get("title")])
