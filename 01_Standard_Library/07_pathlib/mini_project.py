from pathlib import Path

WORKSPACE = Path("practice_files")
WORKSPACE.mkdir(exist_ok=True)

def show_current_directory():
    print("\nCurrent Directory:")
    print(Path.cwd())

def show_home_directory():
    print("\nHome Directory:")
    print(Path.home())


def list_workspace():
    print("\nWorkspace Contents")
    items = list(WORKSPACE.iterdir())
    if not items:
        print("Workspace is empty.")
        return
    for item in items:
        if item.is_dir():
            print(f"[DIR]  {item.name}")
        else:
            print(f"[FILE] {item.name}")


def create_folder():
    folder = input("Folder Name: ")
    path = WORKSPACE / folder
    if path.exists():
        print("Folder already exists.")
    else:
        path.mkdir()
        print("Folder created successfully.")


def rename_item():
    old_name = input("Current Name: ")
    new_name = input("New Name: ")
    old_path = WORKSPACE / old_name
    new_path = WORKSPACE / new_name
    if old_path.exists():
        old_path.rename(new_path)
        print("Renamed successfully.")
    else:
        print("Item not found.")


def create_file():
    filename = input("File Name: ")
    file = WORKSPACE / filename
    if file.exists():
        print("File already exists.")
    else:
        file.touch()
        print("File created successfully.")


def delete_file():
    filename = input("File Name: ")
    file = WORKSPACE / filename
    if file.exists() and file.is_file():
        file.unlink()
        print("File deleted.")
    else:
        print("File not found.")


def delete_folder():
    folder = input("Folder Name: ")
    path = WORKSPACE / folder
    if path.exists() and path.is_dir():
        path.rmdir()
        print("Folder deleted.")
    else:
        print("Folder not found or not empty.")


def search_files():
    extension = input("Enter extension (txt, py, jpg): ").strip(".")
    files = list(WORKSPACE.glob(f"*.{extension}"))
    if not files:
        print("No matching files found.")
        return
    print("\nMatching Files")
    for file in files:
        print(file.name)


def file_information():
    filename = input("Enter File Name: ")
    file = WORKSPACE / filename
    if file.exists():
        print("\nFile Information")
        print("Name      :", file.name)
        print("Stem      :", file.stem)
        print("Extension :", file.suffix)
        print("Parent    :", file.parent)
        print("Exists    :", file.exists())
        print("Is File   :", file.is_file())
        print("Size      :", file.stat().st_size, "bytes")
    else:
        print("File not found.")


while True:
    print("\n" + "=" * 30)
    print("     MODERN FILE EXPLORER")
    print("=" * 30)
    print("1. Show Current Directory")
    print("2. Show Home Directory")
    print("3. List Workspace")
    print("4. Create Folder")
    print("5. Rename Folder/File")
    print("6. Create File")
    print("7. Delete File")
    print("8. Delete Folder")
    print("9. Search Files")
    print("10. File Information")
    print("11. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        show_current_directory()
    elif choice == "2":
        show_home_directory()
    elif choice == "3":
        list_workspace()
    elif choice == "4":
        create_folder()
    elif choice == "5":
        rename_item()
    elif choice == "6":
        create_file()
    elif choice == "7":
        delete_file()
    elif choice == "8":
        delete_folder()
    elif choice == "9":
        search_files()
    elif choice == "10":
        file_information()
    elif choice == "11":
        print("\nThank you for using Modern File Explorer!")
        break
    else:
        print("Invalid Choice! Please try again.")