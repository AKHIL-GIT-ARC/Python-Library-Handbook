# typing Module

The `typing` module is a built-in Python library used to provide **type hints** for variables, function parameters, return values, collections, and other objects.
Type hints make Python code easier to understand, maintain, debug, and analyze with tools such as IDEs and static type checkers.

---

# Why Use typing?

Without type hints:
```python
def add(a, b):
    return a + b
```
It is not immediately clear what type of values `a` and `b` should contain.
Using type hints:
```python
def add(a: int, b: int) -> int:
    return a + b
```

Now we know:

```text
a: int   → a should be an integer
b: int   → b should be an integer
-> int   → function should return an integer
```

---

# Important Note

Type hints do **not normally enforce types at runtime**.
Example:
```python
age: int = "nineteen"
print(age)
```
Python can still run this assignment.
Type hints mainly help:
- Developers understand code
- IDEs detect possible mistakes
- Static type checkers analyze code
- Teams maintain large projects

---

# Importing the Module

```python
import typing
```
Specific features can also be imported:

```python
from typing import Any, Optional, Union, Literal, Callable
```
Modern Python also supports many type hints without importing them from `typing`.

Example:

```python
names: list[str]
marks: dict[str, int]
```

---

# Concepts Covered

| Concept | Purpose |
|---|---|
| `int`, `str`, `float`, `bool` | Basic type annotations |
| `list[str]` | List containing strings |
| `tuple[int, int]` | Tuple containing integers |
| `dict[str, int]` | Dictionary with specified key/value types |
| `set[str]` | Set containing strings |
| `Any` | Accept any type |
| `Union` | Allow multiple types |
| `Optional` | Allow a type or `None` |
| `Literal` | Allow specific values |
| `Callable` | Describe a function |
| `TypeAlias` | Create a reusable type name |

---

# Variable Type Hints

Type hints can be added to variables.
```python
name: str = "Akhil"
age: int = 19
cgpa: float = 8.5
is_student: bool = True
```

The general syntax is:

```python
variable: type = value
```

---

# Function Type Hints

You can specify the expected types of parameters and return values.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

Here:

```text
name: str
```
means `name` should be a string.
```text
-> str
```
means the function should return a string.

---

# Function Returning Nothing

If a function doesn't return a value, use:

```python
-> None
```

Example:

```python
def display(name: str) -> None:
    print(name)
```

---

# Collection Type Hints

## List

```python
marks: list[int] = [80, 90, 75]
```

Means:

> `marks` is a list containing integers.

---

## Dictionary

```python
student: dict[str, int] = {
    "age": 19,
    "marks": 90
}
```

Means:

```text
str → key type
int → value type
```

---

## Tuple

```python
coordinates: tuple[int, int] = (10, 20)
```

---

## Set

```python
subjects: set[str] = {
    "Python",
    "Java",
    "SQL"
}
```

---

# Any

`Any` means a value can be of any type.

```python
from typing import Any

data: Any = 10
data = "Python"
data = [1, 2, 3]
```

Useful when the exact type is unknown or intentionally unrestricted.

---

# Union

`Union` allows multiple possible types.

```python
from typing import Union
value: Union[int, str]
```

The value can be either:

```text
int
or
str
```

Example:

```python
value = 100
```
or:
```python
value = "Python"
```
Modern Python can also use:

```python
value: int | str
```

---

# Optional

`Optional` means a value can contain a specific type **or `None`**.

```python
from typing import Optional
name: Optional[str] = None
```

Equivalent modern syntax:

```python
name: str | None = None
```

So:

```text
Optional[str]

means

str OR None
```

---

# Literal

`Literal` restricts a value to specific choices.

```python
from typing import Literal
status: Literal["active", "inactive"]
```

The intended values are:

```text
"active"
"inactive"
```
This is useful when only specific values should be accepted.

---

# Callable

`Callable` is used to describe functions.

```python
from typing import Callable
operation: Callable[[int, int], int]
```

