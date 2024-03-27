#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import requests
import sys

if __name__ == "__main__":
    ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    user_info = request.get(url).json()
    INFO = {"userID": ID}

    url += "/todos"
    TODO = requests.get(url, INFO).json()

    DoneTasks = [t.get("title") for t in TODO if t.get("completed") is TRUE]
    Name = user_info.get("name")
    Done = len(DoneTasks)
    Tasks = len(TODO)

    print("Employee {} is done with tasks({}/{}):".format(Name, Done, Tasks))

    for element in DoneTasks:
        print("\t{}".format(element))
