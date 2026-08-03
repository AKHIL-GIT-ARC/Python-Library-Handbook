# File Paths - Examples

import os

# -------------------------------
# 1. Current Working Directory
# -------------------------------
print("1. Current Working Directory")
print(os.getcwd())

# -------------------------------
# 2. Change Working Directory
# -------------------------------
print("\n2. Change Working Directory")
# Change the path according to your system
# os.chdir(r"C:\Users\Akhil\Documents")
# print(os.getcwd())

# -------------------------------
# 3. Check Path Exists
# -------------------------------
print("\n3. Path Exists")
print(os.path.exists("notes.txt"))
print(os.path.exists("demo.txt"))

# -------------------------------
# 4. Check File
# -------------------------------
print("\n4. Is File?")
print(os.path.isfile("notes.txt"))
print(os.path.isfile("sample_folder"))

# -------------------------------
# 5. Check Directory
# -------------------------------
print("\n5. Is Directory?")
print(os.path.isdir("sample_folder"))
print(os.path.isdir("notes.txt"))

# -------------------------------
# 6. Relative Path
# -------------------------------
print("\n6. Relative Path")
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

# -------------------------------
# 7. Absolute Path
# -------------------------------
print("\n7. Absolute Path")
absolute_path = os.path.abspath("notes.txt")
print(absolute_path)

# -------------------------------
# 8. File Name from Path
# -------------------------------
print("\n8. File Name")
print(os.path.basename(absolute_path))

# -------------------------------
# 9. Folder Name from Path
# -------------------------------
print("\n9. Folder Name")
print(os.path.dirname(absolute_path))