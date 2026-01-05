"""
condition.py
Author: PK
Purpose: Python conditional statements with examples
Comments: English (clear explanation)
"""

# ==================================================
# 1. BASIC IF STATEMENT
# ==================================================

age = 18

if age >= 18:
    print("Eligible to vote")
# If condition is true, block will execute

# ==================================================
# 2. IF - ELSE STATEMENT
# ==================================================

num = 5

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
# If condition true → if block
# Else → else block

# ==================================================
# 3. IF - ELIF - ELSE STATEMENT
# ==================================================

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
# Multiple conditions checked in order

# ==================================================
# 4. NESTED IF
# ==================================================

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# ==================================================
# 5. COMPARISON OPERATORS
# ==================================================

a = 10
b = 20

a == b    # Equal to
a != b    # Not equal
a > b     # Greater than
a < b     # Less than
a >= b    # Greater than or equal
a <= b    # Less than or equal

# ==================================================
# 6. LOGICAL OPERATORS
# ==================================================

x = 10
y = 20

x > 5 and y > 15   # True if both conditions are true
x > 15 or y > 15  # True if at least one condition is true
not(x > 5)        # Reverse the condition

# ==================================================
# 7. MEMBERSHIP OPERATORS
# ==================================================

nums = [1, 2, 3, 4]

5 in nums          # Check if value exists
5 not in nums      # Check if value does not exist

# ==================================================
# 8. IDENTITY OPERATORS
# ==================================================

a = [1, 2, 3]
b = a
c = [1, 2, 3]

a is b             # True (same memory)
a is c             # False (different memory)
a is not c         # True

# ==================================================
# 9. TERNARY (SHORT HAND IF-ELSE)
# ==================================================

num = 10

result = "Even" if num % 2 == 0 else "Odd"
print(result)
# Single-line conditional expression

# ==================================================
# 10. MULTIPLE CONDITIONS
# ==================================================

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# ==================================================
# 11. PASS STATEMENT
# ==================================================

x = 10

if x > 5:
    pass
# pass is used when statement is required syntactically
# but no action is needed

# ==================================================
# 12. MATCH-CASE (Python 3.10+)
# ==================================================

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Invalid day")

# match-case is similar to switch-case in other languages

# ==================================================
# 13. TRUTHY AND FALSY VALUES
# ==================================================

if "":
    print("This will not execute")

if 1:
    print("This will execute")

# Falsy values: 0, 0.0, "", [], {}, set(), None, False
# All other values are Truthy

# ==================================================
# 14. CONDITION WITH FUNCTIONS
# ==================================================

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))

# ==================================================
# 15. CHAINED COMPARISONS
# ==================================================

x = 15

if 10 < x < 20:
    print("x is between 10 and 20")

# ==================================================
# END OF FILE
# ==================================================
