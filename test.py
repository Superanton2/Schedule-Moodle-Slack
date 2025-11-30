import json

USER_DATABASE_NAME = "users.json"

def sign_up():

    user_login = input("Enter your login: ")
    user_password = input("Enter your password: ")
    user_pogrom = input("Enter your program: ")

    with open(USER_DATABASE_NAME, "r") as file:
        data = json.loads(file.read())
        file_len = len(data)

    # 2. Перевіряємо, чи існує користувач, і додаємо нового
    if user_login in data:
        print("Користувач з таким логіном вже існує!")
        return
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








# Запуск функції

sign_up()