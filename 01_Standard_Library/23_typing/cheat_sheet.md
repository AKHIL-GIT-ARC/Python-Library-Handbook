# typing Module Cheat Sheet

## Import

```python
from typing import Any, Union, Optional, Literal, Callable, TypeAlias
```

The `typing` module provides tools for adding **type hints** to Python code.
Type hints improve readability and help IDEs and static type checkers detect possible type-related mistakes.

---

# 1. Variable Type Hints

**Purpose:** Shows the expected type of a variable.

**Syntax**

```python
variable: type = value
```

**Example**

```python
name: str = "Akhil"
age: int = 19
cgpa: float = 8.5
is_student: bool = True
```
---

# 2. Function Parameter Type Hints
**Purpose:** Shows the expected types of function parameters.
```python
def add(a: int, b: int):
    return a + b
```
Here:
```text
a → int
b → int
```
---

# 3. Return Type
**Purpose:** Shows the expected type returned by a function.
```python
def add(a: int, b: int) -> int:
    return a + b
```

Here:
```text
-> int
```
means the function should return an integer.

---

# 4. None Return Type
Use `-> None` when a function doesn't return a useful value.

```python
def greet(name: str) -> None:
    print(f"Hello, {name}")
```

---

# 5. list

**Purpose:** Specifies the type of values stored inside a list.
```python
marks: list[int] = [80, 90, 75]
```

Means:

```text
list containing integers
```

Another example:

```python
names: list[str] = ["Akhil", "Rahul"]
```

---

# 6. dict

**Purpose:** Specifies dictionary key and value types.

```python
student: dict[str, int] = {
    "age": 19,
    "marks": 90
}
```

Read:
```text
dict[str, int]
     ↓    ↓
    key  value
```

---

# 7. tuple

**Purpose:** Specifies the types and positions of tuple elements.

```python
coordinates: tuple[int, int] = (10, 20)
```
For any number of integers:
```python
numbers: tuple[int, ...] = (10, 20, 30, 40)
```

---

# 8. set

**Purpose:** Specifies the type of values stored in a set.

```python
subjects: set[str] = {
    "Python",
    "Java",
    "SQL"
}
```

---

# 9. Any

**Purpose:** Allows any type.

```python
from typing import Any
data: Any = 100
data = "Python"
data = [1, 2, 3]
```

Memory tip:
```text
Any → Anything
```

Use `Any` only when necessary because it reduces the benefits of type checking.

---

# 10. Union

**Purpose:** Allows multiple possible types.

```python
from typing import Union
student_id: Union[int, str]
```

Means:
```text
int OR str
```

Modern Python syntax:
```python
student_id: int | str
```

---

# 11. Optional

**Purpose:** Allows a type or `None`.

```python
from typing import Optional
email: Optional[str] = None
```

Means:
```text
str OR None
```

Modern syntax:
```python
email: str | None = None
```

Remember:
```text
Optional[str]
      ↓
str | None
```
`Optional` does not mean the function argument itself can be omitted.

---

# 12. Literal

**Purpose:** Restricts a value to specific allowed values.

```python
from typing import Literal
status: Literal[
    "active",
    "inactive"
]
```
Expected values:

```text
active
inactive
```

Another example:

```python
Department = Literal[
    "CSE",
    "ECE",
    "ME",
    "CE"
]
```

---

# 13. Callable

**Purpose:** Describes the parameter and return types of a callable, such as a function.

```python
from typing import Callable
operation: Callable[[int, int], int]
```

Read:

```text
Callable[[input types], return type]
Callable[[int, int], int]
          ↓    ↓      ↓
          inputs      return
```

Example:
```python
def add(a: int, b: int) -> int:
    return a + b
operation: Callable[[int, int], int] = add
```

---

# 14. TypeAlias

**Purpose:** Creates a reusable name for a type.

```python
from typing import TypeAlias
StudentID: TypeAlias = int
```

