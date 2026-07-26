# typing Module Interview Questions

## Beginner Level

### 1. What is the `typing` module?

**Answer:**
The `typing` module provides tools for adding type hints to Python code.
Type hints describe the expected types of variables, function parameters, return values, and collections.

---

### 2. What is a type hint?

**Answer:**
A type hint describes the expected data type of a variable or function.
```python
name: str = "Akhil"
age: int = 19
```
Here:
```text
name → str
age  → int
```

---

### 3. Do type hints enforce types at runtime?

**Answer:**
No.

Type hints mainly help:
- Developers
- IDEs
- Static type checkers
- Code readability
Python normally does not enforce them automatically.

---

### 4. How do you add type hints to function parameters?

**Answer:**
```python
def add(a: int, b: int):
    return a + b
```
Here, both `a` and `b` are expected to be integers.

---

### 5. How do you specify a function's return type?

**Answer:**
Use `->`.

```python
def add(a: int, b: int) -> int:
    return a + b
```
`-> int` means the function should return an integer.

---

## Intermediate Level

### 6. What does `-> None` mean?

**Answer:**

It means the function does not return a useful value.
```python
def greet(name: str) -> None:
    print(name)
```

---

### 7. How do you type hint a list of integers?

**Answer:**

```python
marks: list[int]
```
Example:
```python
marks: list[int] = [80, 90, 75]
```

---

### 8. How do you type hint a dictionary?

**Answer:**

```python
student: dict[str, int]
```
This means:
```text
keys   → str
values → int
```

---

### 9. What is `Any`?

**Answer:**

`Any` means a value can be of any type.

```python
from typing import Any
data: Any = 100
data = "Python"
```
Use `Any` only when necessary because it reduces type-checking benefits.

---

### 10. What is `Union`?
**Answer:**
`Union` means a value can have one of multiple types.

```python
from typing import Union
student_id: Union[int, str]
```

Modern syntax:
```python
student_id: int | str
```

Both mean:
```text
int OR str
```

---

## Advanced Level

### 11. What is `Optional`?

**Answer:**

`Optional` means a value can have a particular type or `None`.

```python
from typing import Optional
email: Optional[str] = None
```

Equivalent modern syntax:
```python
email: str | None = None
```

---

### 12. Does `Optional[str]` mean a function parameter can be omitted?

**Answer:**
No.
```python
def greet(name: Optional[str]):
    ...
```
`name` is still required, but its value can be:
```text
str
OR
None
```
To make the argument omittable:
```python
def greet(name: str | None = None):
    ...
```

---

### 13. What is `Literal`?

**Answer:**

`Literal` describes specific allowed values.

```python
from typing import Literal
status: Literal["active", "inactive"]
```
The intended values are:
```text
"active"
"inactive"
```

---

### 14. What is `Callable`?

**Answer:**

`Callable` is used to describe a callable such as a function.

```python
from typing import Callable
operation: Callable[[int, int], int]
```

This means:
```text
Accepts → int, int
Returns → int
```

Example:
```python
def add(a: int, b: int) -> int:
    return a + b
operation: Callable[[int, int], int] = add
```

---

### 15. What is a type alias?

**Answer:**

A type alias gives another name to a type.

```python
from typing import TypeAlias
StudentID: TypeAlias = int
```
Now:
```python
student_id: StudentID = 101
```
This can make code easier to understand.

---

## Scenario-Based Questions

### 16. You need a variable that can contain either an integer or string. What should you use?

**Answer:**

```python
value: int | str
```

Older syntax:

```python
value: Union[int, str]
```

---

### 17. A user's email can be a string or `None`. How would you type it?

**Answer:**

```python
email: str | None
```

Or:

```python
email: Optional[str]
```

---

### 18. You need a list containing only integer marks. How would you type it?

**Answer:**

```python
marks: list[int]
```

---

### 19. A function receives two integers and returns an integer. How would you describe it with `Callable`?

