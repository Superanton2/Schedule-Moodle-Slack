import json
import random

class User:
    def __init__(self, name: str, program:str, disciplines: list):
        self.name = name
        self.program = program
        self.disciplines = disciplines

    def __str__(self):
        return f"{self.name} is on {self.program} and enrolled to {self.disciplines}"

    def enroll(self, discipline):
        if discipline in self.disciplines:
            print("Student is already enrolled on this discipline")
        else:
            with open("schedule.json", "a") as file:
                for line in file.readlines():
                    schedule = json.loads(line)
                    for day in schedule:
                        for pair in day:
                            subjects = []
                            for subject in pair.values():
                                subjects.append(subject)

                                if not subject in self.disciplines:
                                    self.disciplines.append(subject)
                                    room = random.choice(schedule[day][pair].keys())
                                    if not schedule[day][pair][room]:
                                        schedule[day][pair][room] = subject

                                    with open("users.json", "w") as file:
                                    print(f"You was successfully enrolled to {discipline}")



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
