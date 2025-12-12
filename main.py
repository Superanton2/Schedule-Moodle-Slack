import json
from class_Login import Login
from class_Visual import Visual
from class_Admin import Admin
from class_User import User
from class_WeekSchedule import WeekData

class Run:
    def __init__(self, registration):
        self.admin = None
        self.user = None
        if type(registration) == Admin:
            self.admin = registration
        elif type(registration) == User:
            self.user = registration
        self.schedule = Visual()
        self.week = WeekData("schedule.json", "subjects.json", "users.json")

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
        # вибір для юзера
        inputs = ["1", "2", "3", "4"]
        print(""""
1 - status
2 - enroll
3 - leave discipline
4 - quit""")
        while True:
            answer = input("What you want to do: ")
            while not answer in inputs:
                answer = input("Invalid answer. What you want to do: ")

            if answer == "1":
                print(self.user)

            elif answer == "2":
                discipline = input("Enter what discipline you want to enroll: ")
                with open("subjects.json", "r") as file:
                    subjects = json.load(file)
                    while not discipline in subjects:
                        discipline = input("No such discipline. Enter what discipline you want to enroll: ")
                self.user.enroll(discipline)

            elif answer == "3":
                discipline = input("Enter what discipline you want to leave: ")
                with open("subjects.json", "r") as file:
                    subjects = json.load(file)
                    while not discipline in subjects:
                        discipline = input("No such discipline. Enter what discipline you want to leave: ")
                self.user.leave(discipline)

            elif answer == "4":
                quit()

    def __admin_panel__(self, action):

        with open("schedule.json", "r") as file:
            days = []
            schedule = json.load(file)
            for day in schedule:
                days.append(day.lower())
        new_lesson_day = input(f"Enter day when you want to {action} pair: ")
        while not new_lesson_day.lower() in days:
            new_lesson_day = input(f"Invalid day. Enter day when you want to {action} pair: ")

        new_lesson_name = input(f"Enter lesson you want to {action}: ")
        with open("subjects.json", "r") as file:
            subjects = json.load(file)
            while not new_lesson_name in subjects:
                new_lesson_name = input(f"No such discipline. Enter what discipline you want to {action}: ")

        new_lesson_time = input("Enter time: ")
        pairs = ["pair1", "pair2", "pair3", "pair4"]
        while not new_lesson_time.lower() in pairs:
            new_lesson_time = input("No such time slot. Enter time: ")

        return new_lesson_day.capitalize(), new_lesson_name.upper(), new_lesson_time.capitalize()

    def run_admin(self):
        # малюємо ВЕСЬ розклад
        self.schedule.create_window(6, 6, 12, 16)
        self.schedule.print_window(" ", " ")
        # вибір для адміна
        inputs = ["1", "2"]
        print("""1 - add pair
        2 - remove pair""")
        while True:
            answer = input("What you want to do: ")
            while not answer in inputs:
                answer = input("Invalid answer. What you want to do: ")

            if answer == "1":
                lst = self.__admin_panel__("add")
                self.admin.add_pair(lst[0], lst[1], lst[2])

            if answer == "2":
                lst = self.__admin_panel__("remove")
                self.admin.remove_pair(lst[0], lst[1], lst[2])

l = Login()
result = l.registration()
r = Run(result)
r.program()