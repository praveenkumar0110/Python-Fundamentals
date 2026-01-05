'''
🟢 BASIC IDEA – filter na enna?

👉 Filter = Select pannradhu

Simple words-la:
Iterable-la irukkura ovvoru element-um check pannum,
condition true aagura elements mattum keep pannum.

❗ Values change aagadhu
❗ Count reduce aagalam
'''

add = [10, 25, 30, 45, 50, 65, 70, 85, 90, 100]

result = list(filter(lambda X:X % 2==0,add))
print(result)  # Output: [10, 30, 50, 70, 90, 100]


name = ['praveenkumar.e', 'kumar', 'raja', 'suresh', 'anitha', 'divya']
result = set(filter(lambda X:len(X)>10,name))
print(result)  # Output: {'praveen', 'anitha', 'divya', 'suresh'}

# Example 3: using filter in defining even numbers
def isevn(x):
    return x %2 == 0
pk = [12,34,6,68,90,11,23,45]
result =list(filter(isevn,pk))
print(result)  # Output: [12, 34, 6, 68, 90]

#Example 6: filter + map (Pipeline)

num =[1,2,3,4,5]

result = list(map(lambda X:X*2 ,
                  filter(lambda X:X%2==0,num)))

print(result)  # Output: [4, 8]


#Example 7: filter + map with normal functions
def iseven(x):
    return x % 2 == 0

def add2(x):
    return x*2

num = [1,2,3,4,5]

result  =list(map(add2,
                  filter(iseven,num)))
print(result)  # Output: [4, 6]