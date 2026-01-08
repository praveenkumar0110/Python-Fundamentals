# tips:
# __ double underscore like private class
class account:
    def __init__(self,balance):
      self. __balance = balance

    def deposit(self,amout):
      self. __balance += amout

    def getbalance(self):
      return self. __balance
    
a = account(2000)
a.deposit(9000)

print(a.getbalance())  

 # getter and  setter

class Student:
    def __init__(self, age):
        self._age = age   # hidden data

    def get_age(self):
        return self._age   # getter

    def set_age(self, age):
        self._age = age    # setter


s1 = Student(20)          # object created
s1.set_age(100)           # age changed
print(s1.get_age())  



