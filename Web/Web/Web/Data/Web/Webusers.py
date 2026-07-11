import json
import os


FILE="Data/users.json"


def load_users():

    if not os.path.exists(FILE):

        return {}

    with open(FILE) as f:

        return json.load(f)



def save_user(name):

    users = load_users()


    if name not in users:

        users[name]={
            "memory":[]
        }


    with open(FILE,"w") as f:

        json.dump(
            users,
            f,
            indent=4
        )


    return users[name]
