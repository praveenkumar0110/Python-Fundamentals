'''
Method 1: Using *args (many values)----------------------------important Note
📌 Use case

👉 You don’t know how many numbers the user will pass.
'''

def add(*args):
    total = 0
    for num in args:
        total += num
    print("Sum is:", total)
add(10, 20, 30)  # Output: Sum is: 60
add(5, 15, 25, 35, 45)  # Output



'''
🔵 Method 2: Using **kwargs (optional settings)------------------- important
📌 Use case

👉 You want optional named data (user info, config).
'''

def show_user(**details):
    print("name",details.get("Name"))
    print("age",details.get("Age"))
show_user(Name="praveen",Age = "100")




'''

Super-easy memory line

Numbers only → *args
Names + values → **kwargs
'''