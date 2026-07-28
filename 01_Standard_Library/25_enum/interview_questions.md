# enum Module Interview Questions

## Beginner Level

### 1. What is `Enum` in Python?
**Answer:**
`Enum` is used to create a group of related **named constants**.
```python
from enum import Enum
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```
Instead of using unclear values like:

```python
status = 2
```

we can use:
```python
status = Status.APPROVED
```

---

### 2. What is an enum member?

**Answer:**

Each named value inside an enum is called an **enum member**.
```python
class Status(Enum):
    PENDING = 1
    APPROVED = 2
```

Here:
```text
Status.PENDING  → Enum member
Status.APPROVED → Enum member
```
---

### 3. How do you access an enum member?

**Answer:**
Use the enum class followed by the member name.

```python
Status.APPROVED
```
Example:
```python
print(Status.APPROVED)
```
Output:
```text
Status.APPROVED
```

---

### 4. What does `.name` return?

**Answer:**
`.name` returns the name of the enum member.
```python
print(Status.APPROVED.name)
```

Output:
```text
APPROVED
```

---

### 5. What does `.value` return?

**Answer:**

`.value` returns the value associated with the enum member.

```python
print(Status.APPROVED.value)
```

Output:
```text
2
```

Remember:
```text
Status.APPROVED
      │
      ├── .name  → "APPROVED"
      └── .value → 2
```
---

## Intermediate Level

### 6. How do you access an enum member by name?

**Answer:**

Use square brackets:
```python
status = Status["APPROVED"]
```

Result:
```text
Status.APPROVED
```

---

### 7. How do you access an enum member by value?

**Answer:**

Call the enum class with the value:

```python
status = Status(2)
```

Result:
```text
Status.APPROVED
```

Remember:
```text
Status["APPROVED"] → Find by name
Status(2)          → Find by value
```

---

### 8. How do you iterate through an enum?

**Answer:**

Use a `for` loop.
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

### 9. How do you compare enum members?

**Answer:**
Compare the members directly.

```python
status = Status.APPROVED
if status == Status.APPROVED:
    print("Approved")
```

Prefer:
```python
status == Status.APPROVED
```

instead of comparing the underlying value:

```python
status.value == 2
```

---

### 10. What is `auto()`?

**Answer:**

`auto()` automatically generates values for enum members.

```python
from enum import Enum, auto
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
```

For a normal `Enum`, these values commonly become:

```text
PENDING     → 1
IN_PROGRESS → 2
COMPLETED   → 3
```

Use `auto()` when the actual values are not important.

---

## Advanced Level

### 11. What is `IntEnum`?

**Answer:**

`IntEnum` creates enum members that are also compatible with integers.

```python
from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
```

Now:
```python
Priority.HIGH == 3
```

returns:
```text
True
```

---

### 12. What is the difference between `Enum` and `IntEnum`?

**Answer:**

A normal `Enum` member does not compare equal to its raw integer value.

```python
Status.APPROVED == 2
```

Result:

```text
False
```
An `IntEnum` member is integer-compatible:

```python
Priority.HIGH == 3
```

Result:
```text
True
```
Use `IntEnum` when integer compatibility is specifically required.

---

### 13. What is `StrEnum`?

**Answer:**

`StrEnum` creates enum members that are also compatible with strings.

```python
from enum import StrEnum
class Role(StrEnum):
    STUDENT = "student"
    TEACHER = "teacher"
    ADMIN = "admin"
```

Now:
```python
Role.STUDENT == "student"
```

returns:
```text
True
```
`StrEnum` is available in Python 3.11+.
---

### 14. What does `@unique` do?

**Answer:**

`@unique` ensures that every enum member has a unique value.

```python
from enum import Enum, unique
@unique
class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
```
Duplicate values cause an error.

---

### 15. Can enum members have duplicate values?

**Answer:**

Yes, normal enums can contain duplicate values.

```python
class Status(Enum):
    PENDING = 1
    WAITING = 1
```

In this case, `WAITING` becomes an alias of `PENDING`.

```python
Status.WAITING is Status.PENDING
```

returns:

```text
True
```

Use `@unique` if aliases should not be allowed.

---

## Scenario-Based Questions

### 16. You have task states `PENDING`, `IN_PROGRESS`, and `COMPLETED`. How would you represent them?

**Answer:**

```python
from enum import Enum, auto
class TaskStatus(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
```

---

### 17. The actual numeric values don't matter. What should you use?

**Answer:**

Use:
```python
auto()
```

Example:
```python
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
```

