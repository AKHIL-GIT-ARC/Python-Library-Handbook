import zipfile
from pathlib import Path
WORKSPACE = Path("practice_files")
SOURCE = WORKSPACE / "source"
ARCHIVES = WORKSPACE / "archives"
EXTRACTED = WORKSPACE / "extracted"
ARCHIVES.mkdir(exist_ok=True)
EXTRACTED.mkdir(exist_ok=True)
ZIP_FILE = ARCHIVES / "project.zip"

def create_zip():
    with zipfile.ZipFile(ZIP_FILE, "w") as zip_file:
        for file in SOURCE.iterdir():
            zip_file.write(file, arcname=file.name)
    print("ZIP Archive Created Successfully.")

def view_contents():
    if not ZIP_FILE.exists():
        print("ZIP file not found.")
        return
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_file:
        print("\nZIP Contents")
        zip_file.printdir()

def read_file():
    if not ZIP_FILE.exists():
        print("ZIP file not found.")
        return
    filename = input("Enter File Name: ")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_file:
        if filename in zip_file.namelist():
            content = zip_file.read(filename)
            print("\nFile Content")
            print(content.decode())
        else:
            print("File not found inside ZIP.")

def extract_one():
    if not ZIP_FILE.exists():
        print("ZIP file not found.")
        return
    filename = input("Enter File Name: ")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_file:
        if filename in zip_file.namelist():
            zip_file.extract(filename, EXTRACTED)
            print("File Extracted Successfully.")
        else:
            print("File not found.")

def extract_all():
    if not ZIP_FILE.exists():
        print("ZIP file not found.")
        return
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_file:
        zip_file.extractall(EXTRACTED)
    print("All Files Extracted Successfully.")

def file_information():
    if not ZIP_FILE.exists():
        print("ZIP file not found.")
        return
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_file:
        print("\nFile Information")
        for info in zip_file.infolist():
            print(f"{info.filename} - {info.file_size} bytes")


while True:
    print("\n" + "=" * 30)
    print("      ZIP ARCHIVE MANAGER")
    print("=" * 30)
    print("1. Create ZIP Archive")
    print("2. View ZIP Contents")
    print("3. Read File")
    print("4. Extract One File")
    print("5. Extract All Files")
    print("6. Display File Information")
    print("7. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        create_zip()
    elif choice == "2":
        view_contents()
    elif choice == "3":
        read_file()
    elif choice == "4":
        extract_one()
    elif choice == "5":
        extract_all()
    elif choice == "6":
        file_information()
    elif choice == "7":
        print("\nThank you for using ZIP Archive Manager!")
        break
    else:
        print("Invalid Choice! Please try again.")