"""
mini_project.py
Module: dataclasses
Student Record Manager using dataclasses.
"""
from dataclasses import dataclass, field, asdict

# -----------------------------------------
# Student Dataclass
# -----------------------------------------
@dataclass
class Student:
    roll_no: int
    name: str
    department: str
    marks: list[int] = field(default_factory=list)

    # -------------------------------------
    # Validation
    # -------------------------------------
    def __post_init__(self) -> None:
        if self.roll_no <= 0:
            raise ValueError(
                "Roll number must be greater than 0."
            )
        if not self.name.strip():
            raise ValueError(
                "Name cannot be empty."
            )
        for mark in self.marks:
            if mark < 0 or mark > 100:
                raise ValueError(
                    "Marks must be between 0 and 100."
                )

    # -------------------------------------
    # Calculate Average
    # -------------------------------------
    def calculate_average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    # -------------------------------------
    # Find Grade
    # -------------------------------------
    def get_grade(self) -> str:
        average = self.calculate_average()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    # -------------------------------------
    # Add Mark
    # -------------------------------------
    def add_mark(self, mark: int) -> None:
        if 0 <= mark <= 100:
            self.marks.append(mark)
        else:
            print("Mark must be between 0 and 100.")

    # -------------------------------------
    # Display Student
    # -------------------------------------
    def display(self) -> None:
        print("\n" + "=" * 20)
        print("   STUDENT RECORD")
        print("=" * 20)
        print("Roll No    :", self.roll_no)
        print("Name       :", self.name)
        print("Department :", self.department)
        print("Marks      :", self.marks)
        print(
            "Average    :",
            round(self.calculate_average(), 2)
        )
        print("Grade      :", self.get_grade())

# -----------------------------------------
# Create Student
# -----------------------------------------
student1 = Student(
    roll_no= 8053,
    name="Akhil",
    department="CSE",
    marks=[85, 90, 88]
)

# -----------------------------------------
# Display Student
# -----------------------------------------
student1.display()

# -----------------------------------------
# Add New Mark
# -----------------------------------------
student1.add_mark(99)
print("\nAfter adding mark:")
student1.display()

# -----------------------------------------
# Convert to Dictionary
# -----------------------------------------
student_data = asdict(student1)
print("\nStudent Dictionary:")
print(student_data)