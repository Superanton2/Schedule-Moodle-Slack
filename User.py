from Discipline import Discipline
import json

class User:
    def __init__(self, name: str, program:str, disciplines: list):
        self.name = name
        self.program = program
        self.disciplines = disciplines

    def __str__(self):
        return f"{self.name} is on {self.program} and enrolled to {self.disciplines}"

    def enroll(self, discipline: Discipline):
        if discipline in self.disciplines:
            print("Student is already enrolled on this discipline")
        else:
            if len(discipline.enrolled) < 30:
                discipline.enrolled.append(self.name)
                with open("users.json", "a") as file:
                    for line in file.readlines():
                        line = json.loads(line)
                        dct = line[self.name]
                        dct["courses"].append(discipline)
                print("Enrolled successfully")
            else:
                print("No free places, can't enroll")

    def leave(self, discipline: Discipline):
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