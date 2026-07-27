# dataclasses Module Interview Questions

## Beginner Level

### 1. What is a dataclass in Python?

**Answer:**

A dataclass is a class mainly used to store data while reducing repetitive code.
```python
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
```
Python automatically generates common methods such as `__init__()`, `__repr__()`, and `__eq__()`.

---

### 2. How do you create a dataclass?

**Answer:**

Import `dataclass` and use the `@dataclass` decorator.

```python
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
```

---

### 3. What are fields in a dataclass?

**Answer:**

Fields are the variables defined inside a dataclass.

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

---

### 4. Which methods does `@dataclass` generate by default?

**Answer:**

Commonly:
```text
__init__()
__repr__()
__eq__()
```
This reduces the amount of code we need to write manually.

---

### 5. How do you create an object from a dataclass?

**Answer:**
```python
student = Student(
    "Akhil",
    19
)
```
Just like a normal class.

---

## Intermediate Level

### 6. How do you provide a default value?

**Answer:**

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
automatically uses `"CSE"`.

---

### 7. What is `field()`?

**Answer:**

`field()` is used to customize how a dataclass field behaves.

```python
from dataclasses import field
marks: list[int] = field(
    default_factory=list
)
```

---

### 8. What is `default_factory`?

**Answer:**

`default_factory` creates a new default value for each object.
```python
marks: list[int] = field(
    default_factory=list
)
```
Each student gets a separate empty list.

---

### 9. Why shouldn't we use a list directly as a mutable default?

Avoid:

```python
marks: list[int] = []
```

Use:
```python
marks: list[int] = field(
    default_factory=list
)
```

**Answer:**
Mutable default values should be created separately for each object. `default_factory=list` safely creates a new list whenever an object is created.

---

### 10. What is `__post_init__()`?

**Answer:**

`__post_init__()` runs automatically after the generated `__init__()` finishes.

```python
@dataclass
class Student:
    name: str
    age: int
    def __post_init__(self) -> None:
        if self.age <= 0:
            raise ValueError("Invalid age")
```
It is commonly used for validation and additional initialization.

---

## Advanced Level

### 11. What does `asdict()` do?

**Answer:**
It converts a dataclass object into a dictionary.

```python
data = asdict(student)
```
Example result:

```python
{
    "name": "Akhil",
    "age": 19
}
```

---

### 12. What does `astuple()` do?

**Answer:**
It converts a dataclass object into a tuple.
```python
data = astuple(student)
```

Example:
```python
("Akhil", 19)
```

---

### 13. What does `replace()` do?

**Answer:**
`replace()` creates a new dataclass object with selected field values changed.

```python
student2 = replace(
    student1,
    age=20
)
```
The original object remains unchanged.

---

### 14. What does `frozen=True` do?

**Answer:**
It prevents normal reassignment of dataclass fields after the object is created.

```python
@dataclass(frozen=True)
class Account:
    username: str
```

This:
```python
account.username = "Rahul"
```
raises an error.

---

### 15. What does `order=True` do?

**Answer:**

It enables ordering comparisons between dataclass objects.
```python
@dataclass(order=True)
class Score:
    marks: int
    name: str
```
Now comparisons such as:
```python
score1 < score2
```
can be performed.
Fields are compared in the order they are defined.

---

## Scenario-Based Questions

### 16. You need every Student object to have its own empty marks list. What should you use?

**Answer:**

```python
@dataclass
class Student:
    name: str
    marks: list[int] = field(
        default_factory=list
    )
```

---

### 17. You need to validate age immediately after creating an object. What should you use?

**Answer:**

Use:
```python
__post_init__()
```

Example:
```python
def __post_init__(self) -> None:
    if self.age <= 0:
        raise ValueError("Invalid age")
```

---

### 18. You need to convert a Student object to a dictionary. What should you use?

**Answer:**

```python
asdict(student)
```

---

### 19. You need a new copy of an object with one field changed. What should you use?

**Answer:**

```python
replace()
```

Example:

```python
new_student = replace(
    student,
    age=20
)
```

---

### 20. You don't want fields to be reassigned after object creation. What should you use?

**Answer:**

```python
@dataclass(frozen=True)
```

---

## Coding Questions

### 21. Convert this normal class into a dataclass.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**Answer:**

```python
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
```

---

### 22. Create a dataclass with a default department.

**Answer:**

```python
@dataclass
class Student:
    name: str
    department: str = "CSE"
```

---

### 23. Create a dataclass with an empty list for each object.

**Answer:**

```python
from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    marks: list[int] = field(
        default_factory=list
    )
```

---

### 24. Validate that age is greater than zero.

**Answer:**

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

---

### 25. Create a frozen dataclass.

**Answer:**

```python
@dataclass(frozen=True)
class User:
    user_id: int
    username: str
```

---

### 26. Create an orderable dataclass.

**Answer:**

```python
@dataclass(order=True)
class Score:
    marks: int
    name: str
```

---

## Dataclass vs Normal Class

| Normal Class | Dataclass |
|---|---|
| Usually write `__init__()` manually | Generated automatically |
| Often write `__repr__()` manually | Generated automatically |
| Often write `__eq__()` manually | Generated automatically |
| More boilerplate | Less boilerplate |
| Good for general classes | Great for data-oriented classes |

---

## Frequently Used Features

| Feature | Purpose |
|---|---|
| `@dataclass` | Create dataclass |
| `field()` | Customize field |
| `default_factory` | Create mutable defaults safely |
| `__post_init__()` | Post-initialization logic |
| `asdict()` | Convert to dictionary |
| `astuple()` | Convert to tuple |
| `replace()` | Create modified copy |
| `frozen=True` | Prevent field reassignment |
| `order=True` | Enable ordering |

---

## Best Practices

- Use dataclasses for data-oriented classes.
- Add type hints to fields.
- Put required fields before default fields.
- Use `default_factory` for mutable defaults.
- Use `__post_init__()` for simple validation.
- Use `frozen=True` when field reassignment should be prevented.
- Keep dataclasses simple and readable.

---

## Common Mistakes

### Using a Mutable Default

Wrong:

```python
marks: list[int] = []
```

Correct:

```python
marks: list[int] = field(
    default_factory=list
)
```

---

### Wrong Field Order

Wrong:

```python
@dataclass
class Student:
    age: int = 18
    name: str
```

Correct:

```python
@dataclass
class Student:
    name: str
    age: int = 18
```

---

### Assuming Type Hints Validate Values

```python
@dataclass
class Student:
    age: int
```

This does not automatically validate that `age` is actually an integer at runtime.

---

## Memory Trick

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

## Quick Revision

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
| Modified copy | `replace()` |
| Prevent reassignment | `frozen=True` |
| Enable ordering | `order=True` |

---

## Interview Tip

**Question:** What is the main advantage of a dataclass over a normal class?

**Answer:**

A dataclass reduces boilerplate code by automatically generating common methods such as `__init__()`, `__repr__()`, and `__eq__()`, making data-oriented classes cleaner and easier to maintain.