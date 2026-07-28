"""
examples.py
Module: enum

"""
from enum import Enum, IntEnum, StrEnum, auto, unique
# -----------------------------------------
# 1. Basic Enum
# -----------------------------------------
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
print("Pending:", Status.PENDING)
print("Approved:", Status.APPROVED)
print("Rejected:", Status.REJECTED)

# -----------------------------------------
# 2. Accessing name
# -----------------------------------------
print("\nName:", Status.APPROVED.name)

# -----------------------------------------
# 3. Accessing value
# -----------------------------------------
print("Value:", Status.APPROVED.value)

# -----------------------------------------
# 4. Accessing Member by Name
# -----------------------------------------
status = Status["APPROVED"]
print("\nBy Name:", status)

# -----------------------------------------
# 5. Accessing Member by Value
# -----------------------------------------
status = Status(2)
print("By Value:", status)

# -----------------------------------------
# 6. Iterating Through Enum
# -----------------------------------------
print("\nAll Status Values:")
for status in Status:
    print(status.name, "=", status.value)

# -----------------------------------------
# 7. Comparing Enum Members
# -----------------------------------------
current_status = Status.APPROVED
if current_status == Status.APPROVED:
    print("\nApplication is approved.")

# -----------------------------------------
# 8. auto()
# -----------------------------------------
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
print("\nTask Status:")
for status in TaskStatus:
    print(status.name, "=", status.value)

# -----------------------------------------
# 9. String Values
# -----------------------------------------
class Department(Enum):
    CSE = "Computer Science"
    ECE = "Electronics"
    ME = "Mechanical"
print("\nDepartment:", Department.CSE)
print("Name:", Department.CSE.name)
print("Value:", Department.CSE.value)

# -----------------------------------------
# 10. IntEnum
# -----------------------------------------
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
priority = Priority.HIGH
print("\nPriority:", priority)
print("Value:", priority.value)
print(
    "Priority.HIGH == 3:",
    Priority.HIGH == 3
)

# -----------------------------------------
# 11. Normal Enum vs Integer
# -----------------------------------------
print(
    "\nStatus.APPROVED == 2:",
    Status.APPROVED == 2
)
print(
    "Priority.HIGH == 3:",
    Priority.HIGH == 3
)

# -----------------------------------------
# 12. StrEnum
# Python 3.11+
# -----------------------------------------
class Role(StrEnum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"
role = Role.STUDENT
print("\nRole:", role)
print("Role Name:", role.name)
print("Role Value:", role.value)
print(
    "Role.STUDENT == 'student':",
    Role.STUDENT == "student"
)

# -----------------------------------------
# 13. @unique
# -----------------------------------------
@unique
class PaymentStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3
print("\nPayment Status:")
for status in PaymentStatus:
    print(status.name, "=", status.value)

# -----------------------------------------
# 14. Enum with Function
# -----------------------------------------
def show_status(status: Status) -> None:
    if status == Status.PENDING:
        print("Waiting for approval.")
    elif status == Status.APPROVED:
        print("Application approved.")
    elif status == Status.REJECTED:
        print("Application rejected.")
print("\nStatus Function:")
show_status(Status.APPROVED)

# -----------------------------------------
# 15. Enum in a Class
# -----------------------------------------
class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
class Order:
    def __init__(
        self,
        order_id: int,
        status: OrderStatus
    ) -> None:
        self.order_id = order_id
        self.status = status
    def display(self) -> None:
        print("Order ID:", self.order_id)
        print("Status:", self.status.name)
order = Order(
    101,
    OrderStatus.SHIPPED
)
print("\nOrder:")
order.display()

# -----------------------------------------
# Summary
# -----------------------------------------

print("\n" + "=" * 30)
print("  ENUM MODULE EXAMPLES")
print("=" * 30)
print("""
✓ Enum
✓ name
✓ value
✓ Access by Name
✓ Access by Value
✓ Iteration
✓ Comparison
✓ auto()
✓ String Values
✓ IntEnum
✓ StrEnum
✓ unique()
✓ Enum with Functions
✓ Enum with Classes
""")