**Answer:**

```python
Callable[[int, int], int]
```

---

### 20. A variable should only have `"pending"`, `"approved"`, or `"rejected"`. What should you use?

**Answer:**

```python
from typing import Literal

status: Literal[
    "pending",
    "approved",
    "rejected"
]
```

---

## Coding Questions

### 21. Add type hints to this function.

```python
def multiply(a, b):
    return a * b
```

**Answer:**

```python
def multiply(a: int, b: int) -> int:
    return a * b
```

---

### 22. Create a list of student names with a type hint.

**Answer:**

```python
students: list[str] = [
    "Akhil",
    "Charm",
    "Om"
]
```

---

### 23. Create a function that accepts a list of integers and returns a float.

**Answer:**

```python
def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)
```

---

### 24. Create a variable that accepts `int`, `float`, or `None`.

**Answer:**

```python
value: int | float | None = None
```

---

### 25. Create a function that returns either a string or `None`.

**Answer:**

```python
def find_user(user_id: int) -> str | None:
    if user_id == 101:
        return "Akhil"
    return None
```

---

### 26. Create a `Literal` for student departments.

**Answer:**

```python
from typing import Literal
Department = Literal[
    "CSE",
    "ECE",
    "ME",
    "CE"
]
```

---

## Old vs Modern Syntax

| Older Syntax | Modern Syntax |
|---|---|
| `List[int]` | `list[int]` |
| `Dict[str, int]` | `dict[str, int]` |
| `Tuple[int, int]` | `tuple[int, int]` |
| `Set[str]` | `set[str]` |
| `Union[int, str]` | `int \| str` |
| `Optional[str]` | `str \| None` |

---

## Frequently Used Types

| Type | Purpose |
|---|---|
| `str` | String |
| `int` | Integer |
| `float` | Floating-point number |
| `bool` | Boolean |
| `list[int]` | List of integers |
| `dict[str, int]` | Dictionary |
| `tuple[int, int]` | Tuple |
| `set[str]` | Set |
| `Any` | Any type |
| `Union` / `\|` | Multiple possible types |
| `Optional` | Type or `None` |
| `Literal` | Specific values |
| `Callable` | Callable/function type |
| `TypeAlias` | Reusable type name |

---

## Best Practices

- Type function parameters and return values.
- Prefer specific types over `Any`.
- Use modern built-in collection types such as `list[int]`.
- Use `T | None` for nullable values in modern Python.
- Use `Literal` when only specific values are valid.
- Keep annotations simple and readable.
- Remember that type hints and runtime validation are different things.

---

## Common Mistakes

- Assuming Python automatically enforces type hints.
- Using `Any` unnecessarily.
- Forgetting return type annotations.
- Confusing `Optional` with an argument having a default value.
- Using the wrong collection element types.
- Making annotations unnecessarily complicated.

---

## Memory Trick

```text
variable: type
↓
Variable Type

parameter: type
↓
Parameter Type

-> type
↓
Return Type

list[int]
↓
List of Integers

Any
↓
Anything

Union / |
↓
OR

Optional
↓
Type OR None

Literal
↓
Specific Values

Callable
↓
Function

TypeAlias
↓
Reusable Type Name
```

---

## Quick Revision

| Need | Use |
|---|---|
| Variable type | `name: str` |
| Parameter type | `name: str` |
| Return type | `-> str` |
| No useful return | `-> None` |
| List of integers | `list[int]` |
| Dictionary | `dict[str, int]` |
| Any type | `Any` |
| Multiple types | `int \| str` |
| Type or None | `str \| None` |
| Specific values | `Literal[...]` |
| Function type | `Callable[...]` |
| Reusable type | Type alias |

---

## Interview Tip

**Question:** What is the main purpose of type hints if Python doesn't enforce them at runtime?

**Answer:**

Type hints make code easier to understand and maintain. They also allow IDEs and static type checkers to detect possible type-related mistakes before the program runs.