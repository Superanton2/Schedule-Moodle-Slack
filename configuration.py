"""
here are configurations to our program
"""
import os.path


# path to database with information about users
USER_DATABASE_NAME = "users.json"
ADMIN_DATABASE_NAME = "admin.json"
SCHEDULE_DATABASE_NAME = "schedule.json"
SUBJECTS_DATABASE_NAME = "subjects.json"

# перевіряємо чи існує файл
if not os.path.exists(USER_DATABASE_NAME):
    print("USER database file does not exist, invalid configuration file")
if not os.path.exists(ADMIN_DATABASE_NAME):
    print("ADMIN database file does not exist, invalid configuration file")
if not os.path.exists(SCHEDULE_DATABASE_NAME):
    print("SCHEDULE database file does not exist, invalid configuration file")
if not os.path.exists(SUBJECTS_DATABASE_NAME):
    print("SUBJECTS database file does not exist, invalid configuration file")




# LOGO = [
# "  /\ \   ",
# " / /\ \  ",
# "/ /__\ \ ",
# "\/____\/ ",
# ]

day_encoder = {
    # день тижня: x координата
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5
}

pair_time_encoder = {
    # номер пари: [y координата, фактичний час]
    "Pair1": [3, "8:30-9:50"],
    "Pair2": [2, "10:00-11:20"],
    "Pair3": [1, "11:30-12:50"],
    "Pair4": [0, "13:30-14:50"]
}

PROGRAMS = ["AI", "SE"]


DISCIPLINES = {
    "CS" : {
        "101" : "Computer Science Foundations",
        "201" : "Programming Basics"
    },
    "MATH" : {
        "101" : "Introduction to Mathematics",
        "111" : "Calculus",
        "115" : "Discrete Mathematics"
    }
}

"""
━
┃
┏┳┓
┣╋┫
┗┻┛
"""

# vis = Visual()
# vis.create_window(6, 6, 12, 4)
#
#
# # from configuration import LOGO
#
# # vis.write_lst_to_coordinate(0, 4, LOGO)
# vis.write_lst_to_coordinate(0, 3, ["By Anton", "   Andrew", "   Katya"])
#
#
#
# data_mon = {"Pair1": {"1.08.01": "Math115"}}
# vis.input_day_lessons("Monday", data_mon)
#
# data = {
#   "Monday": {
#     "Pair1": {"1.08.01": "Math115",},
#     "Pair2": {"1.08.03": "Math111",},
#     "Pair4": {"1.08.02": "Math101",}
#   },
#   "Tuesday": {
#     "Pair3": {"1.08.01": "Math111",},
#     "Pair4": {"1.08.01": "Math101",}
#   }
# }
#
# vis.input_week_lessons(data)
#
# # vis.add_line_to_coordinate((0, 0), (1, 0))
# # vis.add_line_to_coordinate((1, 1), (2, 1))
#
# vis.print_window(vertical_sep= "│", horizontal_sep= "─")
# print()
# print()
# print()
# vis.print_window(vertical_sep= "┃", horizontal_sep= "━")
# print()
# print()
# print()
# vis.print_window(vertical_sep= " ", horizontal_sep= " ")