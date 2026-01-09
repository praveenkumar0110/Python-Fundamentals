#Object create aagumbodhu automatically call aagura special method
'''
self is required to access object variables inside class methods; otherwise Python treats them as local variables.

'''

#__init__ = constructor method 

#obj store the memory constructor(create new obj)

class pk:
    def __init__(self,firstname,lastname):
     self.firstname = firstname
     self.lastname = lastname
     #Object-oda variable create பண்ணி, value assign panra line ithu .
    

car = pk("praveen", "kumar")
print(car.firstname,car.lastname)

car1 = pk("prithivi" ,"raj")
print(car1.firstname,car.lastname)




'''
🔑 Summary

Constructor → create & initialize

self → current object

Destructor → clean up

del → delete reference

__str__() → readable object output

'''



