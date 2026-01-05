from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Subclass 1
class Bike(Vehicle):
    def start(self):
        print("Bike started with kick")


# Subclass 2
class Car(Vehicle):
    def start(self):
        print("Car started with self button")


# Subclass 3
class Scooter(Vehicle):
    def start(self):
        print("Scooter started with electric start")


# Object creation
v1 = Bike()
v2 = Car()
v3 = Scooter()

v1.start()
v2.start()
v3.start()




# tips :
# abstract class = incomplet class
# subclass is implaentation is compulsary


