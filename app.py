import json
import os

from user import *


def menu():
    name = input('Please enter your name: ')
    name_file = name + '.txt'
    if name_file_exists(name_file):
        with open(name_file, 'r') as f:
            json_data = json.load(f)
            user = User.from_json(json_data)
    else:
        user = User(name)
    print(user)


def name_file_exists(file_name):
    return os.path.isfile(file_name)


menu()



