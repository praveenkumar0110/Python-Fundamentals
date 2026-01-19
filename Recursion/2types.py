def count(n):
    if n == 0:        # BASE CASE
        return
    print(n)
    count(n - 1)      # RECURSIVE CASE
count(5)