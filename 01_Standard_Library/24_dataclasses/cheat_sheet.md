# dataclasses Module Cheat Sheet

## Import

```python
from dataclasses import dataclass, field, asdict, astuple, replace
```
The `dataclasses` module is used to create classes that mainly store data with less repetitive code.

---
# 1. @dataclass

**Purpose:** Automatically generates common methods like `__init__()`, `__repr__()`, and `__eq__()`.

```python
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
```

Create an object:
```python
student = Student("Akhil", 19)
```

Output:
```text
Student(name='Akhil', age=19)
```
---

# 2. Fields

Variables defined inside a dataclass are called fields.

```python
@dataclass
class Student:
    name: str
    age: int
    department: str
```

Here:
```text
name       → field
age        → field
department → field
```

---
# 3. Default Values
Fields can have default values.

```python
@dataclass
class Student:
    name: str
    department: str = "CSE"
```

Now:
```python
student = Student("Akhil")
```

uses:
```text
department = CSE
```
Required fields should normally come before fields with default values.

---

# 4. field()

**Purpose:** Provides additional control over a dataclass field.

```python
from dataclasses import field
@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)
```
`field()` is commonly used with `default_factory`.

---

# 5. default_factory

**Purpose:** Creates a new mutable default value for every object.

```python
@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)
```

Now:
```python
student1 = Student("Akhil")
student2 = Student("Rahul")
```
each gets a separate empty list.

```text
student1.marks → []
student2.marks → []
```
Memory Tip:
```text
default_factory=list
↓
New list for every object
```

---

# 6. __post_init__()

**Purpose:** Runs automatically after the generated `__init__()` finishes.
```python
@dataclass
class Student:
    name: str
    age: int
    def __post_init__(self) -> None:
        if self.age <= 0:
            raise ValueError(
                "Age must be greater than 0"
            )
```
Useful for:
- Validation
- Calculations
- Additional initialization

---

# 7. Methods Inside Dataclasses
Dataclasses can contain normal methods.
```python
@dataclass
class Rectangle:
    length: float
    width: float
    def area(self) -> float:
        return self.length * self.width
```

Use:
```python
rectangle = Rectangle(10, 5)
print(rectangle.area())
```
Output:
```text
50
```
---

# 8. asdict()

**Purpose:** Converts a dataclass object into a dictionary.

```python
student = Student("Akhil", 19)
data = asdict(student)
```
Result:
```python
{
    "name": "Akhil",
    "age": 19
}
```
Memory Tip:
```text
asdict()
↓
Object → Dictionary
```
---
# 9. astuple()

**Purpose:** Converts a dataclass object into a tuple.
```python
data = astuple(student)
```
Result:
```python
("Akhil", 19)
```

Memory Tip:
```text
astuple()
↓
Object → Tuple
```
---

# 10. replace()

**Purpose:** Creates a new object with selected field values changed.
```python
student1 = Student(
    "Akhil",
    19
)
student2 = replace(
    student1,
    age=20
)
```
Result:
```text
student1 → Student(name='Akhil', age=19)
student2 → Student(name='Akhil', age=20)
```
The original object remains unchanged.

---

# 11. frozen=True
**Purpose:** Prevents normal reassignment of fields after object creation.

```python
@dataclass(frozen=True)
class Account:
    account_id: int
    username: str
```

Create:
```python
account = Account(
    101,
    "akhil"
)
```

This is not allowed:
```python
account.username = "rahul"
```

It raises:
```text
FrozenInstanceError
```

Memory Tip:
```text
frozen=True
↓
Freeze field assignments
```
---

# 12. order=True

**Purpose:** Enables ordering comparisons between dataclass objects.
```python
@dataclass(order=True)
class Score:
    marks: int
    name: str
```
Example:
```python
score1 = Score(80, "Akhil")
score2 = Score(90, "Rahul")
print(score1 < score2)
```
Output:

```text
True
```
Fields are compared in the order they are defined.
Here, `marks` is compared first.

---

# Automatically Generated Methods

By default, `@dataclass` commonly generates:
```text
__init__()
__repr__()
__eq__()
```
Example:
```python
@dataclass
class Student:
    name: str
    age: int
```
You don't need to manually write:
```python
def __init__(...):
    ...
```
for normal field initialization.
---

