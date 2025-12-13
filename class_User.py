from configuration import USER_DATABASE_NAME, SCHEDULE_DATABASE_NAME, SUBJECTS_DATABASE_NAME
from helper_functions import lst_input_to_int

import json
from class_Visual import Visual
from class_WeekSchedule import WeekData

class User:
    def __init__(self, name: str, program:str, disciplines: list):
        self.name = name
        self.program = program
        self.disciplines = disciplines
        self.counter = 0
        self.schedule = Visual()
        self.week = WeekData(SCHEDULE_DATABASE_NAME, SUBJECTS_DATABASE_NAME, USER_DATABASE_NAME)

    def __str__(self):
        self.__re_read__()
        disciplines_str = " ".join(self.disciplines)

        return f"{self.name} is on {self.program} and enrolled to {disciplines_str}"

    def __re_read__(self):
        with open(USER_DATABASE_NAME, "r") as file:
            data = json.load(file)
            self.disciplines = data[self.name]["courses"]

    def __checker__(self, discipline: str):
        """
        перевіряє чи пересікається discipline з нашими дисцепліною
        якщо не пересікається, то до self.counter додаємо 1

        :param discipline: програма яку ми перевіряємо
        """
        with open(SCHEDULE_DATABASE_NAME, "r") as file:
            schedule = json.load(file)
        # закриваємо файл, щоб віддати ресурси
        self.counter = 0

        for day in schedule:
            day_data = schedule[day]
            self.__checker_day__(day_data, discipline)

    def __checker_day__(self, day_data: dict, discipline: str):
        """
        перевіряє чи пересікається discipline з нашими дисцепліною для певного дня
        якщо не пересікається, то до self.counter додаємо 1

        :param day_data: данні дляпевного
        :param discipline: програма яку ми перевіряємо
        """

        for pair in day_data:
            pair_data = day_data[pair]

            for room in pair_data:

                for mine in self.disciplines:
                    if mine in pair.values():
                        break

                if pair[room] == discipline and not pair[room] in self.disciplines:
                    self.counter += 1
                    continue

                else:
                    continue

    def __help_enroll__(self, discipline):
        if self.counter == 1 or self.counter == 0:
            print(f"No way you can visit {discipline}")

        elif self.counter == 2:
            with open(USER_DATABASE_NAME, "r") as file:
                data = json.load(file)
            data[self.name]["courses"].append(discipline)

            with open(USER_DATABASE_NAME, "w") as file:
                json.dump(data, file, indent=2)

            self.disciplines.append(discipline)

            print(f"You was successfully enrolled to {discipline}")

            return True
        else:
            print("something went wrong")
            return False
        return False

    def __help_enroll_2group__(self, discipline_to_enroll: str):
        discipline_to_enroll = list(discipline_to_enroll)

        # міняємо 1 групу на 2
        if discipline_to_enroll[-1] == "1":
            discipline_to_enroll[-1] = "2"
        # міняємо 2 групу на 1
        elif discipline_to_enroll[-1] == "2":
            discipline_to_enroll[-1] = "1"
        
        dis = "".join(discipline_to_enroll)

        # перевіряємо для другої групи
        self.__checker__(dis)

        if not self.__help_enroll__(dis):
            print(f"You was not enrolled on {dis}")
            
        
        

    def enroll(self, discipline):
        if discipline in self.disciplines:
            print("Student is already enrolled on this discipline")
            return False
        else:
            self.__checker__(discipline)
            result = self.__help_enroll__(discipline)
            if result:
                return True
            else:
                print("No free places for this group. Do you want to try pick another group?")
                answers = lst_input_to_int(["Yes", "No"])

                if answers == 1:
                    self.__help_enroll_2group__(discipline)
                    return False
                else:
                    print(f"You was not enrolled on {discipline}")
                    return False

    def leave(self, discipline):
        if not discipline in self.disciplines:
            print("You are not enrolled to this discipline")
            return False
        else:
            with open(USER_DATABASE_NAME, "r") as file:
                user_data = json.load(file)

            user = user_data[self.name]
            user["courses"].remove(discipline)
            user_data[self.name].update(user)

            with open(USER_DATABASE_NAME, "w") as file:
                json.dump(user_data, file, indent=2, ensure_ascii=False)

            self.disciplines.remove(discipline)
            print("Leaved successfully")
            return True