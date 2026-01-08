class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The name is {self.name} and age is {self.age}")

s = Student("Praveen", 23)
s.show()


class std:
     name ="praveen "
     age = 23
     city = "chennai"
     
     def namee():
         print("name is",name)
     def agee():
         print("age" ,age)
    
     def cityy():
        print("cityy",age)

pk1 = std()
print(pk1.name)

pk2 = std()
pk2.name = "kumar"
print(pk2.name)

# method of class :
    

# 1)instance class  --- use self
# 2) class method  ---- use @classmethod
# 3) static method ---- use @staticmethod


# @classmethod --- to handle the class level method
# @staticmethod --- its helper no obj data needed


