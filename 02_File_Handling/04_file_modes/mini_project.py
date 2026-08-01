# Mini Project - Student Record Manager

FILE_NAME = "students.txt"

def add_students():
    n = int(input("How many students? "))
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for _ in range(n):
            name = input("Enter student name: ")
            file.write(name + "\n")
    print("Student records created successfully.")

def append_student():
    name = input("Enter new student name: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(name + "\n")
    print("Student added successfully.")

def display_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            print("\nStudent List")
            for number, student in enumerate(file, start=1):
                print(f"{number}. {student.strip()}")
    except FileNotFoundError:
        print("No student records found.")

# Main Program
add_students()
append_student()
display_students()