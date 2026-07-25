# argparse Module Cheat Sheet

## Import

```python
import argparse
```
The `argparse` module is used to create command-line programs that accept arguments directly from the terminal.

---

# Functions & Options Overview

| Function / Option | Purpose |
|-------------------|---------|
| `ArgumentParser()` | Create argument parser |
| `add_argument()` | Define an argument |
| `parse_args()` | Read command-line arguments |
| `type` | Set argument data type |
| `default` | Set default value |
| `required` | Make optional argument required |
| `choices` | Restrict allowed values |
| `help` | Add help description |
| `action` | Define special argument behavior |
| `nargs` | Control number of accepted values |

---

# 1. ArgumentParser()

**Purpose:** Creates the command-line argument parser.

**Syntax**

```python
parser = argparse.ArgumentParser()
```

**Example**

```python
import argparse
parser = argparse.ArgumentParser(
    description="Student Manager"
)
```

---

# 2. add_argument()

**Purpose:** Defines an argument that the program can accept.

**Syntax**

```python
parser.add_argument("argument")
```

**Example**

```python
parser.add_argument("name")
```

Run:

```bash
python app.py Akhil
```

---

# 3. parse_args()

**Purpose:** Reads the arguments provided through the terminal.

```python
args = parser.parse_args()
```

If you run:

```bash
python app.py Akhil
```

Then:

```python
args.name
```

contains:

```text
Akhil
```

---

# 4. Positional Arguments

**Purpose:** Arguments that must be provided in the correct position.

```python
parser.add_argument("name")
```

Run:

```bash
python app.py Akhil
```

Here:

```text
Akhil → args.name
```

The argument name is written without `--`.

---

# 5. Optional Arguments

**Purpose:** Arguments that are identified using `--`.

```python
parser.add_argument("--age")
```

Run:

```bash
python app.py Akhil --age 19
```

Access:

```python
args.age
```

If `--age` is not provided:

```python
args.age
```

will normally be:

```python
None
```

---

# 6. type

**Purpose:** Converts and validates the argument's data type.

```python
parser.add_argument(
    "--age",
    type=int
)
```

Run:

```bash
python app.py Akhil --age 19
```

Now:

```python
args.age
```

is an integer:

```text
19
```

---

# 7. default

**Purpose:** Provides a value when the user does not give the argument.

```python
parser.add_argument(
    "--country",
    default="India"
)
```

Run:

```bash
python app.py Akhil
```

Then:

```python
args.country
```

contains:

```text
India
```

---

# 8. required

**Purpose:** Makes an optional argument compulsory.

```python
parser.add_argument(
    "--email",
    required=True
)
```

The user must provide:

```bash
python app.py Akhil --email akhil@example.com
```

Otherwise, `argparse` displays an error.

> Positional arguments are required by default, so `required=True` is mainly used with optional arguments such as `--email`.

---

# 9. choices

**Purpose:** Restricts an argument to specific values.

```python
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME"]
)
```

Valid:

```bash
python app.py Akhil --department CSE
```

Invalid:

```bash
python app.py Akhil --department AIML
```
`argparse` automatically displays an error for invalid choices.

---

# 10. help

**Purpose:** Adds a description for an argument.

```python
parser.add_argument(
    "--age",
    type=int,
    help="Enter your age"
)
```

Run:

```bash
python app.py --help
```

`argparse` automatically displays the help information.

---

# 11. action="store_true"

**Purpose:** Creates a Boolean flag.

```python
parser.add_argument(
    "--verbose",
    action="store_true"
)
```

Without:

```bash
python app.py Akhil
```

```text
args.verbose → False
```

With:

```bash
python app.py Akhil --verbose
```

```text
args.verbose → True
```

---

# 12. nargs

**Purpose:** Controls how many values an argument accepts.

Example:

```python
parser.add_argument(
    "name",
    nargs="?"
)
```

