'''
Outer loop  → rows
Inner loop  → columns

'''

'''
star start na 1start (1,n)
start from 1 to 5 (i+1)
'''


n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

'''

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''


n = 5
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()


'''
*
* *
* * *
* * * *
* * * * *
'''

n = 6
for i in range(n):
    for j in range(i,n):
      print("*",end = " ")
    print()
    
'''
* * * * * *
* * * * *
* * * *
* *
*
*
'''

n = 6
for i in range(n):
    for j in range(i,n):
      print(" ",end = " ")
    for j in range(i+1):
      print("*",end = " ")
    print()
    
'''
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
'''
n = 6
for i in range(n):
    for j in range(i+1):
      print(" ",end = " ")
    for j in range(i,n):
      print("*",end = " ")
    print()
    
'''
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
'''

n = 6
for i in range(n):
    for j in range(i,n):
      print(" ",end = " ")
    for j in range(i+1):
      print("*",end = " ")
    for j in range(i):
      print("*",end = " ")
    print()

'''
          *
        * * *
      * * * * *
    * * * * * * *
    * * * * * * * *
  * * * * * * * * * *
* * * * * * * * * * * *
'''


n = 6
for i in range(n):
    for j in range(i,n):
        print(" " , end = " ")
    for j in range(i+1):
        print("*", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" " , end = " ")
    for j in range(i,n-1):
        print("*", end = " ")
    for j in range(i,n):
        print("*", end = " ")
    print()

'''
          *
        * * *
      * * * * *
    * * * * * * * *
  * * * * * * * * * * 
* * * * * * * * * * * *
  * * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
'''
