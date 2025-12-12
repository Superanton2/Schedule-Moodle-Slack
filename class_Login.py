from jinja2 import select_autoescape

from helper_functions import lst_input_to_int
from configuration import USER_DATABASE_NAME, ADMIN_DATABASE_NAME
from class_User import User
from class_Admin import Admin

import json


class Login:
    def __init__(self):

        self.name = ""
        self.password = ""
        self.program = ""
        self.disciplines = []

        self.admin_status = None


    def __try_find_user(self, user_login: str, password: str) -> bool:
        # open file to search for login
        with open(USER_DATABASE_NAME, "r") as file:

            data = json.loads(file.read())

            # якщо нема імені
            if data.get(user_login) is None:
                self.name = ""
                return False

            elif password != data.get(user_login)["password"]:
                self.name = user_login
                return False

            elif password == data.get(user_login)["password"]:
                self.name = user_login
                self.password = password
                self.program = data.get(user_login)["program"]
                self.admin_status = False
                return True

            return False

    def __try_find_admin(self, user_login: str, password: str) -> bool:
        # open file to search for login
        with open(ADMIN_DATABASE_NAME, "r") as file:

            data = json.loads(file.read())

            # якщо нема імені
            if data.get(user_login) is None:
                self.name = ""
                return False

            elif password != data.get(user_login):
                self.name = user_login
                return False

            elif password == data.get(user_login):
                self.name = user_login
                self.password = password
                self.admin_status = True
                return True

            return False

    def _try_login_from_database(self, user_login: str, password: str) -> bool:
        """
        this function check if login and password ase correct

        :param user_login: login
        :param password: password
        :return: True if correct, False if incorrect
        """


        if self.__try_find_user(user_login, password):
            return True
        elif self.__try_find_admin(user_login, password):
            return True
        else:
            return False

    def __reset_values(self):
        self.name = ""
        self.password = ""
        self.program = ""
        self.admin_status = None

    def login(self) -> bool:

        tries = 3
        while tries > 0:
            user_login = input("Enter your login: ")
            user_password = input("Enter your password: ")

            # пробуємо залогінетись
            if self._try_login_from_database(user_login, user_password):
                print("You entered")
                return True

            # якщо не зайшли, то перевіряємо результати програми
            if self.name == "":
                print(f"There is no such name. Do you want to registrate")
                select_action = lst_input_to_int(["Yes", "No"])

                if select_action == 1:
                    # якщо вибрали реєктруватись, то переходимо до реєктрації
                    self.sign_up()
                    return False
                else:
                    print("Continue to log in")

            elif self.password == "":
                print("Wrong password")


            # скидуємо все що ми отримали
            self.__reset_values()
            tries -= 1
            print(f"Try again. You have {tries} tries left")

        return False

    def sign_up(self) -> bool:
        print("sign up")

        with open(USER_DATABASE_NAME, "r") as file:
            data = json.loads(file.read())
            file_len = len(data)

        user_login = input("Enter your login: ")
        while user_login in data:
            print("A user with such a login already exists!")
            user_login = input("Enter your login: ")

        user_password = input("Enter your password: ")
        user_pogrom = input("Enter your program: ")


        data[user_login] = {
            "password": user_password,
            "pogrom": user_pogrom,
            "disciplines": [],
        }

        self.name = user_login
        self.password = user_password
        self.program = user_pogrom

        with open(USER_DATABASE_NAME, "w", encoding='utf-8') as file:
            json.dump(data, file, indent= 4)
            print("User successfully added!")
            return True

    def registration(self):
        select_action = lst_input_to_int(["log in to the account", "sign up to the account", "quit"])

        if select_action == 1:
            # якщо вибрали 1, то запускаємо логін
            self.login()

        elif select_action == 2:
            # якщо вибрали 2, то запускаємо реєстрацію
            self.sign_up()

        else:
            print("Уou have left the registration")
            return False

        if self.admin_status:
            print("You entered your user account")
            output = Admin(self.name)
        elif not self.admin_status:
            print("You entered your admin account")
            output = User(self.name, self.program, self.disciplines)
        else:
            print("You failed registration")
            output = False

        return output
