from pathlib import Path

print("===== Pathlib Module Practice =====")

# ---------------------------------------
# 1. Current & Home Directory
# ---------------------------------------

print("\n1. Directories")
print("Current:", Path.cwd())
print("Home   :", Path.home())

# ---------------------------------------
# 2. Create Path Object
# ---------------------------------------

print("\n2. Path Object")
path = Path("practice_files/example.txt")
print(path)

# ---------------------------------------
# 3. Path Information
# ---------------------------------------

print("\n3. Path Information")
print("Name   :", path.name)
print("Stem   :", path.stem)
print("Suffix :", path.suffix)
print("Parent :", path.parent)

# ---------------------------------------
# 4. Check Path
# ---------------------------------------

print("\n4. Path Check")
print("Exists :", path.exists())
print("Is File:", path.is_file())
print("Is Dir :", path.is_dir())

# ---------------------------------------
# 5. Create Folder
# ---------------------------------------

print("\n5. Create Folder")
folder = Path("practice_files/test_folder")
if not folder.exists():
    folder.mkdir()
    print("Folder Created")
else:
    print("Folder Already Exists")

# ---------------------------------------
# 6. Rename Folder
# ---------------------------------------

print("\n6. Rename Folder")
new_folder = Path("practice_files/my_folder")
if folder.exists():
    folder.rename(new_folder)
    print("Folder Renamed")
else:
    print("Folder Not Found")

# ---------------------------------------
# 7. List Workspace
# ---------------------------------------

print("\n7. Workspace Contents")
workspace = Path("practice_files")
for item in workspace.iterdir():
    print(item.name)

# ---------------------------------------
# 8. Search Text Files
# ---------------------------------------

print("\n8. Search .txt Files")
for file in workspace.glob("*.txt"):
    print(file.name)

# ---------------------------------------
# 9. Recursive Search
# ---------------------------------------

print("\n9. Recursive Search")
for item in workspace.rglob("*"):
    print(item)

# ---------------------------------------
# 10. Delete Folder
# ---------------------------------------

print("\n10. Delete Folder")
if new_folder.exists():
    new_folder.rmdir()
    print("Folder Deleted")
else:
    print("Folder Not Found")