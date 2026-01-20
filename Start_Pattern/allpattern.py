'''
Outer loop  → rows
Inner loop  → columns

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
for i in range(1, n+1):
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
  * * * * * * * * * * *
* * * * * * * * * * * *
  * * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
'''
