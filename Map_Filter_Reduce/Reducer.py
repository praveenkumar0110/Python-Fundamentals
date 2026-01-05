'''
Reducer = Many values → ONE value
[1, 2, 3, 4] → 10

IMPORTANT NOTE (FIRST)

👉 reduce direct-aa Python-la irukkaadhu
👉 functools module-la irundhu import pannanum


from functools import reduce
from functools import reduce

'''
from functools import reduce

# Example 1: Sum of all numbers in a list
num =[10,10,10,10,10,50]

result = reduce(lambda x,y:x+y,num)
print(result)  # Output: 100


# Example 2: Finding maximum value in a list
num = [1,2,3,4,5]

result = reduce(lambda x,y: x if x > y else y ,num)
print(result)  # Output: 5


def pk (x,y):
    if x > y:
        return x
    else:
        return y
    
num = [10,20,30,40,50,60]
result = reduce(pk,num)
print(result)  # Output: 60