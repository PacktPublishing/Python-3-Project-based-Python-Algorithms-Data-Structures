## Adding special methods to the student class

# We first added the __str__() special method to get a string
# representation of our student object, we also added the __len__()
# and __repr__() methods, you can code out the __str__() method
# to see the __repr__() method in action
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

    def __len__(self):
        return len(self.courses)

    def __repr__(self):
        return f"Student('{self.first_name}','{self.last_name}',{self.courses})"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()}\nLast name: {self.last_name.capitalize()}\
        \nCourses: {', '.join(map(str.capitalize, self.courses))}"


courses_1 = ['python','rails','javascript']
courses_2 = ['java','rails','c']
mashrur = Student('mashrur','hossain',courses_1)
john = Student('john','doe',courses_2)
print(mashrur)
print(john)
print(f"{mashrur.first_name.capitalize()} is enrolled in {len(mashrur)} courses")
print(f"{john.first_name.capitalize()} is enrolled in {len(john)} courses")
