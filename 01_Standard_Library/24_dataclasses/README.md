# dataclasses Module

The `dataclasses` module is a built-in Python library used to create classes that mainly store data with less repetitive code.

Using `@dataclass`, Python can automatically generate common methods such as `__init__()`, `__repr__()`, and `__eq__()`.

---

# Why Use dataclasses?

Without `dataclass`:

```python
class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
```

Using `dataclass`:

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    department: str
```

Both allow:

```python
student = Student("Akhil", 19, "CSE")
```

But `@dataclass` removes the need to manually write common boilerplate code.

---

# Importing the Module

```python
from dataclasses import dataclass
```
For additional features:

```python
from dataclasses import (
    dataclass,
    field,
    asdict,
    astuple,
    replace
)
```
---

# Functions and Features Covered

| Feature | Purpose |
|---|---|
| `@dataclass` | Create a data class |
| Fields | Store object data |
| Default values | Give fields initial values |
| `field()` | Customize a field |
| `default_factory` | Create safe mutable defaults |
| `__post_init__()` | Run code after initialization |
| `asdict()` | Convert object to dictionary |
| `astuple()` | Convert object to tuple |
| `replace()` | Create a modified copy |
| `frozen=True` | Prevent field reassignment |
| `order=True` | Enable ordering comparisons |

---

# Basic Dataclass

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    department: str
```

Create an object:

```python
student = Student("Akhil",19,"CSE")
print(student)
```

Output:

```text
Student(name='Akhil', age=19, department='CSE')
```
Python automatically creates a readable representation of the object.

---

# Fields

The variables defined inside a dataclass are called **fields**.

```python
@dataclass
class Student:
    name: str
    age: int
```

Here:

```text
name → field
age  → field
```

They also use type annotations:
```python
name: str
age: int
```

---

# Automatic __init__()

Normally, we write:

```python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

With:

```python
@dataclass
class Student:
    name: str
    age: int
```

Python automatically creates an appropriate `__init__()`.
So we can directly write:

```python
student = Student("Akhil", 19)
```

---

# Automatic __repr__()
A dataclass automatically creates a useful `__repr__()` method.

```python
print(student)
```

Output:
```text
Student(name='Akhil', age=19)
```
With a normal class, printing an object may otherwise produce something like:
```text
<__main__.Student object at 0x...>
```
unless you define your own representation.

---

# Automatic __eq__()

Dataclasses also generate `__eq__()` by default.

```python
student1 = Student("Akhil", 19)
student2 = Student("Akhil", 19)
print(student1 == student2)
```

Output:
```text
True
```
Their field values are equal, so the objects compare as equal.

---

# Default Values

Fields can have default values.

```python
@dataclass
class Student:
    name: str
    age: int
    department: str = "CSE"
```

Now:
```python
student = Student("Akhil", 19)
```

automatically uses:
```text
department = CSE
```

---

# Important Default Value Rule
Fields without defaults must normally come before fields with defaults.

Correct:
```python
@dataclass
class Student:
    name: str
    age: int
    department: str = "CSE"
```

Incorrect:

```python
@dataclass
class Student:
    department: str = "CSE"
    name: str
```

This causes an error because a required field appears after a default field.

---

# field()

`field()` provides additional control over dataclass fields.

```python
from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    marks: list[int] = field(default_factory=list)
```

Here:

```python
field(default_factory=list)
```
creates a new empty list for each object.

---

# Why Use default_factory?

Avoid:

```python
marks: list[int] = []
```
Mutable defaults such as lists should not be defined this way in a dataclass.

Instead:
```python
marks: list[int] = field(
    default_factory=list
)
```
Now each student gets their own list.

```python
student1 = Student("Akhil")
student2 = Student("Rahul")
```

Their `marks` lists are separate objects.

---

# __post_init__()

`__post_init__()` runs automatically after the generated `__init__()` finishes.

```python
@dataclass
class Student:
    name: str
    age: int
    def __post_init__(self):
        print("Student created:", self.name)
```

Create:
```python
student = Student("Akhil", 19)
```
Output:
```text
Student created: Akhil
```
It is useful for:
- Validation
- Calculations
- Additional initialization

---

# Validation with __post_init__()

```python
@dataclass
class Student:
    name: str
    age: int
    def __post_init__(self):
        if self.age <= 0:
            raise ValueError(
                "Age must be greater than 0"
            )
