class dog:
    def sound(self):
        print("barking")

class cat:
     def sound(self):
            print("meow")


for animal in(dog(),cat()):
     animal.sound()



#  tip:
# both class have same funcation name method


'''
🧠 Concept (Simple-aa)

Method overloading na:

Same function name, different number of arguments use pannradhu.

Python-la:
👉 Same function name-ku multiple definitions allow illa
👉 Default arguments use panninaa, ore function-la multiple cases handle pannalaam🧠 Concept (Simple-aa)

Method overloading na:

Same function name, different number of arguments use pannradhu.

Python-la:
👉 Same function name-ku multiple definitions allow illa
👉 Default arguments use panninaa, ore function-la multiple cases handle pannalaam
'''

def add(a, b=0):
    return a + b
print(add(5))      # Output: 5
print(add(5, 3))   # Output: 8


#Same function, different arguments = overloading effect

#Example 2: Multiple Default Arguments
def na(name,mess="welcome"):
    print(name,mess)
na("pk")            #output pk welcome
na("pk","hi")       #output pk hi



# using * args keywords most important ----
class summation:
    def addd(self,*args):
        ans =0
        for i in args:
            ans+=i
        return ans
sum1 = summation()
print(sum1.addd(10,10,80)) #100



#--------------------------
#run time polymorphiam overrriding


'''
Parent class-la irukkura method-ai, Child class-la same name & same parameters use panni redefine pannradhu

👉 Inheritance must irukkanum
'''
class Parent:
    def show(self):
        print("This is Parent class method")
        
class Child(Parent):
    def show(self):
        print("This is Child class method")
        
        
obj = Child()
obj.show() 
#This is Child class method

'''
📝 Short Conclusion:

Overloading → Same method, different parameters

Overriding → Same method, different implementation

Python-la overloading workaround dhaan, overriding proper-aa support
'''