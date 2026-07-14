import zipfile
from pathlib import Path
print("===== Zipfile Module Examples =====")
workspace = Path("practice_files")
source = workspace / "source"
archives = workspace / "archives"
extracted = workspace / "extracted"
zip_path = archives / "project.zip"

# ---------------------------------------
# 1. Create ZIP Archive
# ---------------------------------------

print("\n1. Create ZIP Archive")
with zipfile.ZipFile(zip_path, "w") as zip_file:
    for file in source.iterdir():
        zip_file.write(file, arcname=file.name)
print("ZIP Archive Created")

# ---------------------------------------
# 2. View ZIP Contents
# ---------------------------------------

print("\n2. ZIP Contents")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    zip_file.printdir()

# ---------------------------------------
# 3. List File Names
# ---------------------------------------

print("\n3. File Names")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    for file in zip_file.namelist():
        print(file)

# ---------------------------------------
# 4. File Information
# ---------------------------------------

print("\n4. File Information")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    for info in zip_file.infolist():
        print(f"{info.filename} ({info.file_size} bytes)")

# ---------------------------------------
# 5. Read File Without Extracting
# ---------------------------------------

print("\n5. Read notes.txt")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    content = zip_file.read("notes.txt")
    print(content.decode())

# ---------------------------------------
# 6. Extract One File
# ---------------------------------------

print("\n6. Extract One File")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    zip_file.extract("notes.txt", extracted)
print("notes.txt Extracted")

# ---------------------------------------
# 7. Extract All Files
# ---------------------------------------

print("\n7. Extract All Files")
with zipfile.ZipFile(zip_path, "r") as zip_file:
    zip_file.extractall(extracted)
print("All Files Extracted")