# enum Module

The `enum` module is a built-in Python library used to create a collection of **named constant values**.
Enums make code easier to read, safer, and more organized when a variable should have one value from a fixed set of options.

---

# Why Use enum?

Without `Enum`:
```python
PENDING = 1
APPROVED = 2
REJECTED = 3
status = APPROVED
```
The values `1`, `2`, and `3` do not clearly describe what they represent.

Using `Enum`:
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```

Now:
```python
status = Status.APPROVED
```
is much easier to understand.

---

# Importing the Module

```python
from enum import Enum
```
For additional features:

```python
from enum import Enum, IntEnum, StrEnum, auto, unique
```

> `StrEnum` is available in Python 3.11 and later.

---

# Features Covered

| Feature | Purpose |
|---|---|
| `Enum` | Create an enumeration |
| `.name` | Get member name |
| `.value` | Get member value |
| `auto()` | Automatically assign values |
| `IntEnum` | Integer-based enum |
| `StrEnum` | String-based enum |
| `@unique` | Prevent duplicate values |
| Iteration | Loop through enum members |
| Comparison | Compare enum members |

---

# Creating an Enum

```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```

Here:
```text
Status
│
├── PENDING  → 1
├── APPROVED → 2
└── REJECTED → 3
```
Each item is called an **enum member**.

---

# Accessing Enum Members

Use:

```python
Status.PENDING
```

Example:

```python
print(Status.PENDING)
```

Output:

```text
Status.PENDING
```

---

# name

The `.name` attribute returns the name of an enum member.

```python
print(Status.PENDING.name)
```

Output:

```text
PENDING
```

Remember:

```text
Status.PENDING.name
       ↓
    "PENDING"
```

---

# value

The `.value` attribute returns the value stored in an enum member.

```python
print(Status.PENDING.value)
```

Output:

```text
1
```

Remember:

```text
Status.PENDING.value
       ↓
       1
```

---

# name vs value

For:

```python
class Status(Enum):
    PENDING = 1
```

We have:

```text
Status.PENDING
      │
      ├── .name  → "PENDING"
      │
      └── .value → 1
```

---

# Accessing Member by Name

You can access an enum member using its name:

```python
status = Status["APPROVED"]
print(status)
```
Output:
```text
Status.APPROVED
```
---

# Accessing Member by Value

You can also find a member using its value:
```python
status = Status(2)
print(status)
```
Output:
```text
Status.APPROVED
```
---

# Iterating Through an Enum

Enums can be used in loops.
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

We can display names and values:
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

# Comparing Enum Members
Enum members can be compared using `==`.
```python
status = Status.APPROVED
if status == Status.APPROVED:
    print("Application approved")
