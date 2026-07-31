# Mini Project - Notes Manager

FILE_NAME = "notes.txt"

# Create / replace notes
def create_notes():
    note = input("Enter your note: ")
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Notes created successfully.")

# Add a new note
def add_note():
    note = input("Enter new note: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Note added successfully.")

# Display all notes
def view_notes():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            notes = file.readlines()
        print("\nYour Notes:")
        for number, note in enumerate(notes, start=1):
            print(f"{number}. {note.strip()}")
    except FileNotFoundError:
        print("No notes found.")

create_notes()
add_note()
view_notes()