---

### 18. You need enum members to work like integers. What should you use?

**Answer:**

Use:
```python
IntEnum
```

Example:
```python
class Priority(IntEnum):
    LOW = 1
    HIGH = 2
```

---

### 19. You need enum members to work like strings. What should you use?

**Answer:**

Use `StrEnum` in Python 3.11+.

```python
class Role(StrEnum):
    ADMIN = "admin"
    STUDENT = "student"
```

---

### 20. You want to prevent duplicate enum values. What should you use?

**Answer:**

Use:
```python
@unique
```

Example:
```python
@unique
class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
```

---

## Coding Questions

### 21. Create an enum for traffic lights.

**Answer:**

```python
from enum import Enum, auto
class TrafficLight(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
```

---

### 22. Print the name and value of an enum member.

**Answer:**

```python
status = Status.APPROVED
print(status.name)
print(status.value)
```

Output:
```text
APPROVED
2
```

---

### 23. Loop through all enum members.

**Answer:**

```python
for status in Status:
    print(status.name, status.value)
```

---

### 24. Create a function that accepts a Status enum.

**Answer:**

```python
def check_status(status: Status) -> None:
    if status == Status.APPROVED:
        print("Approved")
    elif status == Status.PENDING:
        print("Pending")
    elif status == Status.REJECTED:
        print("Rejected")
```

Call:
```python
check_status(Status.APPROVED)
```

---

### 25. Create an enum using string values.

**Answer:**
```python
class Department(Enum):
    CSE = "Computer Science"
    ECE = "Electronics"
    ME = "Mechanical"
```
---

### 26. Create an enum with automatic values.

**Answer:**
```python
class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
```

---

## Enum vs IntEnum

| Feature | `Enum` | `IntEnum` |
|---|---|---|
| Named constants | Yes | Yes |
| Can store integers | Yes | Yes |
| Integer compatible | No | Yes |
| `Member == int` | `False` | Can be `True` |
| Preferred default | Yes | Only when int behavior is needed |

---

## Enum vs StrEnum

| Feature | `Enum` | `StrEnum` |
|---|---|---|
| Named constants | Yes | Yes |
| Can store strings | Yes | Yes |
| String compatible | No | Yes |
| `Member == str` | `False` | Can be `True` |
| Python 3.11+ required | No | Yes |

---

## Frequently Used Features

| Feature | Purpose |
|---|---|
| `Enum` | Create named constants |
| `.name` | Get member name |
| `.value` | Get member value |
| `auto()` | Generate values automatically |
| `IntEnum` | Integer-compatible enum |
| `StrEnum` | String-compatible enum |
| `@unique` | Prevent duplicate values |
| `Status["NAME"]` | Find member by name |
| `Status(value)` | Find member by value |

---

## Best Practices

- Use enums when values come from a fixed set.
- Give members meaningful names.
- Use `auto()` when the underlying values do not matter.
- Compare enum members directly.
- Prefer `Enum` unless integer or string compatibility is required.
- Use `@unique` when duplicate values should not be allowed.
- Avoid magic numbers and repeated status strings.

---

## Common Mistakes

### Comparing a Normal Enum to Its Raw Value

Wrong:

```python
status = Status.APPROVED
if status == 2:
    print("Approved")
```

Correct:
```python
if status == Status.APPROVED:
    print("Approved")
```

---

### Confusing `.name` and `.value`

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

### Using Strings Instead of Enums

Avoid:

```python
status = "completed"
```

when the possible values are fixed.

Prefer:
```python
status = TaskStatus.COMPLETED
```

---

## Memory Trick

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
Automatic Values

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

## Quick Revision

| Need | Use |
|---|---|
| Create enum | `Enum` |
| Access member | `Status.APPROVED` |
| Get name | `.name` |
| Get value | `.value` |
| Find by name | `Status["APPROVED"]` |
| Find by value | `Status(2)` |
| Generate values | `auto()` |
| Integer-compatible enum | `IntEnum` |
| String-compatible enum | `StrEnum` |
| Prevent duplicates | `@unique` |
| Loop through enum | `for item in Status` |
| Compare members | `status == Status.APPROVED` |

---

## Interview Tip

**Question:** Why would you use an enum instead of strings or integers?

**Answer:**

Enums group related values under a meaningful type and make the allowed states clear.
Instead of:
```python
status = 2
```

or:

```python
status = "approved"
```

we can write:
```python
status = Status.APPROVED
```
This improves readability, organization, and maintainability while reducing mistakes caused by inconsistent magic values.