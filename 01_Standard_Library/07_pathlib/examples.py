# os.path.exists(path)  →  Path.exists()
# os.listdir()          →  Path.iterdir()
# os.remove()           →  Path.unlink()
from pathlib import Path

print("===== Pathlib Module Examples =====")

# ---------------------------------------
# 1. Create Path Object
# ---------------------------------------

print("\n1. Create Path Object")
path = Path("practice_files")
print(path)

# ---------------------------------------
# 2. Current Working Directory
# ---------------------------------------

print("\n2. Current Working Directory")
print(Path.cwd())

# ---------------------------------------
# 3. Home Directory
# ---------------------------------------

print("\n3. Home Directory")
print(Path.home())

# ---------------------------------------
# 4. Path Components
# ---------------------------------------

print("\n4. Path Components")
file = Path("practice_files/example.txt")
print("Name   :", file.name)
print("Stem   :", file.stem)
print("Suffix :", file.suffix)
print("Parent :", file.parent)

# ---------------------------------------
# 5. Check Path
# ---------------------------------------

print("\n5. Path Information")
print("Exists :", file.exists())
print("Is File:", file.is_file())
print("Is Dir :", file.is_dir())

# ---------------------------------------
# 6. Create Folder
# ---------------------------------------

print("\n6. Create Folder")
folder = Path("practice_files/demo_folder")
if not folder.exists():
    folder.mkdir()
    print("Folder Created")
else:
    print("Folder Already Exists")

# ---------------------------------------
# 7. Rename Folder
# ---------------------------------------

print("\n7. Rename Folder")
new_folder = Path("practice_files/my_folder")
if folder.exists():
    folder.rename(new_folder)
    print("Folder Renamed")
else:
    print("Folder Not Found")

# ---------------------------------------
# 8. Iterate Directory
# ---------------------------------------

print("\n8. List Files & Folders")
workspace = Path("practice_files")
for item in workspace.iterdir():
    print(item.name)

# ---------------------------------------
# 9. Search Files
# ---------------------------------------

print("\n9. Search Python Files")
for file in workspace.glob("*.py"):
    print(file.name)

# ---------------------------------------
# 10. Recursive Search
# ---------------------------------------

print("\n10. Recursive Search")
for file in workspace.rglob("*"):
    print(file)