"""
mini_project.py
Module: logging

Student Management Logger
"""

import logging
# Configure logging
logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
students = []
def add_student():
    name = input("Enter student name: ")
    students.append(name)
    logging.info(f"Student Added: {name}")
    print("Student added successfully.")

def update_student():
    if not students:
        print("No students available.")
        return
    print("\nStudent List")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")
    try:
        choice = int(input("Select student number: ")) - 1
        if 0 <= choice < len(students):
            new_name = input("Enter new name: ")
            old_name = students[choice]
            students[choice] = new_name
            logging.info(f"Student Updated: {old_name} -> {new_name}")
            print("Student updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def delete_student():
    if not students:
        print("No students available.")
        return
    print("\nStudent List")
    for i, student in enumerate(students, start=1):
        print(f"{i}. {student}")
    try:
        choice = int(input("Select student number: ")) - 1
        if 0 <= choice < len(students):
            removed = students.pop(choice)
            logging.warning(f"Student Deleted: {removed}")
            print("Student deleted successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def view_students():
    print("\nCurrent Students")
    if not students:
        print("No students available.")
        return
    for student in students:
        print("-", student)

def view_log():
    print("\n========= student.log =========\n")
    try:
        with open("student.log", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No log file found.")

while True:
    print("\n" + "=" * 30)
    print("    STUDENT MANAGEMENT LOGGER")
    print("=" * 30)
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Students")
    print("5. View Log File")
    print("6. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        update_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        view_students()
    elif choice == "5":
        view_log()
    elif choice == "6":
        logging.info("Application Closed")
        print("Thank You!")
        break
    else:
        logging.error("Invalid Menu Choice")
        print("Invalid choice.")