```

Output:
```text
Application approved
```
This is clearer than:
```python
if status == 2:
```
because `Status.APPROVED` explains what the value represents.

---

# auto()

`auto()` automatically generates values for enum members.

```python
from enum import Enum, auto
class Status(Enum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()
```
Now we don't need to manually write:
```python
PENDING = 1
APPROVED = 2
REJECTED = 3
```

Example:
```python
print(Status.PENDING.value)
print(Status.APPROVED.value)
print(Status.REJECTED.value)
```
For a normal `Enum`, these commonly produce:
```text
1
2
3
```

---

# Why Use auto()?

Sometimes the actual values do not matter.
We only care about:
```text
PENDING
APPROVED
REJECTED
```

So instead of manually assigning numbers, we can use:
```python
auto()
```

Memory Tip:
```text
auto()
↓
Generate value automatically
```

---

# String Values

Enums can also store strings.
```python
class Department(Enum):
    CSE = "Computer Science"
    ECE = "Electronics"
    ME = "Mechanical"
```

Access:
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

# IntEnum

`IntEnum` creates enum members that also behave like integers.
```python
from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
```

Example:
```python
print(Priority.HIGH)
print(Priority.HIGH == 3)
```

Output:
```text
3
True
```
A normal `Enum` does not behave this way:

```python
Status.APPROVED == 2
```

is:
```text
False
```

---

# Enum vs IntEnum

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

But:

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

Use `IntEnum` when compatibility with integers is actually needed.

---

# StrEnum

`StrEnum` creates enum members that also behave like strings.

```python
from enum import StrEnum
class Role(StrEnum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"
```

Example:
```python
role = Role.STUDENT
print(role)
```

Output:
```text
student
```

Comparison:
```python
print(Role.STUDENT == "student")
```

Output:
```text
True
```
`StrEnum` is available in Python 3.11+.

---

# unique()

`@unique` ensures that enum members do not have duplicate values.

```python
from enum import Enum, unique
@unique
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```
This is valid because every value is different.

But:
```python
@unique
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 2
```
causes an error because:
```text
APPROVED → 2
REJECTED → 2
```
have the same value.

---

# Duplicate Values Without unique()
Normal enums can have duplicate values.

```python
class Status(Enum):
    PENDING = 1
    WAITING = 1
```
Here, `WAITING` becomes an **alias** of `PENDING`.

Using:
```python
@unique
```
prevents this.

---

# Enums with Functions

Enums can be used as function parameters.
```python
def show_status(status: Status) -> None:
    if status == Status.PENDING:
        print("Waiting for approval")
    elif status == Status.APPROVED:
        print("Approved")
    elif status == Status.REJECTED:
        print("Rejected")
```

Call:
```python
show_status(Status.APPROVED)
```

Output:
```text
Approved
```

---

# Real-World Example

Suppose an order can have these statuses:
```text
PENDING
PROCESSING
SHIPPED
DELIVERED
CANCELLED
```

Instead of repeatedly using strings:
```python
status = "shipped"
```

we can create:
```python
class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()
```

Then:
```python
status = OrderStatus.SHIPPED
```
This makes the allowed states clear and reduces accidental string mistakes.

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
| Separate variables | Grouped together |
| Less structured | Organized |
| Easy to mix unrelated values | Members belong to an enum type |
| Limited built-in functionality | `.name`, `.value`, iteration, etc. |
| Harder to represent fixed states | Designed for fixed sets of values |

---

# When to Use Enum

Enums are useful when a value should come from a fixed set of options.
Examples:

### User Roles

```text
ADMIN
TEACHER
STUDENT
```

### Order Status

```text
PENDING
SHIPPED
DELIVERED
```

### Priority

```text
LOW
MEDIUM
HIGH
```

### Directions

```text
NORTH
SOUTH
EAST
WEST
```

### Payment Status

```text
PENDING
SUCCESS
FAILED
```

---

# Advantages

- Makes code more readable
- Groups related constants
- Reduces magic numbers and strings
- Provides meaningful names
- Supports iteration
- Supports comparisons
- Makes fixed states easier to manage
- Reduces accidental invalid values

---

# Prerequisites

Before learning this module, you should know:
- Classes
- Objects
- Variables
- Constants
- Loops
- Conditions
- Functions
- Type hints

---

# Mini Project

## Task Status Manager

We'll create task states:

```python
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELLED = auto()
```

Then create tasks such as:
```text
Task   : Complete Python Handbook
Status : IN_PROGRESS
```

The project will demonstrate:
- `Enum`
- `auto()`
- `.name`
- `.value`
- Comparisons
- Iteration
- Functions with enum values

---

# Learning Outcomes

After completing this module, you'll be able to:
- Create enums using `Enum`.
- Access enum members.
- Understand `.name` and `.value`.
- Iterate through enum members.
- Compare enum members.
- Generate values with `auto()`.
- Use `IntEnum`.
- Use `StrEnum`.
- Prevent duplicate values using `@unique`.
- Use enums to represent fixed application states.

---

# Best Practices

- Use meaningful member names.
- Use enums when values come from a fixed set.
- Use `auto()` when actual numeric values do not matter.
- Prefer normal `Enum` unless integer or string compatibility is required.
- Use `@unique` when duplicate values should not be allowed.
- Compare enum members directly instead of comparing magic values.

Prefer:

```python
if status == Status.APPROVED:
```

instead of:

```python
if status.value == 2:
```

---

# Common Mistakes

## Comparing Enum Directly with Its Value

```python
class Status(Enum):
    APPROVED = 2
```

This:

```python
Status.APPROVED == 2
```

returns:

```text
False
```

Use:

```python
Status.APPROVED.value == 2
```

or preferably:

```python
status == Status.APPROVED
```

---

## Confusing name and value

```python
Status.APPROVED.name
```

returns:

```text
APPROVED
```

While:

```python
Status.APPROVED.value
```

returns:

```text
2
```

---

## Using Strings Everywhere

Avoid repeatedly writing:

```python
status = "approved"
```

when the possible statuses are fixed.

Prefer:

```python
status = Status.APPROVED
```

---

# Memory Trick

```text
Enum
↓
Named Constants

Status.PENDING
↓
Enum Member

.name
↓
Member Name

.value
↓
Member Value

auto()
↓
Automatic Value

IntEnum
↓
Integer Enum

StrEnum
↓
String Enum

@unique
↓
No Duplicate Values
```

---

# Quick Revision

| Need | Use |
|---|---|
| Create enum | `Enum` |
| Access member | `Status.PENDING` |
| Get name | `.name` |
| Get value | `.value` |
| Generate value | `auto()` |
| Integer-compatible enum | `IntEnum` |
| String-compatible enum | `StrEnum` |
| Prevent duplicate values | `@unique` |
| Loop through members | `for item in Status` |
| Compare members | `status == Status.PENDING` |

---