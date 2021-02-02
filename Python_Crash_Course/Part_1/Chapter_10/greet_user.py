import json


def greet_user():
    """问候用户,并指出其名字"""
    filename = "username.json"

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            print("Welcome back, %s!" % username)
    except FileNotFoundError:
        username = input("What's your name? ")

        with open(filename, "w") as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, %s!" % username)


greet_user()
