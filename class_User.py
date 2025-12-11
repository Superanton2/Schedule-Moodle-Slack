import json

class User:
    def __init__(self, name: str, program:str, disciplines: list):
        self.name = name
        self.program = program
        self.disciplines = disciplines
        self.counter = 0

    def __str__(self):
        return f"{self.name} is on {self.program} and enrolled to {self.disciplines}"

    def __checker__(self, discipline):
        with open("schedule.json", "r") as file:
                schedule = json.load(file)

                for day in schedule:
                        day = schedule[day]

                        for pair in day:
                            pair = day[pair]

                            for room in pair:

                                for mine in self.disciplines:

                                    if mine in pair.values():
                                        continue

                                    elif pair[room] == discipline and not pair[room] in self.disciplines:
                                        self.counter += 1
                                        continue

                                    else:
                                        continue
        return self.counter

    def __help_enroll__(self, counter, discipline):
        if counter == 1:
            print(f"No way you can visit {discipline}")
        elif counter == 2:
            with open("users.json", "r") as file:
                data = json.load(file)
            data[self.name]["courses"].append(discipline)
            with open("users.json", "w") as file:
                json.dump(data, file, indent=2)
            print(f"You was successfully enrolled to {discipline}")
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

