
'''
| Tool            | Use                   |
| --------------- | --------------------- |
| Breakpoint 🔴   | Pause execution       |
| Step Into ⤴️    | Function inside       |
| Step Over ⤵️    | Next line             |
| Step Out 🔁     | Exit function         |
| Variables panel | Current values        |
| Watch           | Custom variable watch |

'''


# a =10
# b =10
# c = a / b  
# print(c)


'''
complie time error - convert  machine language(interpreter )
runtime error - occur during execution of program
'''


# n = 5 
# ans = 1
# for i in range(1,n+1):
#     ans = ans *i
# print(ans)

# def fact(n):
#     n = 5 
#     ans = 1
#     for i in range(1,n+1):
#         ans = ans *i
#     print(ans)
# n = int(input("Enter a number: "))
# fact(n)


# def print_nums(n):
#     for i in range(1, n):
#         print(i)

# print_nums(5)


'''
Expected
1 2 3 4 5

Actual
1 2 3 4

Debug:

Step through loop

Check range()

Fix
range(1, n+1)

'''


def add_item(lst):
    lst.append(100)
    return lst

nums = add_item([1, 2, 3])
print(nums)