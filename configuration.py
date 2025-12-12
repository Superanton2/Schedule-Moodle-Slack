"""
here are configurations to our program
"""

# path to database with information about users
USER_DATABASE_NAME = "users.json"

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
