#Mapping = Transform types by applying a function to each item in an iterable.

'''
Map(function, iterable)
👉 function → what we change
👉 iterable → list / tuple / set / range
'''

# Example 1: Using map 
pk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = tuple(map(lambda X: X * 2, pk))
print(result)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Example 2: Using map 

pk = ['apple', 'banana', 'cherry']
result = list(map(str.upper,pk))
print(result)  # Output: ['APPLE', 'BANANA', 'CHERRY']



#Example 3: Square all numbers

number = [2,4,6,8,10]

result =list(map(lambda x:x**2,number))
print(result)  # Output: [4, 16, 36, 64, 100]

# #Example 4: map with multiple iterables

a =[1,2,3,4,5]
b =[10,20,30,40,50]

result = list(map(lambda x,y: x+y,a,b))
print(result)  # Output: [11, 22, 33, 44, 55]

# important map WITH NORMAL FUNCTION (not lambda)

def sqare(x):
    return x*2
num = [10,20,30,40,50]

resul= list(map(sqare,num))
print(resul)  # Output: [20, 40, 60, 80, 100]



def uppers(x):
    return x.upper()

name = ["praveen ","kumar"]

result =tuple(map(uppers,name))
print(result)  # Output: ('PRAVEEN ', 'KUMAR')

def lenthofstring(s):
     return len(s)
name = ["im the bat man","hello world","python programming"]

resukt = list(map(lenthofstring,name))
print(resukt)  # Output: [14, 11, 18]


