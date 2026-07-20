# functools Module

The `functools` module provides higher-order functions and utilities that work with callable objects. It helps you write cleaner, reusable, and more efficient code by supporting functional programming, caching, decorators, custom sorting, and generic functions.

---

# Why Use functools?

Without `partial()`:

```python
def multiply(a, b):
    return a * b

print(multiply(5, 10))
print(multiply(8, 10))
print(multiply(12, 10))
```

Using `partial()`:

```python
from functools import partial

def multiply(a, b):
    return a * b

multiply_by_10 = partial(multiply, b=10)

print(multiply_by_10(5))
print(multiply_by_10(8))
print(multiply_by_10(12))
```
Cleaner, reusable, and avoids repeating fixed arguments.

---

# Main Functions & Decorators

| Function | Purpose |
|----------|---------|
| `partial()` | Fix some function arguments |
| `reduce()` | Reduce an iterable to a single value |
| `lru_cache()` | Cache function results |
| `wraps()` | Preserve metadata in decorators |
| `cmp_to_key()` | Convert comparison function to a sorting key |
| `cached_property()` | Cache computed object properties |
| `total_ordering()` | Automatically generate comparison methods |
| `singledispatch()` | Function overloading based on argument type |

---

# Frequently Used Functions

## 1. partial()

Creates a new function with some arguments already filled.

```python
from functools import partial
def power(base, exponent):
    return base ** exponent
square = partial(power, exponent=2)
print(square(5))
```

Output

```python
25
```

---

## 2. reduce()

Applies a function repeatedly to reduce an iterable to one value.

```python
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
```

Output

```python
10
```

---

## 3. lru_cache()

Caches function results to improve performance.

```python
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
```

Output

```python
55
```

---

## 4. wraps()

Preserves the original function's metadata inside decorators.

```python
from functools import wraps
def logger(func):
    @wraps(func)
    def wrapper():
        print("Executing...")
        func()
    return wrapper
```

---

## 5. cmp_to_key()

Converts an old-style comparison function into a sorting key.
```python
from functools import cmp_to_key
def compare(a, b):
    return a - b
numbers = [5, 1, 4, 2]
numbers.sort(key=cmp_to_key(compare))
print(numbers)
```

Output

```python
[1, 2, 4, 5]
```

---

## 6. cached_property()

Calculates a property once and stores the result.

```python
from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2
circle = Circle(5)
print(circle.area)
```

---

## 7. total_ordering()

Automatically creates comparison methods.

```python
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, marks):
        self.marks = marks
    def __eq__(self, other):
        return self.marks == other.marks
    def __lt__(self, other):
        return self.marks < other.marks
```

---

## 8. singledispatch()

Creates generic functions based on argument type.

```python
from functools import singledispatch

@singledispatch
def display(value):
    print("Unknown Type")
@display.register(int)
def _(value):
    print("Integer:", value)
display(100)
```

Output

```python
Integer: 100
```

---

# Advantages

- Improves performance
- Reduces repetitive code
- Makes decorators cleaner
- Supports functional programming
- Increases code reusability
- Built into Python

---

# Real-World Applications

| Function | Example |
|----------|---------|
| `partial()` | Preconfigured functions |
| `reduce()` | Sum, product, maximum |
| `lru_cache()` | Fibonacci, API caching |
| `wraps()` | Logging decorators |
| `cmp_to_key()` | Custom sorting |
| `cached_property()` | Expensive calculations |
| `total_ordering()` | Custom objects |
| `singledispatch()` | Type-based processing |

---

# Module Summary

| Function | Best Used For |
|----------|---------------|
| `partial()` | Reusing functions |
| `reduce()` | Aggregating values |
| `lru_cache()` | Performance optimization |
| `wraps()` | Writing decorators |
| `cmp_to_key()` | Custom sorting |
| `cached_property()` | Cached properties |
| `total_ordering()` | Object comparisons |
| `singledispatch()` | Function overloading |

---

# Prerequisites

Before learning this module, you should know:

- Functions
- Lambda functions
- Decorators
- Classes
- Object-Oriented Programming

---

# Mini Project

In this module, you'll build a **Smart Utility Toolkit**.

Features:

- Cached factorial calculator
- Discount calculator
- Sum numbers using `reduce()`
- Sort student records
- Compare products

---

# Learning Outcomes

After completing this module, you'll be able to:

- Create reusable functions using `partial()`
- Aggregate data with `reduce()`
- Speed up programs using `lru_cache()`
- Write decorators using `wraps()`
- Perform custom sorting with `cmp_to_key()`
- Cache object properties with `cached_property()`
- Reduce comparison boilerplate using `total_ordering()`
- Build generic functions using `singledispatch()`