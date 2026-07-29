"""
mini_project.py
Module: File Basics

Mini Project:
Student Record File Manager
"""
FILE_NAME = "student_records.txt"
# -----------------------------------------
# 1. Create / Reset Record File
# -----------------------------------------
def create_file() -> None:
    with open(
        FILE_NAME,
        "w",
        encoding="utf-8"
    ) as file:
        file.write("       STUDENT RECORDS\n")
        file.write("=" * 30 + "\n")
    print("Student record file created.")


# -----------------------------------------
# 2. Add Student Record
# -----------------------------------------
def add_student(
    name: str,
    roll_no: int,
    marks: float
) -> None:
    with open(
        FILE_NAME,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(f"Name: {name}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Marks: {marks}\n")
        file.write("-" * 20 + "\n")
    print(f"Record added for {name}.")

# -----------------------------------------
# 3. Display All Records
# -----------------------------------------
def display_records() -> None:
    try:
        with open(
            FILE_NAME,
            "r",
            encoding="utf-8"
        ) as file:
            content = file.read()
        print("\n" + "=" * 30)
        print("     ALL STUDENT RECORDS")
        print("=" * 30)
        print(content)
    except FileNotFoundError:
        print("Record file does not exist.")

# -----------------------------------------
# Main Program
# -----------------------------------------
create_file()
add_student(
    "Akhil",
    8053,
    88.5
)
add_student(
    "Charan",
    8124,
    92
)
add_student(
    "Om",
    8000,
    85.5
)
display_records()