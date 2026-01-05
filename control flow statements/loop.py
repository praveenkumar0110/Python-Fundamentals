"""
loop.py
Author: PK
Purpose: Python looping statements with examples
Comments: English (clear explanation)
"""

# ==================================================
# 1. FOR LOOP (BASIC)
# ==================================================

# Loop through a list
numbers = [1, 2, 3, 4, 5]

for n in numbers:
    print(n)
# Iterates over each element in the list

# ==================================================
# 2. FOR LOOP WITH RANGE
# ==================================================

for i in range(5):
    print(i)
# range(5) → 0 to 4

for i in range(1, 6):
    print(i)
# range(start, stop)

for i in range(1, 10, 2):
    print(i)
# range(start, stop, step)

# ==================================================
# 3. LOOP THROUGH STRING
# ==================================================

name = "Python"

for ch in name:
    print(ch)
# Iterates character by character

# ==================================================
# 4. LOOP THROUGH DICTIONARY
# ==================================================

data = {"a": 1, "b": 2, "c": 3}

for key in data:
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)

# ==================================================
# 5. WHILE LOOP
# ==================================================

count = 1

while count <= 5:
    print(count)
    count += 1
# Loop runs while condition is true

# ==================================================
# 6. INFINITE LOOP (USE WITH CAUTION)
# ==================================================

# while True:
#     print("This is infinite")
# Use break to stop infinite loops

# ==================================================
# 7. BREAK STATEMENT
# ==================================================

for i in range(1, 10):
    if i == 5:
        break
    print(i)
# break stops the loop completely

# ==================================================
# 8. CONTINUE STATEMENT
# ==================================================

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# continue skips current iteration

# ==================================================
# 9. PASS STATEMENT IN LOOP
# ==================================================

for i in range(5):
    pass
# pass is used as a placeholder (no operation)

# ==================================================
# 10. ELSE WITH LOOP
# ==================================================

for i in range(5):
    print(i)
else:
    print("Loop completed successfully")
# else executes only if loop finishes without break

# ==================================================
# 11. NESTED LOOPS
# ==================================================

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
# One loop inside another loop

# ==================================================
# 12. LOOP WITH ENUMERATE
# ==================================================

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(index, color)
# enumerate gives index and value

# ==================================================
# 13. LOOP WITH ZIP
# ==================================================

names = ["A", "B", "C"]
scores = [90, 80, 70]

for name, score in zip(names, scores):
    print(name, score)
# zip combines multiple iterables

# ==================================================
# 14. LIST COMPREHENSION (LOOP SHORTCUT)
# ==================================================

squares = [x * x for x in range(1, 6)]
print(squares)
# Compact way to create list using loop

# ==================================================
# 15. NESTED LIST COMPREHENSION
# ==================================================

matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)

# ==================================================
# 16. LOOP CONTROL WITH INPUT
# ==================================================

# Uncomment to test
# while True:
#     user_input = input("Enter 'q' to quit: ")
#     if user_input == 'q':
#         break

# ==================================================
# 17. ITERATING SET AND TUPLE
# ==================================================

my_set = {1, 2, 3}
for x in my_set:
    print(x)

my_tuple = (10, 20, 30)
for x in my_tuple:
    print(x)

# ==================================================
# 18. REVERSED LOOP
# ==================================================

for i in reversed(range(1, 6)):
    print(i)
# reversed iterates backward

# ==================================================
# 19. LOOP WITH COUNTING LOGIC
# ==================================================

count = 0
for i in range(10):
    if i % 2 == 0:
        count += 1
print("Even numbers count:", count)

# ==================================================
# END OF FILE
# ==================================================
