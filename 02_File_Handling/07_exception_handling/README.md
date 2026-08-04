# Exception Handling in Python

Exception handling allows a program to handle errors gracefully instead of crashing.

It is done using:

```text
try
except
else
finally
```

---

## What is an Exception?

An exception is an error that occurs while a program is running.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

Without exception handling, the program stops immediately.

---

## try

Place the code that may cause an error inside the `try` block.

```python
try:
    num = 10 / 0
```

---

## except

Handles the error if it occurs.

```python
try:
    num = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

---

## try-except Flow

```text
try
 │
 ├── No Error ─────► Continue
 │
 └── Error
       │
       ▼
    except
```

---

## Handling Multiple Exceptions

Use multiple `except` blocks.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## else

The `else` block runs only if no exception occurs.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)
```

---

## finally

The `finally` block always executes.

```python
try:
    print("Program Started")

finally:
    print("Program Ended")
```

Common use:

```python
file = open("notes.txt", "r")

try:
    print(file.read())

finally:
    file.close()
```

---

## raise

`raise` is used to generate an exception manually.

```python
age = 15

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

## Key Points

- `try` → Code that may raise an exception.
- `except` → Handles the exception.
- `else` → Runs if no exception occurs.
- `finally` → Always executes.
- `raise` → Creates an exception manually.
- Multiple `except` blocks can handle different exceptions.

---

## Quick Revision

| Keyword | Purpose |
|---------|---------|
| `try` | Risky code |
| `except` | Handle error |
| `else` | Runs if no error |
| `finally` | Always runs |
| `raise` | Raise an exception |