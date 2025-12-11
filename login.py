from check_user_input import input_to_int
from configuration import USER_DATABASE_NAME

import os.path
import json


def try_login_from_database(user_login: str, password: str) -> bool:
    """
    this function check if login and password ase correct

    :param user_login: login
    :param password: password
    :return: True if correct, False if incorrect
    """

    # open file to search for login
    with open(USER_DATABASE_NAME, "r") as file:

        # data = file.read()
        data = json.loads(file.read())

        if data.get(user_login) is None:
            return False
        elif password == data.get(user_login)["password"]:
            return True
        else:
            return False



def login():

    # можливо існує краще місце для цього
    if not os.path.exists("python.exe"):
        print("File does not exist, invalid configuration file")
        return None

    tries = 0
    while tries < 3:
        user_login =  input("Enter your login: ")
        user_password = input("Enter your password: ")

        if try_login_from_database(user_login, user_password):
            print("Correct")
            return user_login
        else:
            print(f"Wrong password. Try again. You have {3 - tries} tries left")
            tries += 1
    return None


def sign_up():

    # можливо існує краще місце для цього
    if not os.path.exists("python.exe"):
        print("File does not exist, invalid configuration file")
        return None

    user_login = input("Enter your login: ")
    user_password = input("Enter your password: ")
    user_pogrom = input("Enter your program: ")



    with open(USER_DATABASE_NAME, "r") as file:
        data = json.loads(file.read())
        file_len = len(data)

    # 2. Перевіряємо, чи існує користувач, і додаємо нового
    if user_login in data:
        print("Користувач з таким логіном вже існує!")
        return None
    else:
        # ДОДАЄМО нового користувача до існуючого словника
        data[user_login] = {
            "password": user_password,
            "pogrom": user_pogrom,
            "disciplines": [],
            "admin": False
        }

    # 3. Перезаписуємо файл повністю (режим "w")
    with open(USER_DATABASE_NAME, "w", encoding='utf-8') as file:
        # indent=4 робить файл читабельним (з відступами), як у твоєму прикладі
        json.dump(data, file, indent= (file_len + 1), ensure_ascii=False)
        print("Користувача успішно додано!")
        return user_login


def registration():
    """

    :return: повертає username зареєстрованого учасника
    """
    select_action = input_to_int("""
        1 - log in to the account
        2 - sign up to the account
        3 - quit
        """)
    while select_action not in [1, 2, 3]:
        print("Invalid input")
        select_action = input_to_int("""
        1 - log in to the account
        2 - sign up to the account
        3 - quit
            """)



    if select_action == 1:
        username = login()
        if username:
            print("You entered your account")
            return username
        else:
            print("Failure")

    elif select_action == 2:
        if sign_up():
            print("You have successfully registered on the site")
        else:
            print("Something went wrong")
    elif select_action == 3:
        print("Уou have left the registration")


    return None