This means:

```text
Function accepts:
int, int

Function returns:
int
```

Example:

```python
def add(a: int, b: int) -> int:
    return a + b

operation = add
```

---

# TypeAlias

A type alias gives a reusable name to a type.

```python
from typing import TypeAlias
StudentID: TypeAlias = int
```

Now:

```python
student_id: StudentID = 101
```
is easier to understand than simply:

```python
student_id: int = 101
```

For modern Python code, the newer `type` statement is also available in Python 3.12+:

```python
type StudentID = int
```

---

# Old vs Modern Syntax
Older Python code often uses:

```python
from typing import List, Dict, Tuple, Set
names: List[str]
marks: Dict[str, int]
point: Tuple[int, int]
subjects: Set[str]
```

Modern Python uses:
```python
names: list[str]
marks: dict[str, int]
point: tuple[int, int]
subjects: set[str]
```
Prefer the modern syntax when your Python version supports it.

---

# Real-World Applications

## APIs

```python
def get_user(user_id: int) -> dict[str, str]:
    ...
```

---

## Data Processing

```python
def average(values: list[float]) -> float:
    ...
```

---

## Student Management

```python
def create_student(
    name: str,
    age: int,
    marks: list[int]
) -> dict:
    ...
```

---

## Large Projects

Type hints help developers understand:
- What data a function expects
- What a function returns
- What collections contain
- Which values may be `None`

---

# Advantages
- Improves code readability
- Makes functions easier to understand
- Helps detect type-related mistakes
- Improves IDE suggestions and autocomplete
- Makes large projects easier to maintain
- Documents expected data types directly in code

---

# Prerequisites

Before learning this module, you should know:
- Variables
- Data types
- Functions
- Lists
- Tuples
- Dictionaries
- Sets
- Python imports

---

# Mini Project

## Student Record Validator

The project will use type hints for:
- Student names
- Ages
- Departments
- Marks
- Functions
- Collections
- Return values

Example:

```python
def calculate_average(marks: list[int]) -> float:
    return sum(marks) / len(marks)
```

---

# Learning Outcomes

After completing this module, you'll be able to:
- Add type hints to variables.
- Add parameter and return type annotations to functions.
- Type collections such as lists and dictionaries.
- Use `Any`, `Union`, and `Optional`.
- Restrict values using `Literal`.
- Describe functions using `Callable`.
- Create reusable type aliases.
- Write clearer and more maintainable Python code.

---

# Module Summary

| Topic | Covered |
|---|---|
| Variable annotations | ✅ |
| Function annotations | ✅ |
| Return types | ✅ |
| Collection types | ✅ |
| `Any` | ✅ |
| `Union` | ✅ |
| `Optional` | ✅ |
| `Literal` | ✅ |
| `Callable` | ✅ |
| Type aliases | ✅ |

---

# Best Practices

- Add type hints to function parameters and return values.
- Use modern built-in types like `list[str]` and `dict[str, int]`.
- Use `Any` only when necessary.
- Use `T | None` for optional values in modern Python.
- Keep type hints simple and readable.
- Use static type checkers when working on larger projects.

---

# Common Mistakes

- Assuming type hints automatically enforce types at runtime.
- Using `Any` everywhere.
- Forgetting to annotate return values.
- Creating unnecessarily complicated type hints.
- Confusing `Optional[str]` with an optional function argument.

Remember:
```python
Optional[str]
```

means:
```text
str | None
```

It does **not** mean the argument itself can simply be omitted.

---

# Quick Revision

| Need | Use |
|---|---|
| String | `str` |
| Integer | `int` |
| Float | `float` |
| Boolean | `bool` |
| List of integers | `list[int]` |
| Dictionary | `dict[str, int]` |
| Multiple possible types | `int \| str` |
| Type or None | `str \| None` |
| Any type | `Any` |
| Specific allowed values | `Literal` |
| Function type | `Callable` |
| Reusable type | Type alias |

---