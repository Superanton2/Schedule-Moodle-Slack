from check_user_input import input_to_int
from configuration import USER_DATABASE_NAME

import json


def try_login_from_database(login: str, password: str) -> bool:
    """
    this function check if login and password ase correct

    :param login: login
    :param password: password
    :return: True if correct, False if incorrect
    """

    # open file to search for login
    with open(USER_DATABASE_NAME, "r") as file:

        # data = file.read()
        data = json.loads(file.read())

        if data.get(login) is None:
            return False

        elif password == data.get(login)["password"]:
            return True
        else:
            return False






print(try_login_from_database("Anton", "123"))