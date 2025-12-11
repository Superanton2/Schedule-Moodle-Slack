import json
import random

class WeekData:
    ALL_CLASSROOMS = ["1.08.01", "1.08.02", "1.08.03", "1.08.04"]

    def __init__(self, schedule_file, subjects_file, users_file):
        self.users_file = users_file
        self.schedule_file = schedule_file
        self.subjects_file = subjects_file
        self.students = []
        self.import_data()
        self.import_subjects()
        self.user_courses()


    def import_subjects(self):
        self.subjects = []
        with open(self.subjects_file, "r") as f:
            subjects_data = json.load(f)
            for subject in subjects_data:
                self.subjects.append(subject)


    def get_a_slot(self):
        slot_day = random.choice(list(self.data))
        slot_time = random.choice(list(self.data[slot_day]))
        slot_room = random.choice(list(self.data[slot_day][slot_time]))
        return [slot_day, slot_time, slot_room]

    def random_schedule(self):
        for subject in self.subjects:
            for i in range(2):
                slot = self.get_a_slot()

                while self.data[slot[0]][slot[1]][slot[2]] != "":
                    slot = self.get_a_slot()
                self.data[slot[0]][slot[1]][slot[2]] = subject
        self.upload_data()


    def empty_schedule(self):
        for day in self.data:
            for time in self.data[day]:
                for room in self.data[day][time]:
                    if room != "":
                        self.data[day][time][room] = ""
                    else:
                        continue

        self.upload_data()


    def import_data(self):
        with open(self.schedule_file, "r") as f:
            self.data = json.load(f)


    def upload_data(self):
        with open(self.schedule_file, "w") as f:
            json.dump(self.data, f, indent=2)


    def user_courses(self):
        self.users_courses = []
        with open(self.users_file, "r") as f:
            users_data = json.load(f)
            for user in users_data:
                self.users_courses.append(users_data[user]["courses"])

    def get_free_classrooms(self, day, time):
        free = []
        occupied = []
        if day in self.data and time in self.data[day]:
            for room, available in self.data[day][time].items():
                if available == "":
                    free.append(room)
                else:
                    occupied.append((room, available))
        return free, occupied

    def has_conflict(self, new_lesson_day, new_lesson_name, new_lesson_time):

        for student_courses in self.users_courses:
            if new_lesson_name in student_courses:
                for room, lesson in self.data[new_lesson_day][new_lesson_time].items():
                    if lesson in student_courses:
                        return True
        return False

    def add_lesson(self, new_lesson_day, new_lesson_name, new_lesson_time):
        free, occupied = self.get_free_classrooms(new_lesson_day, new_lesson_time)
        if new_lesson_name not in self.subjects:
            print("The lessons name was not declared")
        elif new_lesson_name in self.data[new_lesson_day][new_lesson_time].values():
            print("Such lesson is already on this time")
        elif self.has_conflict(new_lesson_day, new_lesson_name, new_lesson_time):
            print("Sorry, the conflict is detected. Students already have another course at this time.")
        elif not free:
            print("Sorry, no free classrooms")
        else:
            self.data[new_lesson_day][new_lesson_time][free[0]] = new_lesson_name
            print(f"Lesson {new_lesson_name} added to {free[0]} on {new_lesson_day} / {new_lesson_time}")

        self.upload_data()

    def remove_lesson(self, day_of_lesson_to_remove, name_of_lesson_to_remove, time_of_lesson_to_remove):
        classrooms = self.data[day_of_lesson_to_remove][time_of_lesson_to_remove]
        for room, subject in classrooms.items():
            if subject == name_of_lesson_to_remove:
                classrooms[room] = ""
                break
        else:
            print("No such lesson")

        self.upload_data()


    def to_visualize(self):
        return self.data

