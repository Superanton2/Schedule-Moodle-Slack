from helper_functions import lst_input_to_int, GREEN, RED, RESET
from configuration import USER_DATABASE_NAME, PROGRAMS

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
    if not os.path.exists(USER_DATABASE_NAME):
        print("File does not exist, invalid configuration file")
        return None

    tries = 0
    while tries < 3:
        user_login =  input("Enter your login: ")
        user_password = input("Enter your password: ")

        if try_login_from_database(user_login, user_password):
            print(f"{GREEN}Correct{RESET}")
            return user_login
        else:
            print(f"{RED}Wrong password{RESET}. Try again. You have {3 - tries} tries left")
            tries += 1
    return None


def sign_up_user(admin= False):
    """
    якщо реєструвати юзера, то input user= True
    якщо реєструвати адміна, то input user= False
    :param admin: те кого ми будемо реєктрувати
    :return: імʼя людини яку ми зареєстрували
    """

    # можливо існує краще місце для цього
    if not os.path.exists(USER_DATABASE_NAME):
        print(f"{RED}File does not exist, invalid configuration file{RESET}")
        return None

    # отримуємо данні з файлу
    with open(USER_DATABASE_NAME, "r") as file:
        data = json.loads(file.read())
        file_len = len(data)


    user_login = input("Enter your login: ")
    # якщо існує вже така людина, то питаємо поки не дасть норм відповідь
    while user_login in data:
        print(f"{RED}A user with such a login already exists!{RESET}")
        user_login = input("Enter your login: ")


    user_password = input("Enter your password: ")


    # якщо ми передали до адміна, то
    if admin:
        user_program = ""
        data_admin = True
    else:
        user_program = PROGRAMS[lst_input_to_int(PROGRAMS) - 1]
        data_admin = False


    # 2. Перевіряємо, чи існує користувач, і додаємо нового

    # ДОДАЄМО нового користувача до існуючого словника
    data[user_login] = {
        "password": user_password,
        "program": user_program,
        "disciplines": [],
        "admin": data_admin
    }

    # 3. Перезаписуємо файл повністю (режим "w")
    with open(USER_DATABASE_NAME, "w", encoding='utf-8') as file:
        # indent=4 робить файл читабельним (з відступами), як у твоєму прикладі
        json.dump(data, file, indent= (file_len + 1), ensure_ascii=False)
        print(f"{GREEN}User successfully added!{RESET}")
        return user_login


def registration():
    """

    :return: повертає username зареєстрованого учасника
    """

    select_action = lst_input_to_int(["log in to the account", "sign up to the account", "quit"])


    if select_action == 1:
        username = login()
        if username:
            print("You entered your account")
            return username
        else:
            print("Failure")

    elif select_action == 2:
        if sign_up_user():
            print("You have successfully registered on the site")
        else:
            print("Something went wrong")
    elif select_action == 3:
        print("Уou have left the registration")


    return None