# Automatic Equality

```python
student1 = Student("Akhil", 19)
student2 = Student("Akhil", 19)
print(student1 == student2)
```
Output:
```text
True
```
Dataclasses compare their field values.

---

# Default Field Order
Correct:
```python
@dataclass
class Student:
    name: str
    age: int = 18
```

Incorrect:
```python
@dataclass
class Student:
    age: int = 18
    name: str
```
Required fields should come before default fields.

---

# Mutable Defaults

Avoid:
```python
@dataclass
class Student:
    marks: list[int] = []
```

Use:
```python
@dataclass
class Student:
    marks: list[int] = field(
        default_factory=list
    )
```
Why?
Because each object should receive its own list.

---

# Dataclass vs Normal Class

| Normal Class | Dataclass |
|---|---|
| Usually write `__init__()` | Generated automatically |
| Often write `__repr__()` | Generated automatically |
| Often write `__eq__()` | Generated automatically |
| More boilerplate | Less boilerplate |
| General-purpose classes | Great for data-oriented classes |

---

# Complete Example

```python
from dataclasses import dataclass, field, asdict
@dataclass
class Student:
    roll_no: int
    name: str
    department: str = "CSE"
    marks: list[int] = field(
        default_factory=list
    )
    def __post_init__(self) -> None:
        if self.roll_no <= 0:
            raise ValueError(
                "Invalid roll number"
            )
    def average(self) -> float:
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

student = Student(
    101,
    "Akhil",
    marks=[85, 90, 80]
)
print(student)
print(student.average())
print(asdict(student))
```
---
# How Dataclass Works

```text
@dataclass
    ↓
Class fields
    ↓
Automatic __init__()
    ↓
Create Object
    ↓
__post_init__()
    ↓
Object Ready
```
Example:
```python
student = Student(
    101,
    "Akhil"
)
```
Python handles the basic initialization automatically.
---

# Best Practices
- Use dataclasses for data-oriented classes.
- Add type hints to fields.
- Put required fields before default fields.
- Use `default_factory` for mutable defaults.
- Use `__post_init__()` for simple validation.
- Use `asdict()` when dictionary conversion is needed.
- Use `frozen=True` when fields should not be reassigned.
- Keep dataclasses simple and readable.

---
# Common Mistakes

❌ Forgetting the decorator:
```python
class Student:
    name: str
    age: int
```

Use:
```python
@dataclass
class Student:
    name: str
    age: int
```

---

❌ Using a mutable default directly:
```python
marks: list[int] = []
```

Use:
```python
marks: list[int] = field(
    default_factory=list
)
```
---

❌ Putting a required field after a default field:

```python
@dataclass
class Student:
    department: str = "CSE"
    name: str
```

Correct:
```python
@dataclass
class Student:
    name: str
    department: str = "CSE"
```

---

❌ Assuming type hints validate values:
```python
@dataclass
class Student:
    age: int
```

This does not automatically check whether the provided value is really an integer.
Use validation when needed.

---

# Memory Trick

```text
@dataclass
↓
Create Data Class

field()
↓
Customize Field

default_factory
↓
New Mutable Value

__post_init__()
↓
After Initialization

asdict()
↓
Object → Dictionary

astuple()
↓
Object → Tuple

replace()
↓
Modified Copy

frozen=True
↓
Prevent Reassignment

order=True
↓
Enable Ordering
```

---

# Quick Revision

| Need | Use |
|---|---|
| Create dataclass | `@dataclass` |
| Define field | `name: str` |
| Default value | `age: int = 18` |
| Customize field | `field()` |
| New list per object | `default_factory=list` |
| Validation after initialization | `__post_init__()` |
| Convert to dictionary | `asdict()` |
| Convert to tuple | `astuple()` |
| Create modified copy | `replace()` |
| Prevent field reassignment | `frozen=True` |
| Enable comparisons | `order=True` |

---

# Interview Tip

**Why use `default_factory=list` instead of `marks: list[int] = []`?**

`default_factory=list` creates a new list for every dataclass object.
```python
marks: list[int] = field(
    default_factory=list
)
```
This prevents different objects from unintentionally sharing the same mutable list.