`?` means the argument accepts **zero or one value**.

So both can work:

```bash
python app.py list
```

and

```bash
python app.py search Akhil
```

---

# Common nargs Values

| Value | Meaning |
|-------|---------|
| `?` | Zero or one |
| `*` | Zero or more |
| `+` | One or more |
| `2` | Exactly two |

Example:

```python
parser.add_argument(
    "numbers",
    nargs="+",
    type=int
)
```

Run:

```bash
python app.py 10 20 30 40
```

Result:

```python
args.numbers
```

```text
[10, 20, 30, 40]
```

---

# Positional vs Optional Arguments

| Positional | Optional |
|------------|----------|
| `"name"` | `"--age"` |
| No `--` | Uses `--` |
| Usually required | Usually optional |
| Position matters | Position generally doesn't matter |

Example:

```bash
python app.py Akhil --age 19
```

```text
Akhil    → positional
--age 19 → optional
```

---

# Complete Example

```python
import argparse
parser = argparse.ArgumentParser(
    description="Student Information"
)
parser.add_argument(
    "name",
    help="Student name"
)
parser.add_argument(
    "--age",
    type=int,
    help="Student age"
)
parser.add_argument(
    "--department",
    choices=["CSE", "ECE", "ME"]
)
parser.add_argument(
    "--country",
    default="India"
)
parser.add_argument(
    "--verbose",
    action="store_true"
)
args = parser.parse_args()
print("Name:", args.name)
print("Age:", args.age)
print("Department:", args.department)
print("Country:", args.country)
if args.verbose:
    print("Verbose mode enabled")
```

Run:
```bash
python app.py Akhil --age 19 --department CSE --verbose
```

---

# How argparse Works

```text
Terminal Command
      ↓
ArgumentParser()
      ↓
add_argument()
      ↓
Defines accepted inputs
      ↓
parse_args()
      ↓
Reads the inputs
      ↓
args
      ↓
args.name
args.age
args.department
```

---

# Best Practices

- Use meaningful argument names.
- Add `help` descriptions.
- Use `type` for data validation.
- Use `choices` when only specific values are valid.
- Use `default` for sensible fallback values.
- Use flags such as `--verbose` for Boolean options.
- Keep CLI commands simple and understandable.

---

# Common Mistakes

❌ Forgetting `parse_args()`:

```python
parser.add_argument("name")
```

You still need:

```python
args = parser.parse_args()
```

---

❌ Forgetting `--` for optional arguments:

```bash
python app.py age 19
```

Correct:

```bash
python app.py --age 19
```

---

❌ Forgetting `type=int`:

```python
parser.add_argument("--age")
```

`age` will be stored as a string.

Use:

```python
parser.add_argument(
    "--age",
    type=int
)
```

---

❌ Providing invalid `choices`:

```python
choices=["CSE", "ECE"]
```

Then:

```bash
python app.py --department ME
```

will produce an error.

---

# Memory Trick

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

Fallback Value

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

True / False Flag

nargs
↓

Number of Values
```

---

# Quick Revision

| Need | Use |
|------|-----|
| Create parser | `ArgumentParser()` |
| Add argument | `add_argument()` |
| Read arguments | `parse_args()` |
| Positional argument | `"name"` |
| Optional argument | `"--name"` |
| Set data type | `type=int` |
| Default value | `default=value` |
| Make optional argument required | `required=True` |
| Restrict values | `choices=[...]` |
| Help description | `help="..."` |
| Boolean flag | `action="store_true"` |
| Zero or one value | `nargs="?"` |
| Zero or more values | `nargs="*"` |
| One or more values | `nargs="+"` |

---

# Interview Tip

**What is the difference between positional and optional arguments in `argparse`?**

**Answer:**

A positional argument is identified by its position and is usually required.

```bash
python app.py Akhil
```

An optional argument uses a flag such as `--age` and is usually optional.

```bash
python app.py Akhil --age 19
```