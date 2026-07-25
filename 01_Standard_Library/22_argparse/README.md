# argparse Module

The `argparse` module is a built-in Python library used to create **command-line interfaces (CLI)**. It allows users to pass arguments to a Python program through the terminal instead of using `input()`.

It automatically parses command-line arguments, validates input, generates help messages, and makes your programs more professional and user-friendly.

---

# Why Use argparse?

Using `input()`:

```python
name = input("Enter your name: ")
print(name)
```

Run

```text
Enter your name: Akhil
```

Using `argparse`:

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name")
args = parser.parse_args()
print(args.name)
```

Run

```bash
python app.py Akhil
```

Output

```text
Akhil
```

The user provides the input directly while running the program.

---

# Importing the Module

```python
import argparse
```

---

# Functions and Classes Covered

| Function / Class | Purpose |
|------------------|---------|
| `ArgumentParser()` | Creates a command-line parser |
| `add_argument()` | Adds command-line arguments |
| `parse_args()` | Reads and parses arguments |
| `default` | Sets a default value |
| `required` | Makes an optional argument mandatory |
| `type` | Specifies the data type |
| `choices` | Restricts valid values |
| `help` | Displays help information |
| `action` | Defines special argument behavior |

---

# Why Learn argparse?

The `argparse` module is widely used in:

- Command-line tools
- DevOps automation
- System administration
- Cybersecurity scripts
- Machine learning programs
- Data processing utilities
- Backup scripts
- Python utilities

---

# Advantages

- Eliminates repeated use of `input()`
- Automatically validates arguments
- Generates help messages
- Supports optional and required arguments
- Supports different data types
- Built into Python

---

# Common Operations

## Creating a Parser

```python
import argparse
parser = argparse.ArgumentParser()
```

---

## Adding a Positional Argument

```python
parser.add_argument("name")
```

Run

```bash
python app.py Akhil
```

Output

```text
Akhil
```

---

## Parsing Arguments

```python
args = parser.parse_args()
```

This stores all command-line arguments inside the `args` object.

---

## Optional Arguments

```python
parser.add_argument("--age")
```

Run

```bash
python app.py --age 19
```

---

## Default Value

```python
parser.add_argument(
    "--city",
    default="Rajkot"
)
```

If the user doesn't provide a city, `"Rajkot"` is used automatically.

---

## Required Optional Argument

```python
parser.add_argument(
    "--email",
    required=True
)
```

The program won't run unless `--email` is provided.

---

## Data Type

```python
parser.add_argument(
    "--age",
    type=int
)
```

Only integer values are accepted.

---

## Choices

```python
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME"]
)
```

Only these values are allowed.

---

## Help Message

```python
parser.add_argument(
    "--name",
    help="Enter student name"
)
```

Run

```bash
python app.py --help
``

The help message is displayed automatically.`

---

## Boolean Flag

```python
parser.add_argument(
    "--verbose",
    action="store_true"
)
```

Run

```bash
python app.py --verbose
```

If `--verbose` is present:

```python
args.verbose
```

becomes

```python
True
```

Otherwise:

```python
False
```

---

# Real-World Applications

## DevOps

- Deployment scripts
- Automation tools

---

## Cybersecurity

- Network scanners
- Password auditing tools

---

## Machine Learning

- Training models
- Passing dataset paths

---

## Data Processing

- CSV processing
- Report generation

---

## System Administration

- Backup scripts
- File management tools

---

# Prerequisites

Before learning this module, you should know:

- Variables
- Functions
- Python imports
- Command Prompt or Terminal
- Basic Python execution

---

# Mini Project

## Student CLI Manager

Features:

- Add Student
- Delete Student
- Search Student
- List Students
- Display Help
- Command-line Interface

---

# Learning Outcomes

After completing this module, you'll be able to:

- Create command-line applications.
- Accept user input through terminal arguments.
- Validate user input.
- Create optional and required arguments.
- Generate professional help messages.
- Build CLI tools similar to Git and Pip.

---

# Best Practices

- Give meaningful argument names.
- Use `type` to validate input.
- Use `choices` whenever possible.
- Provide helpful descriptions using `help`.
- Use optional arguments for optional information.
- Display friendly help messages.

---

# Common Mistakes

- Forgetting to call `parse_args()`.
- Using optional arguments without `--`.
- Forgetting to specify the correct data type.
- Using `required=True` for positional arguments.
- Giving invalid values when using `choices`.

---

# Quick Revision

| Need | Use |
|------|-----|
| Create parser | `ArgumentParser()` |
| Add argument | `add_argument()` |
| Read arguments | `parse_args()` |
| Default value | `default` |
| Required argument | `required=True` |
| Set data type | `type` |
| Restrict values | `choices` |
| Help message | `help` |
| Boolean flag | `action="store_true"` |

---