# def ap(x,y):
#     return x+y

# a= 10
# b= 20

# result = ap(a,b)
# print(result)  # Output: 30

# Parameter → function definition

# Argument → function call

# type of arguments and parameters

# 1. Positional Arguments---------

# def pk(a,b):
#     return a+b
# result = pk(10,20)
# print(result)  # Output: 30

# First value → first parameter
# Second value → second parameter

# 2. Keyword Arguments---------

# def student(name,age):
#     print("Name:",name)
#     print("Age:",age)
    
# student(age=23,name="praveen")


# 3. Default Arguments---------

# def animal(sound = "meow"):
#     print("Cat Sound is :",sound)
# animal()  # Output: Animal Sound: meow
# animal("bark")  # Output: Animal Sound: bark

# 4.*args 
'''
Evlo arguments venumnaalum pass pannalaam
 Ellam tuple-aa collect aagum
 '''
 
# def total(*args):
#      print(args)
#     #  print(type(args))
# total(10,20,30,40)
# total(1,2,3,4,6,7)



def pk(**kwargs):
    print("name",kwargs.get("name"))
    print("age",kwargs.get("age"))

pk(name ="paveen",age = "age")



