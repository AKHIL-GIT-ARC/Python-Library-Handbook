import os

print("===== OS Module Practice =====")

# ---------------------------------------
# 1. Display Current Directory
# ---------------------------------------

print("\n1. Current Working Directory")
print(os.getcwd())

# ---------------------------------------
# 2. List Files & Folders
# ---------------------------------------

print("\n2. Files & Folders")
for item in os.listdir():
    print(item)

# ---------------------------------------
# 3. Create a Folder
# ---------------------------------------

print("\n3. Create Folder")
folder = "practice_files/test_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder Created")
else:
    print("Folder Already Exists")

# ---------------------------------------
# 4. Create Nested Folders
# ---------------------------------------

print("\n4. Create Nested Folders")
nested_folder = "practice_files/project/python"
if not os.path.exists(nested_folder):
    os.makedirs(nested_folder)
    print("Nested Folders Created")
else:
    print("Folders Already Exist")

# ---------------------------------------
# 5. Rename Folder
# ---------------------------------------

print("\n5. Rename Folder")
old_name = "practice_files/test_folder"
new_name = "practice_files/my_folder"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("Folder Renamed")
else:
    print("Source Folder Not Found")

# ---------------------------------------
# 6. Check Path
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
joined_path = os.path.join(
    "practice_files",
    "documents",
    "notes.txt"
)
print(joined_path)

# ---------------------------------------
# 8. Display Environment Variables
# ---------------------------------------

print("\n8. Environment Variables")
print("Username :", os.environ.get("USERNAME"))
print("Home Path:", os.environ.get("USERPROFILE"))

# ---------------------------------------
# 9. Delete Empty Folder
# ---------------------------------------

print("\n9. Delete Folder")
folder = "practice_files/my_folder"
if os.path.exists(folder):
    os.rmdir(folder)
    print("Folder Deleted")
else:
    print("Folder Not Found")

# ---------------------------------------
# 10. Delete Nested Folders
# ---------------------------------------
print("\n10. Delete Nested Folders")
nested = "practice_files/project/python"
if os.path.exists(nested):
    os.removedirs(nested)
    print("Nested Folders Deleted")
else:
    print("Folders Not Found")