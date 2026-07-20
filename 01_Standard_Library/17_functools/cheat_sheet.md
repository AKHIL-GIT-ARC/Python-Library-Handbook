# functools Module Cheat Sheet
## Import
```python
from functools import (
    partial,
    reduce,
    lru_cache,
    wraps,
    cmp_to_key,
    cached_property,
    total_ordering,
    singledispatch
)
```
The `functools` module provides higher-order functions and decorators for reusable, efficient, and optimized Python code.

---

# Functions Overview

| Function | Purpose |
|----------|---------|
| `partial()` | Fix function arguments |
| `reduce()` | Reduce an iterable to one value |
| `lru_cache()` | Cache function results |
| `wraps()` | Preserve decorator metadata |
| `cmp_to_key()` | Convert comparison function to sorting key |
| `cached_property()` | Cache computed class properties |
| `total_ordering()` | Generate comparison methods |
| `singledispatch()` | Function overloading by type |

---

# 1. partial()

**Purpose:** Creates a new function with some arguments already filled.

**Syntax**

```python
partial(function, *args, **kwargs)
```

**Example**

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, b=2)

print(double(10))
```

**Output**

```python
20
```

---

# 2. reduce()

**Purpose:** Applies a function cumulatively to reduce an iterable into a single value.

**Syntax**

```python
reduce(function, iterable)
```

**Example**

```python
from functools import reduce

numbers = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, numbers)

print(total)
```

**Output**

```python
10
```

---

# 3. lru_cache()

**Purpose:** Stores previously computed results to improve performance.

**Syntax**

```python
@lru_cache(maxsize=None)
```

**Example**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
```

**Output**

```python
55
```

---

# 4. wraps()

**Purpose:** Preserves the original function's metadata inside decorators.

**Syntax**

```python
@wraps(function)
```

**Example**

```python
from functools import wraps

def logger(func):

    @wraps(func)
    def wrapper():
        print("Running...")
        func()

    return wrapper
```

---

# 5. cmp_to_key()

**Purpose:** Converts a comparison function into a sorting key.

**Syntax**

```python
cmp_to_key(compare_function)
```

**Example**

```python
from functools import cmp_to_key

def compare(a, b):
    return a - b

numbers = [5, 3, 1]
numbers.sort(key=cmp_to_key(compare))
print(numbers)
```

**Output**

```python
[1, 3, 5]
```

---

# 6. cached_property()

**Purpose:** Computes a property once and caches the result.

**Syntax**

```python
@cached_property
```

**Example**

```python
from functools import cached_property

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2
```

---

# 7. total_ordering()

**Purpose:** Automatically creates missing comparison methods.

**Syntax**

```python
@total_ordering
```

**Example**

```python
from functools import total_ordering

@total_ordering
class Student:
    def __eq__(self, other):
        ...
    def __lt__(self, other):
        ...
```

---

# 8. singledispatch()

**Purpose:** Creates generic functions based on argument type.

**Syntax**

```python
@singledispatch
```

**Example**

```python
from functools import singledispatch

@singledispatch
def display(value):
    print("Unknown")

@display.register(int)
def _(value):
    print("Integer")
```

---

# partial() vs lambda

| partial() | lambda |
|------------|---------|
| Reuses existing function | Creates a new anonymous function |
| Cleaner for fixed arguments | Better for simple expressions |
| More readable | Can become complex |

---

# reduce() vs sum()

| reduce() | sum() |
|-----------|-------|
| Works with any operation | Only addition |
| Flexible | Simpler for numeric sums |

---

# cached_property() vs property()

| property() | cached_property() |
|-------------|-------------------|
| Recalculates every access | Calculates only once |
| No caching | Cached result |

---

# Best Practices

- Use `partial()` to avoid repeating fixed arguments.
- Use `reduce()` for cumulative operations.
- Use `lru_cache()` for expensive recursive functions.
- Always use `wraps()` when writing decorators.
- Use `cmp_to_key()` when a comparison function already exists.
- Use `cached_property()` for expensive calculations.
- Use `total_ordering()` to reduce comparison code.
- Use `singledispatch()` for type-specific behavior.

---

# Common Mistakes

- Forgetting `@wraps()` in decorators.
- Using `reduce()` when `sum()` is sufficient.
- Applying `lru_cache()` to functions with mutable arguments.
- Expecting `cached_property()` to update automatically after object changes.
- Forgetting that `singledispatch()` dispatches only on the first argument.

---

# When Should I Use This Module?

✅ **Use `functools` when:**

- Optimizing repeated calculations
- Writing decorators
- Building reusable functions
- Performing custom sorting
- Creating generic functions
- Working with functional programming

❌ **Avoid `functools` when:**

- A simple loop or function is clearer.
- Optimization is unnecessary.

---

# Memory Trick

```
partial()
↓

Fix Arguments

reduce()
↓

One Result

lru_cache()
↓

Remember Results

wraps()
↓

Keep Metadata

cmp_to_key()
↓

Custom Sorting

cached_property()
↓

Compute Once

total_ordering()
↓

Auto Comparisons

singledispatch()
↓

Dispatch By Type
```

---

# Quick Revision

| Need | Function |
|------|----------|
| Fix arguments | `partial()` |
| Aggregate values | `reduce()` |
| Speed up repeated calls | `lru_cache()` |
| Preserve decorator metadata | `wraps()` |
| Custom sorting | `cmp_to_key()` |
| Cache class property | `cached_property()` |
| Auto comparison methods | `total_ordering()` |
| Function overloading | `singledispatch()` |