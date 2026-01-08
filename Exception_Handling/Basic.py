# x = 10 / 0
# print(x)
# Program crash


'''
try:
    # risky code
except:
    # error vandha run aagum

'''
try:
    x = int(input("Enter number: "))
    print(10 / 0) 
except:
    print("Error occurred") # this is run


try:
    a =[1,2,3,4,5,67]
    print(max(a))
except:
    print("failed")