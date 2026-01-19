'''
To  use Python-la file path handle
import os
'''
'''
os.path.isfile("test.txt")   # File ah?
os.path.isdir("myfolder")    # Folder ah?
'''

import os

path= "test.txt"

if os.path.exists(path):
    if os.path.isfile(path):
        print("file is there")
    elif os.path.isdir(path):
        print("this is folder")
else:
    print("path is  not there")
    

'''
🏁 FINAL SUMMARY
os.path.exists()

👉 Path irukka-nu check

os.path.isfile()

👉 File ah?

os.path.isdir()

👉 Folder ah?

os.getcwd()

👉 Python enga irundhu run aagudhu
'''



# data manipulate -----importnat 

pk = open("data.txt" ,"r")

for line in pk:
    print(line)
pk.close()


#Proper way (with keyword)
with open ("data.txt" ,"r") as f:
    data = f.read()
    print(data)

# "r" is read----------------
    
#File-la write pannradhu

with open("data.txt", "w") as f:
    f.write("hello world\n")
    f.write("File handling\n")
    
# "w" is wirte-------------------
    
    
# STEP 5: Append (old data delete aagadhu)
with open("data.txt","a") as f:
    f.write("apple\n")
    f.write("Mango\n")
    
# "a" is append----------------



#Numbers sum pannradhu

total = 0
with open("marks.txt" ,"r") as f:
    for line in f:
        total+= int(line.strip())
print("total",total)

# Duplicate remove pannradhu
unique_words = set()
with open("data.txt" , "r") as f:
     for line in f:
         unique_words.add(line.strip())
print(unique_words)


word ="apple"
with open("data.txt","r") as f :
    for line in f:
        if word in line:
            print("found",line.strip())
        else:
            print("not matched")


#STEP 9: New file create panni save pannradhu
with open("data2.txt","w") as f:
    f.write("myfolder\n")
    f.write("hello  welcome to python world")


# folder create

os.mkdir("data")
print("Folder created")



'''
most important
| Task           | Method          |
| -------------- | --------------- | 
| Read full file | `read()`        |
| Line by line   | `for line in f` |
| Write          | `"w"`           |
| Append         | `"a"`           |
| Replace        | `replace()`     |
| Clean data     | `strip()`       |
csv file handling use pandas lib

'''
 