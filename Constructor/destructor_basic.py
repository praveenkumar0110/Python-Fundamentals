'''
A destructor is a method that runs when an object is destroyed.

In Python, the destructor method is called __del__().
'''


class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

s1 = Student("Praveen")
del s1



'''
🔑 Summary

Constructor → create & initialize

self → current object

Destructor → clean up

del → delete reference

__str__() → readable object output
'''