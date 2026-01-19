
# basic level recursion to display a tree structure.
# tree = {
#     "name": "A",
#     "children": [
#         {"name": "B", "children": []},
#         {"name": "pk", "children": []}
#     ]
# }

# def show_tree(node):
#     print(node["name"])
#     for child in node["children"]:
#         show_tree(child)
# show_tree(tree)


# LEVEL 2 — MEDIUM TREE RECURSION

# folders = {
#     "name": "C:/",
#     "children": [
#         {
#             "name": "Documents",
#             "children": [
#                 {"name": "resume.pdf", "children": []},
#                 {"name": "notes.txt", "children": []}
#             ]
#         },
#         {
#             "name": "Pictures",
#             "children": [
#                 {"name": "photo1.jpg", "children": []},
#                 {"name": "photo2.png", "children": []}
#             ]
#         }
#     ]
# }


# def desplay_folder(node,indent=0):
#     print("  "* indent + node["name"])
    
#     for child in node["children"]:
#         desplay_folder(child,indent + 1)
        
# desplay_folder(folders)



# LEVEL 3 — ADVANCED TREE (LIKE YOUR ICD10 SCRAPER) RECURSION


categories = {
    "name": "Electronics",
    "children": [
        {
            "name": "Mobiles",
            "children": [
                {"name": "iPhone 15", "children": []},
                {"name": "Samsung S23", "children": []}
            ]
        },
        {
            "name": "Laptops",
            "children": [
                {"name": "Macbook Pro", "children": []},
                {"name": "Dell XPS", "children": []}
            ]
        }
    ]
}

def print_tree(node):
     print(node["name"]);
     for child in node["children"]:
         print_tree(child)
print_tree(categories)