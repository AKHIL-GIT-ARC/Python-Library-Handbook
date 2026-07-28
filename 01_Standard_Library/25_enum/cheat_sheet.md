# enum Module Cheat Sheet

## Import

```python
from enum import Enum, IntEnum, StrEnum, auto, unique
```
The `enum` module is used to create **named constants** that belong to a fixed group.

---

# 1. Enum

**Purpose:** Creates a group of related named constants.

```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```

Access a member:
```python
Status.APPROVED
```

Result:
```text
Status.APPROVED
```

Memory Tip:
```text
Enum
↓
Group of Named Constants
```

---

# 2. Enum Member

Each value inside an enum is called an **enum member**.

```python
class Status(Enum):
    PENDING = 1
    APPROVED = 2
```

Here:
```text
Status.PENDING  → Enum Member
Status.APPROVED → Enum Member
```

---

# 3. .name

**Purpose:** Returns the name of an enum member.

```python
print(Status.APPROVED.name)
```

Output:
```text
APPROVED
```

Memory Tip:
```text
.name
↓
Member Name
```

---

# 4. .value

**Purpose:** Returns the value stored in an enum member.

```python
print(Status.APPROVED.value)
```

Output:
```text
2
```

Memory Tip:
```text
.value
↓
Member Value
```
---

# 5. name vs value

For:
```python
class Status(Enum):
    APPROVED = 2
```
We have:
```text
Status.APPROVED
      │
      ├── .name  → "APPROVED"
      └── .value → 2
```
---

# 6. Access by Name

Use square brackets to find a member using its name.
```python
status = Status["APPROVED"]
print(status)
```

Output:
```text
Status.APPROVED
```

Remember:
```text
Status["APPROVED"]
↓
Search by Name
```

---

# 7. Access by Value

Call the enum class with a value:
```python
status = Status(2)
print(status)
```

Output:
```text
Status.APPROVED
```

Remember:
```text
Status(2)
↓
Search by Value
```
---

# 8. Iteration

Enums can be looped through.
```python
for status in Status:
    print(status)
```

Output:
```text
Status.PENDING
Status.APPROVED
Status.REJECTED
```
To display names and values:
```python
for status in Status:
    print(status.name, status.value)
```

Output:
```text
PENDING 1
APPROVED 2
REJECTED 3
```
---

# 9. Comparison

Compare enum members directly.

```python
status = Status.APPROVED
if status == Status.APPROVED:
    print("Approved")
```

Prefer:
```python
status == Status.APPROVED
```

Instead of:
```python
status.value == 2
```
The enum comparison is clearer and does not depend on the underlying value.

---

# 10. auto()

**Purpose:** Automatically generates values for enum members.

```python
from enum import Enum, auto
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
```
Typically:
```text
PENDING     → 1
IN_PROGRESS → 2
COMPLETED   → 3
```
Use `auto()` when the actual values are not important.
Memory Tip:
```text
auto()
↓
Automatic Value
```
---
# 11. String Values

Enum values can also be strings.
```python
class Department(Enum):
    CSE = "Computer Science"
    ECE = "Electronics"
    ME = "Mechanical"
```

Example:
```python
print(Department.CSE.name)
print(Department.CSE.value)
```
Output:
```text
CSE
Computer Science
```
---

# 12. IntEnum

**Purpose:** Creates enum members that are also compatible with integers.

```python
from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
```
Example:
```python
print(Priority.HIGH == 3)
```

Output:
```text
True
```

With normal `Enum`:
```python
Status.APPROVED == 2
```

Output:
```text
False
```

Memory Tip:
```text
IntEnum
↓
Enum + Integer Behavior
```
---

# 13. StrEnum

**Purpose:** Creates enum members that are also compatible with strings.

```python
from enum import StrEnum
class Role(StrEnum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"
```
Example:
```python
print(Role.STUDENT == "student")
```

Output:
```text
True
```

Memory Tip:
```text
StrEnum
↓
Enum + String Behavior
```
`StrEnum` is available in Python 3.11+.

---

# 14. @unique

**Purpose:** Ensures enum values are unique.
```python
from enum import Enum, unique
@unique
class PaymentStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3
```
This is valid because every member has a different value.
This is invalid:

```python
@unique
class PaymentStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 2
```
because:
```text
SUCCESS → 2
FAILED  → 2
```
have duplicate values.

Memory Tip:
```text
@unique
↓
No Duplicate Values
```
---

# 15. Duplicate Values and Aliases

Without `@unique`, duplicate values are allowed.

```python
class Status(Enum):
    PENDING = 1
    WAITING = 1
```
`WAITING` becomes an alias of `PENDING`.

```python
print(Status.WAITING is Status.PENDING)
```

Output:
```text
True
```
Use `@unique` when aliases should not be allowed.

---

# 16. Enum with Functions

Enums can be passed to functions.

```python
def show_status(status: Status) -> None:
    if status == Status.PENDING:
        print("Pending")
    elif status == Status.APPROVED:
        print("Approved")
    elif status == Status.REJECTED:
        print("Rejected")
```

Call:
```python
show_status(Status.APPROVED)
```

---

# 17. Enum with Classes

Enums are useful for representing object states.

```python
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
```

