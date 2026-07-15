import json
from pathlib import Path
JSON_FILE = Path("data/students.json")

def load_students():
    with open(JSON_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    with open(JSON_FILE, "w") as file:
        json.dump(students, file, indent=4)

def add_student():
    students = load_students()
    student = {
        "id": int(input("Enter ID: ")),
        "name": input("Enter Name: "),
        "age": int(input("Enter Age: ")),
        "course": input("Enter Course: ")
    }
    students.append(student)
    save_students(students)
    print("Student Added Successfully.")

def view_students():
    students = load_students()
    if not students:
        print("No Student Records Found.")
        return
    print("\nStudent Records")
    for student in students:
        print(student)

def search_student():
    students = load_students()
    name = input("Enter Student Name: ")
    for student in students:
        if student["name"].lower() == name.lower():
            print(student)
            return
    print("Student Not Found.")

def update_student():
    students = load_students()
    student_id = int(input("Enter Student ID: "))
    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            save_students(students)
            print("Student Updated Successfully.")
            return
    print("Student Not Found.")

def delete_student():
    students = load_students()
    student_id = int(input("Enter Student ID: "))
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student Deleted Successfully.")
            return
    print("Student Not Found.")

while True:
    print("\n" + "=" * 35)
    print("       STUDENT RECORD MANAGER")
    print("=" * 35)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("\nThank you for using Student Record Manager!")
        break
    else:
        print("Invalid Choice! Please try again.")