Now:
```python
student_id: StudentID = 101
```
`StudentID` is an alias for `int`.
Python 3.12+ also supports:
```python
type StudentID = int
```

---

# Collection Type Hints

| Data Structure | Type Hint |
|---|---|
| List of integers | `list[int]` |
| List of strings | `list[str]` |
| Dictionary | `dict[str, int]` |
| Two integers in tuple | `tuple[int, int]` |
| Variable-length integer tuple | `tuple[int, ...]` |
| Set of strings | `set[str]` |

---

# Function Type Hint Example

```python
def calculate_average(
    marks: list[int]
) -> float:

    return sum(marks) / len(marks)
```

Read:
```text
marks
↓
list[int]

return
↓
float
```

---

# Multiple Possible Return Types

```python
def find_student(
    student_id: int
) -> str | None:
    if student_id == 101:
        return "Akhil"
    return None
```

The function can return:
```text
str
OR
None
```

---

# Old vs Modern Syntax

Older syntax:
```python
from typing import List, Dict, Tuple, Set
names: List[str]
student: Dict[str, int]
point: Tuple[int, int]
subjects: Set[str]
```
Modern syntax:
```python
names: list[str]
student: dict[str, int]
point: tuple[int, int]
subjects: set[str]
```
For modern Python, prefer the built-in collection syntax.

---

# Type Hints vs Validation

Type hint:

```python
age: int
```

Means:

```text
age should be an integer
```

Runtime validation:

```python
if age < 0:
    print("Invalid age")
```

actually checks the value while the program runs.

```text
Type Hint
↓
Describes expected type

Validation
↓
Checks actual value
```

---

# Best Practices

- Add type hints to function parameters.
- Add return type annotations.
- Prefer modern syntax such as `list[int]`.
- Prefer `int | str` over `Union[int, str]` in modern Python.
- Prefer `str | None` over `Optional[str]` in modern Python.
- Use `Any` only when necessary.
- Keep type hints simple and readable.
- Use `Literal` when only specific values are valid.

---

# Common Mistakes

❌ Assuming type hints enforce types automatically.

```python
age: int = "nineteen"
```

Python normally still allows this at runtime.

---

❌ Using `Any` everywhere.

```python
name: Any
age: Any
marks: Any
```

This removes much of the benefit of type checking.
Prefer specific types:
```python
name: str
age: int
marks: list[int]
```

---

❌ Confusing `Optional` with an optional parameter.
```python
def greet(name: Optional[str]):
    ...
```

This means:
```text
name can be str or None
```

It does not mean `name` can be omitted.
To make it omittable, provide a default:

```python
def greet(name: str | None = None):
    ...
```

---

❌ Incorrect dictionary types.

```python
student: dict[str, int] = {
    "name": "Akhil"
}
```

The annotation says values should be `int`, but `"Akhil"` is a `str`.

---

# Memory Trick

```text
name: str
↓
String

age: int
↓
Integer

-> int
↓
Returns Integer

list[int]
↓
List of Integers

dict[str, int]
↓
String Keys + Integer Values

Any
↓
Anything

Union
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

# Quick Revision

| Need | Use |
|---|---|
| String | `str` |
| Integer | `int` |
| Float | `float` |
| Boolean | `bool` |
| No useful return value | `-> None` |
| List of integers | `list[int]` |
| Dictionary | `dict[str, int]` |
| Tuple | `tuple[int, int]` |
| Set | `set[str]` |
| Any type | `Any` |
| Multiple types | `int \| str` |
| Type or None | `str \| None` |
| Specific values | `Literal[...]` |
| Function type | `Callable[...]` |
| Type alias | `TypeAlias` |

---

# Interview Tip

**Question:** Do Python type hints enforce data types at runtime?

**Answer:**
No. Type hints mainly describe the expected types and help developers, IDEs, and static type checkers identify possible type errors.
For example:
```python
age: int = "nineteen"
```
Python normally allows this assignment at runtime, even though it does not match the type annotation.