"""
examples.py
Module: typing

"""
from typing import Any, Union, Optional, Literal, Callable, TypeAlias
# -----------------------------------------
# 1. Variable Type Hints
# -----------------------------------------
name: str = "Akhil"
age: int = 19
cgpa: float = 8.5
is_student: bool = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)


# -----------------------------------------
# 2. Function Parameter and Return Type
# -----------------------------------------
def add(a: int, b: int) -> int:
    return a + b
print("\nAddition:", add(10, 20))

# -----------------------------------------
# 3. Function Returning None
# -----------------------------------------
def greet(name: str) -> None:
    print(f"Hello, {name}!")
greet("Akhil")

# -----------------------------------------
# 4. List Type Hint
# -----------------------------------------
marks: list[int] = [85, 90, 78, 92]
print("\nMarks:", marks)

# -----------------------------------------
# 5. Dictionary Type Hint
# -----------------------------------------
student: dict[str, str] = {
    "name": "Akhil",
    "department": "CSE"
}
print("Student:", student)

# -----------------------------------------
# 6. Tuple Type Hint
# -----------------------------------------
coordinates: tuple[int, int] = (10, 20)
print("Coordinates:", coordinates)

# -----------------------------------------
# 7. Set Type Hint
# -----------------------------------------
subjects: set[str] = {
    "Python",
    "Java",
    "SQL"
}
print("Subjects:", subjects)

# -----------------------------------------
# 8. Any
# -----------------------------------------
data: Any = 100
print("\nAny:", data)
data = "Python"
print("Any after change:", data)

# -----------------------------------------
# 9. Union
# -----------------------------------------
student_id: Union[int, str] = 101
print("\nStudent ID:", student_id)
student_id = "ST101"
print("Student ID:", student_id)

# -----------------------------------------
# 10. Modern Union Syntax
# -----------------------------------------
roll_number: int | str = 25
print("\nRoll Number:", roll_number)
roll_number = "CSE25"
print("Roll Number:", roll_number)

# -----------------------------------------
# 11. Optional
# -----------------------------------------
email: Optional[str] = None
print("\nEmail:", email)
email = "student@example.com"
print("Email:", email)

# -----------------------------------------
# 12. Modern Optional Syntax
# -----------------------------------------
phone: str | None = None
print("\nPhone:", phone)
phone = "9876543210"
print("Phone:", phone)

# -----------------------------------------
# 13. Literal
# -----------------------------------------
status: Literal["active", "inactive"] = "active"
print("\nStatus:", status)

# -----------------------------------------
# 14. Callable
# -----------------------------------------
def multiply(a: int, b: int) -> int:
    return a * b
operation: Callable[[int, int], int] = multiply
print("\nMultiplication:", operation(5, 4))

# -----------------------------------------
# 15. Type Alias
# -----------------------------------------
StudentID: TypeAlias = int
sid: StudentID = 101
print("\nStudent ID:", sid)

# -----------------------------------------
# 16. Function with List
# -----------------------------------------
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)
scores: list[int] = [80, 90, 70]
print("\nAverage:", calculate_average(scores))

# -----------------------------------------
# 17. Function Returning Dictionary
# -----------------------------------------
def create_student(
    name: str,
    department: str
) -> dict[str, str]:
    return {
        "name": name,
        "department": department
    }
result = create_student("Akhil", "CSE")
print("\nCreated Student:", result)

# -----------------------------------------
# 18. Function with Optional Return
# -----------------------------------------
def find_student(student_id: int) -> str | None:
    if student_id == 101:
        return "Akhil"
    return None
print("\nSearch 101:", find_student(101))
print("Search 999:", find_student(999))

# -----------------------------------------
# Summary
# -----------------------------------------
print("\n" + "=" * 30)
print("   TYPING MODULE EXAMPLES")
print("=" * 30)
print("""
✓ Variable Type Hints
✓ Function Annotations
✓ Return Types
✓ list
✓ dict
✓ tuple
✓ set
✓ Any
✓ Union
✓ Optional
✓ Literal
✓ Callable
✓ TypeAlias
""")