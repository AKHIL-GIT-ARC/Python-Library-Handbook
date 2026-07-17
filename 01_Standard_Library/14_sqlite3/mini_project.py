import sqlite3
from pathlib import Path
DB_FILE = Path("database/students.db")
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
connection.commit()

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    cursor.execute("""
    INSERT INTO students(name, age, course)
    VALUES (?, ?, ?)
    """, (name, age, course))
    connection.commit()
    print("Student Added Successfully.")

def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if not students:
        print("No Student Records Found.")
        return
    print("\nStudent Records\n")
    for student in students:
        print(student)

def search_student():
    student_id = int(input("Enter Student ID: "))
    cursor.execute("""
    SELECT * FROM students
    WHERE id = ?
    """, (student_id,))
    student = cursor.fetchone()
    if student:
        print(student)
    else:
        print("Student Not Found.")

def update_student():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    course = input("Enter New Course: ")
    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (name, age, course, student_id))
    connection.commit()
    if cursor.rowcount:
        print("Student Updated Successfully.")
    else:
        print("Student Not Found.")

def delete_student():
    student_id = int(input("Enter Student ID: "))
    cursor.execute("""
    DELETE FROM students
    WHERE id=?
    """, (student_id,))
    connection.commit()
    if cursor.rowcount:
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")


while True:

    print("\n" + "=" * 40)
    print("     STUDENT DATABASE MANAGER")
    print("=" * 40)
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
        connection.close()
        print("\nDatabase Closed.")
        print("Thank you for using Student Database Manager!")
        break
    else:
        print("Invalid Choice!")