Use inside a class:
```python
class Task:
    def __init__(
        self,
        title: str,
        status: TaskStatus = TaskStatus.PENDING
    ) -> None:
        self.title = title
        self.status = status
```
Create:
```python
task = Task(
    "Complete Python Handbook"
)
```
The default status is:
```text
PENDING
```
---

# Enum vs Regular Constants

Regular constants:
```python
PENDING = 1
APPROVED = 2
REJECTED = 3
```

Enum:
```python
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```
| Regular Constants | Enum |
|---|---|
| Separate values | Grouped values |
| Less structured | Organized |
| Easy to mix values | Members belong to enum |
| No `.name` | Supports `.name` |
| No built-in iteration group | Enum is iterable |

---

# Enum vs IntEnum

## Enum

```python
class Status(Enum):
    APPROVED = 2
```

```python
Status.APPROVED == 2
```

Result:
```text
False
```

## IntEnum

```python
class Priority(IntEnum):
    HIGH = 3
```

```python
Priority.HIGH == 3
```

Result:
```text
True
```

Remember:
```text
Enum
↓
Separate Enum Type

IntEnum
↓
Enum + Integer Compatibility
```

---

# Enum vs StrEnum

Normal string-valued enum:
```python
class Role(Enum):
    STUDENT = "student"
```
```python
Role.STUDENT == "student"
```
Result:
```text
False
```
Using `StrEnum`:
```python
class Role(StrEnum):
    STUDENT = "student"
```
```python
Role.STUDENT == "student"
```

Result:
```text
True
```

---

# When to Use Enu
Use enums when a value should come from a fixed set of options.
Examples:
```text
Task Status
├── PENDING
├── IN_PROGRESS
├── COMPLETED
└── CANCELLED
```
```text
Priority
├── LOW
├── MEDIUM
└── HIGH
```
```text
User Role
├── ADMIN
├── TEACHER
└── STUDENT
```
```text
Order Status
├── PENDING
├── PROCESSING
├── SHIPPED
└── DELIVERED
```
---

# Best Practices

- Use enums for fixed sets of related values.
- Give members clear and meaningful names.
- Use `auto()` when underlying values do not matter.
- Compare enum members directly.
- Use `IntEnum` only when integer compatibility is needed.
- Use `StrEnum` only when string compatibility is useful.
- Use `@unique` when duplicate values should not be allowed.
- Avoid unnecessary magic numbers and repeated status strings.

---

# Common Mistakes

## Comparing Enum with Raw Value

Wrong:

```python
status = Status.APPROVED
if status == 2:
    print("Approved")
```

For a normal `Enum`, this comparison is false.

Prefer:

```python
if status == Status.APPROVED:
    print("Approved")
```

---

## Confusing .name and .value

```python
Status.APPROVED.name
```

returns:
```text
APPROVED
```

But:
```python
Status.APPROVED.value
```

returns:
```text
2
```

Remember:
```text
.name  → Name
.value → Value
```

---

## Using Strings for Fixed States

Avoid:
```python
status = "completed"
```

when the available statuses are fixed.

Prefer:
```python
status = TaskStatus.COMPLETED
```

This avoids inconsistent values such as:

```text
"completed"
"complete"
"done"
"COMPLETED"
```

---

## Using IntEnum Without Needing Integer Behavior
Don't use `IntEnum` just because the enum values happen to be integers.

Prefer:
```python
class Status(Enum):
```

unless you specifically need behavior such as:
```python
Priority.HIGH == 3
```

---

# Complete Example

```python
from enum import Enum, auto
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
status = TaskStatus.IN_PROGRESS
print(status)
print(status.name)
print(status.value)
if status == TaskStatus.IN_PROGRESS:
    print("Task is currently in progress.")
for item in TaskStatus:
    print(item.name, item.value)
```

Possible output:
```text
TaskStatus.IN_PROGRESS
IN_PROGRESS
2
Task is currently in progress.
PENDING 1
IN_PROGRESS 2
COMPLETED 3
```

---

# Memory Trick

```text
Enum
↓
Named Constants

Status.APPROVED
↓
Enum Member

.name
↓
Member Name

.value
↓
Member Value

Status["APPROVED"]
↓
Find by Name

Status(2)
↓
Find by Value

auto()
↓
Automatic Value

IntEnum
↓
Integer-Compatible Enum

StrEnum
↓
String-Compatible Enum

@unique
↓
No Duplicate Values
```

---

# Quick Revision

| Need | Use |
|---|---|
| Create enum | `Enum` |
| Access member | `Status.APPROVED` |
| Get member name | `.name` |
| Get member value | `.value` |
| Find by name | `Status["APPROVED"]` |
| Find by value | `Status(2)` |
| Automatic values | `auto()` |
| Integer compatibility | `IntEnum` |
| String compatibility | `StrEnum` |
| Prevent duplicate values | `@unique` |
| Iterate | `for item in Status` |
| Compare | `status == Status.APPROVED` |

---

# Interview Tip

**Question:** What is the main advantage of using `Enum` instead of normal constants?

**Answer:**

`Enum` groups related constants into a single type and gives each value a meaningful name.
Instead of:
```python
status = 2
```

we can write:
```python
status = Status.APPROVED
```
This makes the code clearer, more organized, and easier to maintain.