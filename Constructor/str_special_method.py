'''
__str__() is a special method in Python.
It defines what should be shown when you print an object.

'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

s1 = Student("Praveen", 23)
print(s1)


'''
__init__() → creates and initializes the object

__str__() → returns a readable string for the object

print(s1) → automatically calls s1.__str__()
'''