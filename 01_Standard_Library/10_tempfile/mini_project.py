import tempfile
import os

def show_temp_directory():
    print("\nSystem Temporary Directory")
    print(tempfile.gettempdir())

def create_temp_file():
    with tempfile.TemporaryFile(mode="w+t") as file:
        print(file.name)
        file.write("Hello from Temporary File!")
        file.seek(0)
        print("\nTemporary File Content")
        print(file.read())
    print("Temporary File Deleted Automatically.")

def create_named_temp_file():
    with tempfile.NamedTemporaryFile(mode="w+t") as file:
        print("\nFile Name")
        print(file.name)
        file.write("Named Temporary File")
        file.seek(0)
        print(file.read())
    print("Named Temporary File Deleted Automatically.")

def create_temp_directory():
    with tempfile.TemporaryDirectory() as folder:
        print("\nTemporary Directory")
        print(folder)
    print("Temporary Directory Deleted Automatically.")

def write_temp_notes():
    note = input("\nEnter Your Note: ")
    with tempfile.NamedTemporaryFile(mode="w+t") as file:
        file.write(note)
        file.seek(0)
        print("\nSaved Note")
        print(file.read())
    print("Temporary Note Deleted.")

def create_secure_temp_file():
    fd, path = tempfile.mkstemp()
    print("\nSecure Temporary File")
    print("File Descriptor :", fd)
    print("File Path       :", path)
    os.close(fd)
    os.remove(path)
    print("Secure Temporary File Deleted.")


while True:
    print("\n" + "=" * 35)
    print("     TEMPORARY WORKSPACE MANAGER")
    print("=" * 35)
    print("1. Show Temp Directory")
    print("2. Create Temporary File")
    print("3. Create Named Temporary File")
    print("4. Create Temporary Directory")
    print("5. Write Temporary Notes")
    print("6. Create Secure Temporary File")
    print("7. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        show_temp_directory()
    elif choice == "2":
        create_temp_file()
    elif choice == "3":
        create_named_temp_file()
    elif choice == "4":
        create_temp_directory()
    elif choice == "5":
        write_temp_notes()
    elif choice == "6":
        create_secure_temp_file()
    elif choice == "7":
        print("\nThank you for using Temporary Workspace Manager!")
        break
    else:
        print("Invalid Choice! Please try again.")