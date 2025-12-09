from User import User

class Discipline:
    def __init__(self, name: str, teacher: str, enrolled: list):
        self.name = name
        self.teacher = teacher
        self.enrolled = enrolled

    def __str__(self):
        return f"The teacher on {self.name} is {self.teacher}. {len(self.enrolled)} students are enrolled on this subject"

    def add_student(self, name: User):
        if name in self.enrolled:
            print("Student is already enrolled")
        else:
            self.enrolled.append(name)

    def remove_student(self, name: User):
        self.enrolled.remove(name)
