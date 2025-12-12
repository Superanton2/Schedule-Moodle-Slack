from configuration import USER_DATABASE_NAME
import json
import requests
import random

url = "https://randomuser.me/api/?results=100"

def get_names():
    response = requests.get(url)
    data = response.json()
    students = []
    lst = data["results"]
    for dct in lst:
        dct_name = dct["name"]
        first = dct_name["first"]
        last = dct_name["last"]
        name = str(first + " " + last)
        students.append(name)
    return students

programs = ["AI", "SE", "CS"]
courses = ["CS101", "CS201", "MATH101", "MATH115", "MATH111"]
url2 = "https://makemeapassword.ligos.net/api/v1/alphanumeric/json?c=100&l=8"
def get_password():
    response = requests.get(url2)
    data = response.json()
    passwords = data["pws"]
    return passwords

def generate_users_database():
    passwords = get_password()
    names = get_names()
    users_data = {name: {"password": password, "program": random.choice(programs), "courses": []} for name, password in zip(names, passwords)}

    with open(USER_DATABASE_NAME, "w", encoding='utf-8') as file:
        file.write(json.dumps(users_data, indent=4, ensure_ascii=False))
    print("Database created")

generate_users_database()