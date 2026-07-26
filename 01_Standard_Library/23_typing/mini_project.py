"""
mini_project.py
Module: typing
Student Record Validator using Python type hints.
"""
from typing import Literal

# -----------------------------------------
# Type Alias
# -----------------------------------------
Department = Literal["CSE", "ECE", "ME", "CE"]

# -----------------------------------------
# Calculate Average
# -----------------------------------------
def calculate_average(marks: list[int]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

# -----------------------------------------
# Validate Age
# -----------------------------------------
def validate_age(age: int) -> bool:
    return 0 < age <= 100

# -----------------------------------------
# Validate Marks
# -----------------------------------------
def validate_marks(marks: list[int]) -> bool:
    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    return True

# -----------------------------------------
# Create Student
# -----------------------------------------
def create_student(
    name: str,
    age: int,
    department: Department,
    marks: list[int]
) -> dict[str, object]:
    return {
        "name": name,
        "age": age,
        "department": department,
        "marks": marks
    }

# -----------------------------------------
# Display Student
# -----------------------------------------
def display_student(
    student: dict[str, object]
) -> None:
    print("\n" + "=" * 20)
    print("  STUDENT RECORD")
    print("=" * 20)
    print("Name       :", student["name"])
    print("Age        :", student["age"])
    print("Department :", student["department"])
    print("Marks      :", student["marks"])

# -----------------------------------------
# Main Program
# -----------------------------------------
name: str = input("Enter student name: ")
try:
    age: int = int(
        input("Enter student age: ")
    )
except ValueError:
    print("Age must be an integer.")
    raise SystemExit
department: str = input(
    "Enter department (CSE/ECE/ME/CE): "
).upper()
if department not in ["CSE", "ECE", "ME", "CE"]:
    print("Invalid department.")
    raise SystemExit
try:
    marks: list[int] = list(
        map(
            int,
            input(
                "Enter marks separated by spaces: "
            ).split()
        )
    )
except ValueError:
    print("Marks must contain integers only.")
    raise SystemExit

# -----------------------------------------
# Validation
# -----------------------------------------
if not validate_age(age):
    print("Invalid age.")
    raise SystemExit
if not validate_marks(marks):
    print("Marks must be between 0 and 100.")
    raise SystemExit

# -----------------------------------------
# Create Record
# -----------------------------------------
student = create_student(
    name,
    age,
    department,  # type: ignore[arg-type]
    marks
)

# -----------------------------------------
# Display Result
# -----------------------------------------
display_student(student)
average: float = calculate_average(marks)
print("Average    :", round(average, 2))
print("\nRecord created successfully!")