```
Now invalid data can be rejected when the object is created.

---

# asdict()

`asdict()` converts a dataclass object into a dictionary.

```python
from dataclasses import asdict
student = Student("Akhil", 19)
print(asdict(student))
```
Output:
```python
{
    "name": "Akhil",
    "age": 19
}
```

---

# astuple()

`astuple()` converts a dataclass object into a tuple.

```python
from dataclasses import astuple
print(astuple(student))
```

Output:
```python
("Akhil", 19)
```
---

# replace()

`replace()` creates a new dataclass object with selected field values changed.

```python
from dataclasses import replace
student1 = Student(
    "Akhil",
    19
)
student2 = replace(
    student1,
    age=20
)
```

Now:
```text
student1 → Student(name='Akhil', age=19)
student2 → Student(name='Akhil', age=20)
```

The original object is not modified.

---

# frozen=True

`frozen=True` prevents normal reassignment of fields after the object is created.

```python
@dataclass(frozen=True)
class Student:
    name: str
    roll_no: int
```

Create:

```python
student = Student(
    "Akhil",
    101
)
```
Trying:
```python
student.roll_no = 102
```
raises an error.

Think:
```text
frozen=True
↓
Fields cannot be reassigned normally
```

---

# order=True
`order=True` generates ordering methods for the dataclass.

```python
@dataclass(order=True)
class Student:
    marks: int
    name: str
```
Now comparisons such as:
```python
student1 < student2
```
can work.

The fields are compared in the order they are defined.
---

# Dataclass vs Normal Class

| Normal Class | Dataclass |
|---|---|
| Write `__init__()` manually | Generated automatically |
| Often write `__repr__()` manually | Generated automatically |
| Often write `__eq__()` manually | Generated automatically |
| More boilerplate | Less boilerplate |
| Good for general behavior-heavy classes | Great for data-oriented classes |

---

# Real-World Applications

Dataclasses are useful for representing:
- Students
- Employees
- Products
- Configuration data
- API responses
- Database records
- Coordinates
- Application settings

Example:

```python
@dataclass
class Product:
    name: str
    price: float
    quantity: int
```

---

# Advantages
- Reduces boilerplate code
- Improves readability
- Works naturally with type hints
- Automatically generates useful methods
- Supports default values
- Supports validation
- Easy conversion to dictionaries and tuples
- Useful for structured data models

---

# Prerequisites

Before learning this module, you should know:
- Classes
- Objects
- `__init__()`
- `self`
- Type hints
- Lists and dictionaries
- Functions

---

# Mini Project

## Student Record Manager
We'll represent students using:
```python
@dataclass
class Student:
    roll_no: int
    name: str
    department: str
    marks: list[int]
```

The project will demonstrate:
- Creating dataclass objects
- Default values
- `default_factory`
- Methods inside dataclasses
- Student records
- Average calculation
- Object comparison and conversion

---

# Learning Outcomes

After completing this module, you'll be able to:
- Create classes using `@dataclass`.
- Understand automatically generated methods.
- Define dataclass fields.
- Use default values.
- Use `field()` and `default_factory`.
- Run initialization logic with `__post_init__()`.
- Convert objects using `asdict()` and `astuple()`.
- Create modified copies using `replace()`.
- Create frozen dataclasses.
- Enable ordering comparisons.

---

# Best Practices
- Use dataclasses for classes mainly designed to store structured data.
- Add clear type hints to fields.
- Use `default_factory` for mutable defaults.
- Keep required fields before fields with defaults.
- Use `__post_init__()` for simple validation or derived values.
- Use `frozen=True` when field reassignment should be prevented.
- Prefer a normal class when complex behavior is more important than stored data.

---

# Common Mistakes
## Mutable Default Values

Avoid:

```python
@dataclass
class Student:
    name: str
    marks: list[int] = []
```

Use:

```python
@dataclass
class Student:
    name: str
    marks: list[int] = field(
        default_factory=list
    )
```

---

## Wrong Field Order

Avoid:

```python
@dataclass
class Student:
    department: str = "CSE"
    name: str
```

Use:

```python
@dataclass
class Student:
    name: str
    department: str = "CSE"
```

---

## Assuming Type Hints Validate Data

This:
```python
@dataclass
class Student:
    age: int
```
does not automatically guarantee that `age` is an integer at runtime.
Type hints and runtime validation are different concepts.

---

# Quick Revision

| Need | Use |
|---|---|
| Create dataclass | `@dataclass` |
| Define field | `name: str` |
| Default value | `age: int = 18` |
| Customize field | `field()` |
| Mutable default | `default_factory` |
| Post-initialization logic | `__post_init__()` |
| Convert to dictionary | `asdict()` |
| Convert to tuple | `astuple()` |
| Modified copy | `replace()` |
| Prevent reassignment | `frozen=True` |
| Enable ordering | `order=True` |

---