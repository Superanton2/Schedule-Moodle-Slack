from class_WeekSchedule import WeekData

class Admin:
    def __init__(self, name):
        self.name = name

    def add_pair(self, new_lesson_day, new_lesson_name, new_lesson_time):
        w = WeekData("schedule.json", "subjects.json")
        if not ValueError:
            print(f"{self.name} added {new_lesson_name} lesson in {new_lesson_day} at {new_lesson_time}")
        w.add_lesson(new_lesson_day, new_lesson_name, new_lesson_time)


    def remove_pair(self, new_lesson_day, new_lesson_name, new_lesson_time):
        w = WeekData("schedule.json", "subjects.json")
        print(f"{self.name} removed {new_lesson_name} lesson in {new_lesson_day} at {new_lesson_time}")
        w.remove_lesson(new_lesson_day, new_lesson_name, new_lesson_time)

a = Admin("Andrii")
a.add_pair("Monday", "CS101.1", "Pair2")