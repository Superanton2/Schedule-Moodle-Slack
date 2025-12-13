from configuration import USER_DATABASE_NAME, SCHEDULE_DATABASE_NAME
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
        self.week = WeekData("schedule.json", "subjects.json", "users.json")

    def __str__(self):
        self.__re_read__()
        return f"{self.name} is on {self.program} and enrolled to {self.disciplines}"

    def __re_read__(self):
        with open(USER_DATABASE_NAME, "r") as file:
            data = json.load(file)
            self.disciplines = data[self.name]["courses"]

    def __checker__(self, discipline):
        with open(SCHEDULE_DATABASE_NAME, "r") as file:
                schedule = json.load(file)

                for day in schedule:
                        day = schedule[day]

                        for pair in day:
                            pair = day[pair]

                            for room in pair:

                                    for mine in self.disciplines:
                                        if mine in pair.values():
                                            break

                                    if pair[room] == discipline and not pair[room] in self.disciplines:
                                        self.counter += 1
                                        continue

                                    else:
                                        continue
        return self.counter

    def __help_enroll__(self, counter, discipline):
        if counter == 1:
            print(f"No way you can visit {discipline}")
        elif counter == 2:
            with open(USER_DATABASE_NAME, "r") as file:
                data = json.load(file)
            data[self.name]["courses"].append(discipline)
            with open(USER_DATABASE_NAME, "w") as file:
                json.dump(data, file, indent=2)
            print(f"You was successfully enrolled to {discipline}")
            self.__print_schedule__()
            return True
        else:
            return False
        return False

    def __help_enroll_2__(self, discipline, counter):
        discipline = list(discipline)
        if discipline[-1] == "1":
            discipline[-1] = "2"
            dis = "".join(discipline)
            counter2 = self.__checker__(dis)
            print(counter2)
            counter += counter2
            if not self.__help_enroll__(counter, dis):
                print(f"You was not enrolled on {dis}")

        elif discipline[-1] == "2":
            discipline[-1] = "1"
            dis = "".join(discipline)
            counter2 = self.__checker__(dis)
            counter += counter2
            if not self.__help_enroll__(counter, dis):
                print(f"You was not enrolled on {dis}")


    def enroll(self, discipline):
        if discipline in self.disciplines:
            print("Student is already enrolled on this discipline")
            return False
        else:
            counter = self.__checker__(discipline)
            print(counter)
            result = self.__help_enroll__(counter, discipline)
            if result:
                return True
            else:
                answers = ["y", "n"]
                ans = input("No free places for this group. Do you want to try pick another group? [y/n]: ")
                while not ans.lower() in answers:
                    ans = input("Invalid answer. Do you want to try pick another group? [y/n]: ")
                if ans == "y":
                    self.__help_enroll_2__(discipline, counter)
                    return False
                else:
                    print(f"You was not enrolled on {discipline}")
                    return False

    def __print_schedule__(self):
        self.__re_read__()
        self.schedule.create_window(6, 6, 12, 4)
        self.schedule.input_week_lessons(self.week.schedule_for_user(self.disciplines))
        self.schedule.print_window(" ", " ")

    def leave(self, discipline):
        if not discipline in self.disciplines:
            print("You are not enrolled to this discipline")
            return False
        else:
            with open(USER_DATABASE_NAME, "r") as file:
                dct = json.load(file)
            user = dct[self.name]
            user["courses"].remove(discipline)
            dct[self.name].update(user)
            with open(USER_DATABASE_NAME, "w") as file:
                json.dump(dct, file, indent=2, ensure_ascii=False)
                self.__print_schedule__()
            print("Leaved successfully")
            return True