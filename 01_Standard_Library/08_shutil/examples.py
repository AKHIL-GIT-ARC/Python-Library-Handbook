import shutil
from pathlib import Path

print("===== Shutil Module Examples =====")

workspace = Path("practice_files")
source = workspace / "source"
destination = workspace / "destination"
backup = workspace / "backup"

# ---------------------------------------
# 1. Copy a File
# ---------------------------------------

print("\n1. Copy File")

source_file = source / "sample.txt"
destination_file = destination / "sample.txt"
shutil.copy(source_file, destination_file)
print("File Copied Successfully")

# ---------------------------------------
# 2. Copy File with Metadata
# ---------------------------------------

print("\n2. Copy File with Metadata")
source_file = source / "notes.txt"
destination_file = destination / "notes_copy.txt"
shutil.copy2(source_file, destination_file)
print("File Copied with Metadata")

# ---------------------------------------
# 3. Move a File
# ---------------------------------------

print("\n3. Move File")
source_file = destination / "sample.txt"
moved_file = backup / "sample.txt"
shutil.move(source_file, moved_file)
print("File Moved Successfully")

# ---------------------------------------
# 4. Copy an Entire Folder
# ---------------------------------------

print("\n4. Copy Folder")
source_folder = source
destination_folder = workspace / "source_backup"
if not destination_folder.exists():
    shutil.copytree(source_folder, destination_folder)
    print("Folder Copied Successfully")
else:
    print("Backup Folder Already Exists")

# ---------------------------------------
# 5. Disk Usage
# ---------------------------------------

print("\n5. Disk Usage")
usage = shutil.disk_usage(Path.cwd())
print(f"Total : {usage.total // (1024**3)} GB")
print(f"Used  : {usage.used // (1024**3)} GB")
print(f"Free  : {usage.free // (1024**3)} GB")

# ---------------------------------------
# 6. Create ZIP Archive
# ---------------------------------------

print("\n6. Create ZIP Archive")
archive = backup / "project_backup"
shutil.make_archive(str(archive), "zip", source)
print("ZIP Archive Created")

# ---------------------------------------
# 7. Extract ZIP Archive
# ---------------------------------------

print("\n7. Extract ZIP Archive")
zip_file = backup / "project_backup.zip"
extract_folder = workspace / "extracted"
if not extract_folder.exists():
    shutil.unpack_archive(zip_file, extract_folder)
    print("Archive Extracted")
else:
    print("Extract Folder Already Exists")

# ---------------------------------------
# 8. Locate an Executable
# ---------------------------------------

print("\n8. Find Executable")
python_path = shutil.which("python")
print("Python Location:")
print(python_path)