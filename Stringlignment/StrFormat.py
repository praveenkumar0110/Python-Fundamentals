'''
| Feature    | Use                 |
| ---------- | ------------------- |
| `sep`      | separate values     |
| `end`      | control line ending |
| `\n`       | new line            |
| `\t`       | tab alignment       |
| `ljust()`  | left align          |
| `rjust()`  | right align         |
| `center()` | center align        |
| f-strings  | best formatting     |

'''


s = "batman"
p = "to save myself onlt"

print(f"im the {s} and i have t go{p}")





# table alignment

print("Name\tAge\tCity")
print("PK\t22\tChennai")
print("Ram\t25\tDelhi")



#FORMAT METHOD F" STRINGS - DELCLAR A VARIABLE WITHIN {} IMPORTANT METHOD
print(f"{'Name':<10}{'Age':<5}{'City':<10}")
print(f"{'PK':<10}{22:<5}{'Chennai':<10}")
print(f"{'Ram':<10}{25:<5}{'Delhi':<10}")



print("Hello", end=" ")
print("World")



for i in range(5):
    print(i, end=" | ")


print("A", "B", "C", sep="-", end=" END\n")
print("Next")

