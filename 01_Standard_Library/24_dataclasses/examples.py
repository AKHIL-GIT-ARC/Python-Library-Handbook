"""
examples.py
Module: dataclasses

"""
from dataclasses import dataclass, field, asdict, astuple, replace
# -----------------------------------------
# 1. Basic Dataclass
# -----------------------------------------
@dataclass
class Student:
    name: str
    age: int
    department: str
student1 = Student("Akhil", 19, "CSE")
print("Student:", student1)

# -----------------------------------------
# 2. Accessing Fields
# -----------------------------------------
print("\nName:", student1.name)
print("Age:", student1.age)
print("Department:", student1.department)

# -----------------------------------------
# 3. Automatic __repr__()
# -----------------------------------------
print("\nObject Representation:")
print(student1)

# -----------------------------------------
# 4. Automatic __eq__()
# -----------------------------------------
student2 = Student("Akhil", 19, "CSE")
student3 = Student("Rahul", 20, "ECE")
print("\nStudent 1 == Student 2:", student1 == student2)
print("Student 1 == Student 3:", student1 == student3)

# -----------------------------------------
# 5. Default Values
# -----------------------------------------
@dataclass
class Employee:
    name: str
    department: str = "IT"
employee1 = Employee("Rahul")
employee2 = Employee("Chitra", "HR")
print("\nEmployee 1:", employee1)
print("Employee 2:", employee2)

# -----------------------------------------
# 6. default_factory
# -----------------------------------------
@dataclass
class Result:
    name: str
    marks: list[int] = field(default_factory=list)
result1 = Result("Akhil")
result2 = Result("Rahul")
result1.marks.append(90)
print("\nResult 1:", result1)
print("Result 2:", result2)

# -----------------------------------------
# 7. __post_init__()
# -----------------------------------------
@dataclass
class Product:
    name: str
    price: float
    quantity: int
    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative")
product = Product(
    "Laptop",
    75000.0,
    2
)
print("\nProduct:", product)

# -----------------------------------------
# 8. Method Inside Dataclass
# -----------------------------------------
@dataclass
class Rectangle:
    length: float
    width: float
    def area(self) -> float:
        return self.length * self.width
rectangle = Rectangle(10, 5)
print("\nRectangle:", rectangle)
print("Area:", rectangle.area())

# -----------------------------------------
# 9. asdict()
# -----------------------------------------
student_dict = asdict(student1)
print("\nDictionary:", student_dict)
print("Name:", student_dict["name"])

# -----------------------------------------
# 10. astuple()
# -----------------------------------------
student_tuple = astuple(student1)
print("\nTuple:", student_tuple)

# -----------------------------------------
# 11. replace()
# -----------------------------------------
student4 = replace(
    student1,
    age=20
)
print("\nOriginal:", student1)
print("Modified Copy:", student4)

# -----------------------------------------
# 12. frozen=True
# -----------------------------------------
@dataclass(frozen=True)
class Account:
    account_id: int
    username: str
account = Account(
    101,
    "akhil"
)
print("\nAccount:", account)
# This would cause an error:
#
# account.username = "rahul"

# -----------------------------------------
# 13. order=True
# -----------------------------------------
@dataclass(order=True)
class Score:
    marks: int
    name: str
score1 = Score(80, "Akhil")
score2 = Score(90, "Rahul")
print("\nScore 1:", score1)
print("Score 2:", score2)
print("Score 1 < Score 2:", score1 < score2)

# -----------------------------------------
# Summary
# -----------------------------------------
print("\n" + "=" * 30)
print(" DATACLASSES MODULE EXAMPLES")
print("=" * 30)
print("""
✓ Basic Dataclass
✓ Fields
✓ Automatic __repr__()
✓ Automatic __eq__()
✓ Default Values
✓ field()
✓ default_factory
✓ __post_init__()
✓ Methods
✓ asdict()
✓ astuple()
✓ replace()
✓ frozen=True
✓ order=True
""")