import json

class User:
    def __init__(self, name: str, program:str, disciplines: list):
        self.name = name
        self.program = program
        self.disciplines = disciplines

    def __str__(self):
        return f"{self.name} is on {self.program} and enrolled to {self.disciplines}"

    def __checker__(self, discipline):
        counter = 0
        with (open("schedule.json", "r") as file):
            for line in file.readlines():
                schedule = json.loads(line)
                for day in schedule:
                    for pair in day:
                        for subject in pair.values():
                            if subject != discipline or subject in self.disciplines:
                                continue
                            elif subject == discipline and not subject in self.disciplines:
                                counter = 1
                            else:
                                continue
        return counter

    def enroll(self, discipline):
        if discipline in self.disciplines:
            print("Student is already enrolled on this discipline")
            return False
        else:
            counter = self.__checker__(discipline)
            if counter == 1:
                answers = ["y", "n"]
                ans = input("No free places for this group. Do you want to try pick another group? [y/n]")
                while not ans.lower() in answers:
                    ans = input("Invalid answer. Do you want to try pick another group? [y/n]")
                if ans == "y":
                    discipline = list(discipline)
                    if discipline[:-1] == "1":
                        discipline[:-1] = "2"
                        dis = "".join(discipline)
                        counter2 = self.__checker__(dis)
                        counter += counter2
                        if counter == 1:
                            print("No free places for you on those discipline")
                        elif counter == 2:
                            with open("users.json", "w") as file:
                                data = json.load(file)
                                data[self.name]["courses"].append(discipline)
                                print(f"You was successfully enrolled to {discipline}")
                        return True
                else:
                    print(f"You was not enrolled on {discipline}")
                    return False

    def leave(self, discipline):
        if not self.name in discipline.enrolled:
            print("You are not enrolled to this discipline")
        else:
            with open("users.json", "a") as file:
                for line in file.readlines():
                    line = json.loads(line)
                    dct = line[self.name]
                    dct["courses"].remove(discipline)
            discipline.enrolled.remove(self.name)
            print("Leaved successfully")
