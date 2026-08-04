# Exception Handling — Cheat Sheet

## Syntax

```python
try:
    # Risky code
except ExceptionType:
    # Handle exception
else:
    # Runs if no exception
finally:
    # Always runs
```

---

## `try`

Code that may cause an exception.

```python
try:
    result = 10 / 0
```

---

## `except`

Handles the exception.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## Multiple `except`

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## `else`

Runs only if no exception occurs.

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input.")
else:
    print(number)
```

---

## `finally`

Always executes.

```python
try:
    print("Start")
finally:
    print("End")
```

---

## `raise`

Raises an exception manually.

```python
age = 16
if age < 18:
    raise ValueError("Age must be 18 or above.")
```

---

## Common Exceptions

| Exception | Cause |
|-----------|-------|
| `ZeroDivisionError` | Divide by zero |
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `IndexError` | Invalid list index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File not found |

---

## Quick Revision

```text
try        → Risky code
except     → Handle error
else       → No error
finally    → Always executes
raise      → Raise exception
```

---

## Key Points

- `try` contains code that may fail.
- `except` catches and handles exceptions.
- `else` executes only when no exception occurs.
- `finally` always executes, even if an exception occurs.
- `raise` is used to create exceptions manually.
- Use multiple `except` blocks to handle different exception types.