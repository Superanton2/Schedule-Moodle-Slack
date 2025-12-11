import json
import random

class WeekData:
    ALL_CLASSROOMS = ["1.08.01", "1.08.02", "1.08.03", "1.08.04"]

    def __init__(self, schedule_file, subjects_file):
        self.schedule_file = schedule_file
        self.subjects_file = subjects_file
        self.students = []
        self.import_data()
        self.import_subjects()


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


    def import_data(self):
        with open(self.schedule_file, "r") as f:
            self.data = json.load(f)


    def upload_data(self):
        with open(self.schedule_file, "w") as f:
            json.dump(self.data, f, indent=2)


    def get_free_classrooms(self, day, time):
        used = set()

        if day in self.data and time in self.data[day]:
            used = set(self.data[day][time].keys())

        free = [room for room in self.ALL_CLASSROOMS if room not in used]
        return free


    def add_lesson(self, new_lesson_day, new_lesson_name, new_lesson_time):
        if len(self.data[new_lesson_day][new_lesson_time]) < 4:
            if new_lesson_name not in self.data[new_lesson_day][new_lesson_time].values():
                free = self.get_free_classrooms(new_lesson_day, new_lesson_time)
                self.data[new_lesson_day][new_lesson_time][free[0]] = new_lesson_name
            else:
                raise ValueError("The particular time is full")
        else:
            raise ValueError("The particular time is full")

        self.upload_data()
        self.import_data()

    def remove_lesson(self, day_of_lesson_to_remove, name_of_lesson_to_remove, time_of_lesson_to_remove):
        classrooms = self.data[day_of_lesson_to_remove][time_of_lesson_to_remove]
        for room, subject in classrooms.items():
            if subject == name_of_lesson_to_remove:
                del classrooms[room]
                break
        else:
            raise ValueError("No such lesson")

        self.upload_data()
        self.import_data()


    def to_visualize(self):
        return self.data

