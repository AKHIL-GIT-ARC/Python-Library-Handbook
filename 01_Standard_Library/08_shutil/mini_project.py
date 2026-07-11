import shutil
from pathlib import Path
WORKSPACE = Path("practice_files")
SOURCE = WORKSPACE / "source"
DESTINATION = WORKSPACE / "destination"
BACKUP = WORKSPACE / "backup"
BACKUP.mkdir(exist_ok=True)

def copy_file():
    filename = input("Enter file name: ")
    source_file = SOURCE / filename
    destination_file = DESTINATION / filename
    if source_file.exists():
        shutil.copy(source_file, destination_file)
        print("File copied successfully.")
    else:
        print("File not found.")

def move_file():
    filename = input("Enter file name: ")
    source_file = DESTINATION / filename
    destination_file = BACKUP / filename
    if source_file.exists():
        shutil.move(source_file, destination_file)
        print("File moved successfully.")
    else:
        print("File not found.")

def copy_folder():
    backup_folder = WORKSPACE / "source_backup"
    if backup_folder.exists():
        print("Backup folder already exists.")
    else:
        shutil.copytree(SOURCE, backup_folder)
        print("Folder copied successfully.")

def delete_folder():
    folder = input("Enter folder name: ")
    folder_path = WORKSPACE / folder
    if folder_path.exists():
        shutil.rmtree(folder_path)
        print("Folder deleted successfully.")
    else:
        print("Folder not found.")

def create_zip():
    archive = BACKUP / "project_backup"
    shutil.make_archive(str(archive), "zip", SOURCE)
    print("ZIP archive created successfully.")

def extract_zip():
    zip_file = BACKUP / "project_backup.zip"
    extract_folder = WORKSPACE / "restored"
    if zip_file.exists():
        if not extract_folder.exists():
            shutil.unpack_archive(zip_file, extract_folder)
            print("Archive extracted successfully.")
        else:
            print("Restore folder already exists.")
    else:
        print("ZIP archive not found.")

def disk_usage():
    usage = shutil.disk_usage(Path.cwd())
    print("\nDisk Usage")
    print(f"Total : {usage.total // (1024 ** 3)} GB")
    print(f"Used  : {usage.used // (1024 ** 3)} GB")
    print(f"Free  : {usage.free // (1024 ** 3)} GB")

def find_python():
    print("\nPython Executable")
    print(shutil.which("python"))


while True:
    print("\n" + "=" * 30)
    print("      BACKUP MANAGER PRO")
    print("=" * 30)
    print("1. Copy File")
    print("2. Move File")
    print("3. Copy Folder")
    print("4. Delete Folder")
    print("5. Create ZIP Backup")
    print("6. Extract ZIP Backup")
    print("7. Disk Usage")
    print("8. Find Python Location")
    print("9. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        copy_file()
    elif choice == "2":
        move_file()
    elif choice == "3":
        copy_folder()
    elif choice == "4":
        delete_folder()
    elif choice == "5":
        create_zip()
    elif choice == "6":
        extract_zip()
    elif choice == "7":
        disk_usage()
    elif choice == "8":
        find_python()
    elif choice == "9":
        print("\nThank you for using Backup Manager Pro!")
        break
    else:
        print("Invalid Choice! Please try again.")