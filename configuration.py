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




LOGO = [
"  /\ \   ",
" / /\ \  ",
"/ /__\ \ ",
"\/____\/ ",
]

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
