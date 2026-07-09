import os

WORKSPACE = "practice_files"

# Create workspace if it doesn't exist
os.makedirs(WORKSPACE, exist_ok=True)

def current_directory():
    print("\nCurrent Directory:")
    print(os.getcwd())


def list_items():
    print("\nFiles & Folders:")
    items = os.listdir(WORKSPACE)
    if not items:
        print("Workspace is empty.")
        return
    for item in items:
        path = os.path.join(WORKSPACE, item)
        if os.path.isdir(path):
            print(f"[DIR]  {item}")
        else:
            print(f"[FILE] {item}")


def create_folder():
    folder = input("Folder Name: ")
    path = os.path.join(WORKSPACE, folder)
    if os.path.exists(path):
        print("Folder already exists.")
    else:
        os.mkdir(path)
        print("Folder created successfully.")


def rename_item():
    old = input("Current Name: ")
    new = input("New Name: ")
    old_path = os.path.join(WORKSPACE, old)
    new_path = os.path.join(WORKSPACE, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print("Renamed successfully.")
    else:
        print("Item not found.")


def delete_folder():
    folder = input("Folder Name: ")
    path = os.path.join(WORKSPACE, folder)
    if os.path.isdir(path):
        os.rmdir(path)
        print("Folder deleted.")
    else:
        print("Folder not found or not empty.")


def create_file():
    filename = input("File Name: ")
    path = os.path.join(WORKSPACE, filename)
    if os.path.exists(path):
        print("File already exists.")
    else:
        with open(path, "w") as file:
            file.write("")

        print("File created successfully.")


def delete_file():
    filename = input("File Name: ")
    path = os.path.join(WORKSPACE, filename)
    if os.path.isfile(path):
        os.remove(path)
        print("File deleted.")
    else:
        print("File not found.")


def check_path():
    name = input("Enter File/Folder Name: ")
    path = os.path.join(WORKSPACE, name)
    print("\nPath Exists :", os.path.exists(path))
    print("Is File     :", os.path.isfile(path))
    print("Is Directory:", os.path.isdir(path))


while True:
    print("\n" + "=" * 30)
    print("         FILE MANAGER")
    print("=" * 30)
    print("1. Current Directory")
    print("2. List Files & Folders")
    print("3. Create Folder")
    print("4. Rename File/Folder")
    print("5. Delete Folder")
    print("6. Create File")
    print("7. Delete File")
    print("8. Check Path")
    print("9. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        current_directory()
    elif choice == "2":
        list_items()
    elif choice == "3":
        create_folder()
    elif choice == "4":
        rename_item()
    elif choice == "5":
        delete_folder()
    elif choice == "6":
        create_file()
    elif choice == "7":
        delete_file()
    elif choice == "8":
        check_path()
    elif choice == "9":
        print("\nThank you for using File Manager!")
        break
    else:
        print("Invalid Choice!")