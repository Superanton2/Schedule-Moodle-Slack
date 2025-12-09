from User import User

class Discipline:
    def __init__(self, name: str, teacher: str, enrolled: list):
        self.name = name
        self.teacher = teacher
        self.enrolled = enrolled

    def add_student(self, name: User):
        self.enrolled.append(name)

    def remove_student(self, name: User):
        self.enrolled.remove(name)