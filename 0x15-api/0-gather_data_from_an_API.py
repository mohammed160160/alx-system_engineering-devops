#!/usr/bin/python3
"""THIS IS A DESCRIPTION"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    ID = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(ID)
    REQUEST = requests.get(url)
    to_do = REQUEST.json()

    name = to_do[0]['name']
    done_tasks = [td for td in to_do if td['completed']]
    t_num = len(to_do)
    d_num = len(done_tasks)
    print("Employee {} is done with tasks({}/{})".format(name, dnum, tnum))

    for taskname in done_tasks:
        print("\t{}".format(taskname['title']))
