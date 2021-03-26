## Creating a custom Student class
# We can create a class using the class keyword
class Student:
    pass

# We can create instances of the class, or instances
# of student objects basically by calling the class name followed
# by () like below:
mashrur = Student()
john = Student()

# Note above mashrur and john are separate instances of students
# They are not the same object even though are both type student

# You can add attributes to your objects like below, note: we
# aim to work with first_name, last_name and eventually courses
# attributes
mashrur.first_name = 'mashrur'
mashrur.last_name = 'hossain'
john.first_name = 'john'
john.last_name = 'doe'

# You can access the attributes associated with each student object
print(mashrur.first_name, mashrur.last_name)
print(john.first_name, john.last_name)

# You can use the special __init__() method to assign the attributes
# when the instance of the object is created. It takes in a default
# first argument which is called self by convention in python, self
# is the object being created itself, followed by any other
# attributes you wish to initialize. We modified the class like below:

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

courses_1 = ['python','rails','javascript']
courses_2 = ['java','rails','c']
mashrur = Student('mashrur','hossain',courses_1)
john = Student('john','doe',courses_2)
print(mashrur.first_name, mashrur.last_name, mashrur.courses)
print(john.first_name, john.last_name, john.courses)
