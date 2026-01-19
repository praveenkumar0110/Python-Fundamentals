def count(n):
    if n == 0:        # BASE CASE
        return
    print(n)
    count(n - 1)      # RECURSIVE CASE
count(6)

# explaination
# The function count is defined to take a single argument n.
# It checks if n is 0 (the base case). If so, it returns without doing anything.
# If n is not 0, it prints the value of n and then calls itself with n - 1 (the recursive case).
# until n reaches 0, at which point the recursion stops.


