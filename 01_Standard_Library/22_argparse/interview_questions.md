# argparse Module Interview Questions

## Beginner Level

### 1. What is the `argparse` module?

**Answer:**

The `argparse` module is a built-in Python library used to create command-line interfaces and accept arguments directly from the terminal.

---

### 2. Why do we use `argparse`?

**Answer:**

It allows a Python program to:
- Accept command-line arguments
- Validate input
- Convert data types
- Generate help messages
- Build professional CLI applications

---

### 3. How do you import `argparse`?

**Answer:**

```python
import argparse
```

---

### 4. What is `ArgumentParser()`?

**Answer:**

`ArgumentParser()` creates an object that manages command-line arguments.

```python
parser = argparse.ArgumentParser()
```

---

### 5. What does `add_argument()` do?

**Answer:**

`add_argument()` defines an argument that the program can accept.

```python
parser.add_argument("name")
```

Run:

```bash
python app.py Akhil
```

---

## Intermediate Level

### 6. What does `parse_args()` do?

**Answer:**

`parse_args()` reads the command-line arguments and stores them in an object.

```python
args = parser.parse_args()
```

You can then access values using:

```python
args.name
```

---

### 7. What is a positional argument?

**Answer:**

A positional argument is identified by its position in the command and is usually required.

```python
parser.add_argument("name")
```

Run:

```bash
python app.py Akhil
```

Here, `Akhil` becomes:

```python
args.name
```

---

### 8. What is an optional argument?

**Answer:**

An optional argument uses a flag such as `--age`.

```python
parser.add_argument("--age")
```

Run:

```bash
python app.py --age 19
```

---

### 9. What does `type` do?

**Answer:**

`type` converts and validates an argument's data type.

```python
parser.add_argument(
    "--age",
    type=int
)
```

Now `args.age` will contain an integer.

---

### 10. What does `default` do?

**Answer:**

It provides a fallback value when the user doesn't supply the argument.

```python
parser.add_argument(
    "--country",
    default="India"
)
```

---

## Advanced Level

### 11. What does `required=True` do?

**Answer:**

It makes an optional argument compulsory.

```python
parser.add_argument(
    "--email",
    required=True
)
```

The user must provide `--email`.

---

### 12. What does `choices` do?

**Answer:**

`choices` restricts an argument to specific values.

```python
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME"]
)
```

Valid:

```bash
python app.py --department CSE
```

Invalid:

```bash
python app.py --department Civil
```

---

### 13. What does `action="store_true"` do?

**Answer:**

It creates a Boolean flag.

```python
parser.add_argument(
    "--verbose",
    action="store_true"
)
```

If the user runs:

```bash
python app.py --verbose
```

then:

```python
args.verbose
```

is:

```text
True
```

Without `--verbose`, it is `False`.

---

### 14. What is `nargs`?

**Answer:**

`nargs` controls how many values an argument can accept.

```python
parser.add_argument(
    "name",
    nargs="?"
)
```

Here, `?` means zero or one value.

---

### 15. What are the common `nargs` values?

| Value | Meaning |
|---|---|
| `?` | Zero or one |
| `*` | Zero or more |
| `+` | One or more |
| `2` | Exactly two |

---

## Scenario-Based Questions

### 16. You need to accept a user's age as an integer. What should you use?

**Answer:**

```python
parser.add_argument(
    "--age",
    type=int
)
```

---

### 17. You want the default country to be India. What should you use?

**Answer:**

```python
parser.add_argument(
    "--country",
    default="India"
)
```

---

### 18. You only want users to select `CSE`, `ECE`, or `ME`. What should you use?

**Answer:**

```python
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME"]
)
```

---

### 19. You want a `--verbose` flag that becomes `True` when provided. What should you use?

**Answer:**

```python
parser.add_argument(
    "--verbose",
    action="store_true"
)
```

---

### 20. You want an argument to accept multiple filenames. What can you use?

**Answer:**

```python
parser.add_argument(
    "files",
    nargs="+"
)
```
This accepts one or more filenames.

---

## Coding Questions

### 21. Create an argument parser.

```python
parser = argparse.ArgumentParser()
```

---

### 22. Create a positional argument called `name`.

```python
parser.add_argument("name")
```

---

### 23. Create an optional integer argument called `age`.

```python
parser.add_argument(
    "--age",
    type=int
)
```

---

### 24. Create an argument with a default value.

```python
parser.add_argument(
    "--country",
    default="India"
)
```

---

### 25. Create a Boolean flag.

```python
parser.add_argument(
    "--verbose",
    action="store_true"
)
```

---

### 26. Parse command-line arguments.

```python
args = parser.parse_args()
```

---

## Frequently Used Features

| Feature | Purpose |
|---|---|
| `ArgumentParser()` | Create parser |
| `add_argument()` | Define arguments |
| `parse_args()` | Parse arguments |
| `type` | Set data type |
| `default` | Default value |
| `required` | Make optional argument compulsory |
| `choices` | Restrict values |
| `help` | Argument description |
| `action` | Define argument behavior |
| `nargs` | Number of accepted values |

---

## Best Practices

- Use meaningful argument names.
- Provide `help` descriptions.
- Use `type` for input validation.
- Use `choices` when valid options are limited.
- Use sensible default values.
- Use flags for Boolean options.
- Keep CLI commands simple and readable.

---

## Common Mistakes

- Forgetting to call `parse_args()`.
- Forgetting `--` for optional arguments.
- Not specifying `type` when conversion is required.
- Providing values outside `choices`.
- Confusing positional and optional arguments.
- Using `required=True` unnecessarily with positional arguments.

---

## Memory Trick

```text
ArgumentParser()
↓
Create Parser

add_argument()
↓
Define Input

parse_args()
↓
Read Input

type
↓
Data Type

default
↓
Fallback

required
↓
Must Provide

choices
↓
Allowed Values

help
↓
Description

action="store_true"
↓
Boolean Flag

nargs
↓
Number of Values
```

---

## Quick Revision

| Need | Use |
|---|---|
| Create parser | `ArgumentParser()` |
| Add argument | `add_argument()` |
| Read arguments | `parse_args()` |
| Positional argument | `"name"` |
| Optional argument | `"--name"` |
| Integer input | `type=int` |
| Default value | `default=value` |
| Required optional argument | `required=True` |
| Restrict values | `choices=[...]` |
| Help text | `help="..."` |
| Boolean flag | `action="store_true"` |
| Zero or one value | `nargs="?"` |
| Zero or more | `nargs="*"` |
| One or more | `nargs="+"` |

---

## Interview Tip

**Question:** What is the difference between `input()` and `argparse`?

**Answer:**

`input()` asks the user for information while the program is already running.
```python
name = input("Enter name: ")
```
`argparse` receives the information when the program is launched from the terminal.
```bash
python app.py Akhil
```
`argparse` is better suited for command-line tools, scripts, automation, and professional CLI applications.