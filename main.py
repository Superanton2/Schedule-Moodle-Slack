from class_WeekSchedule import WeekData
from class_Visual import Visual
from class_Login import Login
from class_Admin import Admin
from class_User import User

from configuration import SCHEDULE_DATABASE_NAME, SUBJECTS_DATABASE_NAME, USER_DATABASE_NAME
from helper_functions import lst_input_to_int

import json

class Run:
    def __init__(self, registration):
        self.admin = None
        self.user = None
        if type(registration) == Admin:
            self.admin = registration
        elif type(registration) == User:
            self.user = registration
        self.schedule = Visual()
        self.week = WeekData(SCHEDULE_DATABASE_NAME, SUBJECTS_DATABASE_NAME, USER_DATABASE_NAME)

    def program(self):
        if self.user:
            self.run_user()
        elif self.admin:
            self.run_admin()

    def run_user(self):
        # малюємо розклад для юзера
        self.schedule.create_window(6, 6, 12,4)
        self.schedule.input_week_lessons(self.week.schedule_for_user(self.user.disciplines))
        self.schedule.print_window(" ", " ")

        while True:
            # вибір для юзера
            answer = lst_input_to_int(["status", "enroll", "leave discipline", "quit"])

            if answer == 1:
                print(self.user)

            elif answer == 2:
                discipline = input("Enter what discipline you want to enroll: ")
                with open(SUBJECTS_DATABASE_NAME, "r") as file:
                    subjects = json.load(file)
                    while not discipline in subjects:
                        discipline = input("No such discipline. Enter what discipline you want to enroll: ")
                self.user.enroll(discipline)

            elif answer == 3:
                discipline = input("Enter what discipline you want to leave: ")
                with open(SUBJECTS_DATABASE_NAME, "r") as file:
                    subjects = json.load(file)
                    while not discipline in subjects:
                        discipline = input("No such discipline. Enter what discipline you want to leave: ")
                self.user.leave(discipline)

            elif answer == 4:
                quit()

    def __admin_panel__(self, action):

        with open(SCHEDULE_DATABASE_NAME, "r") as file:
            days = []
            schedule = json.load(file)
            for day in schedule:
                days.append(day.lower())


        new_lesson_day = input(f"Enter day when you want to {action} pair: ")
        while not new_lesson_day.lower() in days:
            new_lesson_day = input(f"Invalid day. Enter day when you want to {action} pair: ")


        new_lesson_name = input(f"Enter lesson you want to {action}: ")
        with open(SUBJECTS_DATABASE_NAME, "r") as file:
            subjects = json.load(file)
            while not new_lesson_name in subjects:
                new_lesson_name = input(f"No such discipline. Enter what discipline you want to {action}: ")


        new_lesson_time = input("Enter time: ")
        pairs = ["pair1", "pair2", "pair3", "pair4"]
        while not new_lesson_time.lower() in pairs:
            new_lesson_time = input("No such time slot. Enter time: ")

        return new_lesson_day, new_lesson_name, new_lesson_time

    def run_admin(self):
        # малюємо ВЕСЬ розклад
        self.schedule.create_window(6, 6, 12, 16)
        self.schedule.print_window(" ", " ")

        while True:
            # вибір для адміна
            answer = lst_input_to_int(["add pair", "remove pair", "quit"])

            if answer == 1:
                self.admin.add_pair(self.__admin_panel__("add")[0], self.__admin_panel__("add")[1], self.__admin_panel__("add")[2])

            if answer == 2:
                self.admin.remove_pair(self.__admin_panel__("remove")[0], self.__admin_panel__("remove")[1], self.__admin_panel__("remove")[2])

            elif answer == 3:
                quit()

    def create_schedule_window(self):
        # малюємо розклад для юзера
        self.schedule.create_window(6, 6, 12,4)
        self.schedule.input_week_lessons(self.week.schedule_for_user(self.user.disciplines))
        self.schedule.print_window(" ", " ")


def main():
    l = Login()
    result = l.registration()
    r = Run(result)
    r.program()


if __name__ == "__main__":
    main()