from class_WeekSchedule import WeekData as schedule
from class_User import User as u
#
# def main():
#     while True:
#         print()
#         print("Hello")
#         user = registration()
#         if user:
#             print(user)


# s = schedule("schedule.json", "subjects.json")
# s.random_schedule()

user = u("Wendy Parra", "CS", ["MATH111.2"])
user.enroll("MATH115.1")

# if __name__ == "__main__":
#     main()