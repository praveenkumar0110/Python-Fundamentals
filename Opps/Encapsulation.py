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




'''
Without Encapsulation (Bad practice ❌)--------------------
balance = 1000

def withdraw(amount):
    global balance
    balance -= amount
👉 Data & function separate
👉 Any place-la balance change pannalaam 😬


With Encapsulation (Correct 👍)-------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


Usage:

acc = BankAccount(1000)
acc.withdraw(200)
print(acc.get_balance())



Neenga balance directly change panna mudiyadhu -------------summary most mportant

ATM methods (withdraw, deposit) moolama dhaan

👉 Idhu dhaan Encapsulation

📌 One-line Thanglish summary

Encapsulation = Data + Methods
ore class-kulla irundhu
unnecessary access-a hide pannradhu

'''