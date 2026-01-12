'''

Python file
   ↓
MongoDB server connect
   ↓
Database select
   ↓
Collection select
   ↓
find() / find_one()
'''

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ICD10"]
collection = db["Categories"]

#FIRST DATA READ (MOST IMPORTANT 🔥)
# for doc in collection.find():
#     print(doc)
    
# for doc in collection.find():
#       print(
#         doc["_id"],
#         doc["letter_range"],
#         doc["total_codes_count"]
#     )

# for doc in collection.find():
#     for code in doc["codes_list"]:
#         print(code["description"])


# for doc in collection.find():
#     print(doc["_id"],print(["letter_range"]))



#array-ah loop pannradhu (FOUNDATION)

# for doc in collection.find():
#     for code in doc["codes_list"]:
#         print(code ["code"], code["description"])
        
        
#Safe + Clean version (BEST PRACTICE 💯)

# for doc in collection.find():
#     for code in doc.get("codes_list",[]):
#         pk = code.get("code","N/A")
#         desc = code.get("description","N/A")
#         print(pk, desc)


doc = collection.find_one(
    {"codes_list.code": "A00"},
    {"codes_list.$": 1, "_id": 0}
)

print(doc)
