## Adding methods to the student class

# The add and remove course methods were added to the class in the video
# The class looked like below at the end of it
# I have added some execution code to the bottom for demo purposes

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
enrolled in the {course} course")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")

courses_1 = ['python','rails','javascript']
courses_2 = ['java','rails','c']
mashrur = Student('mashrur','hossain',courses_1)
john = Student('john','doe',courses_2)
print(mashrur.first_name, mashrur.last_name, mashrur.courses)
print(john.first_name, john.last_name, john.courses)
print("Courses added to students")
mashrur.add_course('c')
john.add_course('c++')
print(mashrur.first_name, mashrur.last_name, mashrur.courses)
print(john.first_name, john.last_name, john.courses)
print("Courses removed from students")
mashrur.remove_course('rails')
john.remove_course('java')
print(mashrur.first_name, mashrur.last_name, mashrur.courses)
print(john.first_name, john.last_name, john.courses)
