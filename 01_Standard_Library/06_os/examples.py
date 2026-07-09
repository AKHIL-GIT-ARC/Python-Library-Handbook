import os

print("===== OS Module Examples =====")

# ---------------------------------------
# 1. Current Working Directory
# ---------------------------------------

print("\n1. Current Working Directory")
print(os.getcwd())

# ---------------------------------------
# 2. List Files & Folders
# ---------------------------------------

print("\n2. Files & Folders")
items = os.listdir()
for item in items:
    print(item)

# ---------------------------------------
# 3. Create a Folder
# ---------------------------------------

print("\n3. Create Folder")
folder = "practice_files/demo_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder Created")
else:
    print("Folder Already Exists")

# ---------------------------------------
# 4. Create Nested Folders
# ---------------------------------------

print("\n4. Create Nested Folders")
nested = "practice_files/python/os"
if not os.path.exists(nested):
    os.makedirs(nested)
    print("Nested Folders Created")
else:
    print("Folders Already Exist")

# ---------------------------------------
# 5. Rename a Folder
# ---------------------------------------

print("\n5. Rename Folder")
old_name = "practice_files/demo_folder"
new_name = "practice_files/my_folder"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("Folder Renamed")
else:
    print("Source Folder Not Found")

# ---------------------------------------
# 6. Check Path Exists
# ---------------------------------------

print("\n6. Check Path")
path = "practice_files/my_folder"
print("Exists :", os.path.exists(path))
print("Is File:", os.path.isfile(path))
print("Is Dir :", os.path.isdir(path))

# ---------------------------------------
# 7. Join Paths
# ---------------------------------------

print("\n7. Join Paths")
joined_path = os.path.join("practice_files", "notes.txt")
print(joined_path)

# ---------------------------------------
# 8. Environment Variables
# ---------------------------------------

print("\n8. Environment Variables")
print("Username:", os.environ.get("USERNAME"))
print("Home:", os.environ.get("USERPROFILE"))