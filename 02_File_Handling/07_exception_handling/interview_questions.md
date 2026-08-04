# Exception Handling — Interview Questions

## 1. What is an exception in Python?

An exception is a runtime error that interrupts the normal execution of a program.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

---

## 2. Why is exception handling used?

It prevents the program from crashing and allows errors to be handled gracefully.

---

## 3. What is the purpose of `try`?

The `try` block contains code that may raise an exception.

```python
try:
    result = 10 / 0
```

---

## 4. What is the purpose of `except`?

It catches and handles an exception.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 5. What is the purpose of `else`?

The `else` block executes only if no exception occurs.

```python
try:
    number = int(input())
except ValueError:
    print("Invalid input.")
else:
    print("Valid input")
```

---

## 6. What is the purpose of `finally`?

The `finally` block always executes, whether an exception occurs or not.

```python
try:
    print("Program started")
finally:
    print("Program ended")
```

---

## 7. What is `raise`?

`raise` is used to generate an exception manually.

```python
age = 16
if age < 18:
    raise ValueError("Age must be 18 or above.")
```

---

## 8. How do you handle multiple exceptions?

Use multiple `except` blocks.

```python
try:
    number = int(input())
    result = 10 / number
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 9. Name some common built-in exceptions.

| Exception | Cause |
|-----------|-------|
| `ZeroDivisionError` | Divide by zero |
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `IndexError` | Invalid list index |
| `KeyError` | Missing dictionary key |
| `FileNotFoundError` | File not found |

---

## 10. What is the execution order of exception handling blocks?

```text
try
 ↓
except (if exception occurs)
 ↓
else (if no exception)
 ↓
finally (always executes)
```

---

## Quick Revision

```text
try        → Risky code
except     → Handle exception
else       → Runs if no exception
finally    → Always runs
raise      → Raise exception

ZeroDivisionError → Divide by zero
ValueError        → Invalid value
TypeError         → Wrong data type
IndexError        → Invalid index
KeyError          → Missing key
FileNotFoundError → File not found
```