"""
datatype.py
Author: PK
Purpose: Python built-in datatypes with methods
Comments: English (clear explanation)
"""

# ==================================================
# 1. INTEGER (int)
# ==================================================

x = 10

# Integer methods
x.bit_length()        # Number of bits needed to represent the number
x.bit_count()         # Count of 1s in binary representation
x.to_bytes(2, 'big')  # Convert integer to bytes
int.from_bytes(b'\x00\n', 'big')  # Convert bytes to integer

# Common built-in functions
abs(x)                # Absolute value
pow(x, 2)             # Power operation
divmod(10, 3)         # Returns (quotient, remainder)

# ==================================================
# 2. FLOAT
# ==================================================

f = 10.5

f.is_integer()        # Check if float value is an integer
f.hex()               # Convert float to hexadecimal
f.as_integer_ratio()  # Return numerator and denominator
float.fromhex('0x1.5000000000000p+3')  # Hexadecimal to float

# ==================================================
# 3. COMPLEX
# ==================================================

c = 2 + 3j

c.real                # Real part
c.imag                # Imaginary part
c.conjugate()         # Conjugate of complex number

# ==================================================
# 4. BOOLEAN
# ==================================================

a = True
b = False

bool(1)               # True
bool(0)               # False
# Boolean has no special methods (it is a subclass of int)

# ==================================================
# 5. STRING (str)
# ==================================================

s = "hello world"

# Case conversion
s.upper()             # Convert to uppercase
s.lower()             # Convert to lowercase
s.title()             # Title case
s.capitalize()        # Capitalize first letter
s.swapcase()          # Swap upper and lower case

# Remove spaces
s.strip()             # Remove spaces from both ends
s.lstrip()            # Remove left spaces
s.rstrip()            # Remove right spaces

# Split and join
s.split()             # Split by space
s.rsplit()            # Split from right
s.splitlines()        # Split by lines
"-".join(["hello", "world"])  # Join iterable into string

# Searching
s.find("o")           # Find index (returns -1 if not found)
s.rfind("o")          # Find from right
s.index("o")          # Like find but raises error if not found
s.count("l")          # Count occurrences

# Replace
s.replace("world", "PK")  # Replace substring

# Start / End checks
s.startswith("he")
s.endswith("ld")

# Validation methods
s.isalpha()
s.isdigit()
s.isalnum()
s.islower()
s.isupper()
s.isspace()
s.istitle()

# Alignment
s.center(20)
s.ljust(20)
s.rjust(20)
s.zfill(15)

# Formatting
s.format()
s.format_map({})

# Advanced string methods
s.encode()            # Convert string to bytes
s.casefold()          # Aggressive lowercase
s.expandtabs()        # Replace tab with spaces
s.partition(" ")     # Split into 3 parts
s.rpartition(" ")
str.maketrans("aeiou", "12345")  # Create translation table
s.translate(str.maketrans("aeiou", "12345"))

# ==================================================
# 6. LIST
# ==================================================

lst = [1, 2, 3]

# Add elements
lst.append(4)         # Add at end
lst.extend([5, 6])    # Add multiple elements
lst.insert(0, 100)    # Insert at specific index

# Remove elements
lst.remove(100)       # Remove by value
lst.pop()             # Remove last element
lst.clear()           # Remove all elements

# Search
lst.index(2)          # Get index of value
lst.count(2)          # Count occurrences

# Ordering
lst.sort()            # Sort list
lst.reverse()         # Reverse list

# Copy
new_list = lst.copy() # Shallow copy

# ==================================================
# 7. TUPLE
# ==================================================

t = (1, 2, 3, 2)

t.count(2)            # Count value
t.index(3)            # Get index

# ==================================================
# 8. SET
# ==================================================

s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Add and remove
s1.add(10)
s1.update([20, 30])
s1.remove(10)         # Raises error if not found
s1.discard(100)       # No error if not found
s1.pop()              # Remove random element
s1.clear()            # Remove all elements

# Set operations
s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
s1.symmetric_difference(s2)

# Update operations
s1.union_update(s2)
s1.intersection_update(s2)
s1.difference_update(s2)
s1.symmetric_difference_update(s2)

# Relationship checks
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)

# ==================================================
# 9. FROZENSET (Immutable Set)
# ==================================================

fs = frozenset([1, 2, 3])

fs.union([4, 5])
fs.intersection([2, 3])
fs.difference([1])
fs.symmetric_difference([3, 4])

fs.isdisjoint([10])
fs.issubset([1, 2, 3, 4])
fs.issuperset([1])

# ==================================================
# 10. DICTIONARY
# ==================================================

d = {"a": 1, "b": 2}

# Access methods
d.keys()
d.values()
d.items()

# Safe access
d.get("a")             # Returns None if key not found
d.setdefault("c", 3)   # Set default value if key not exists

# Update and remove
d.update({"d": 4})
d.pop("a")
d.popitem()            # Remove last inserted item

# Other methods
d.clear()
d.copy()
dict.fromkeys(["x", "y"], 0)

# ==================================================
# 11. BYTES
# ==================================================

b = b"hello"

b.decode()             # Convert bytes to string
b.count(b"l")
b.find(b"e")
b.replace(b"l", b"x")
b.split()
b.startswith(b"h")

# ==================================================
# END OF FILE
# ==================================================
