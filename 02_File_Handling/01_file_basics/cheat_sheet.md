# File Basics Cheat Sheet

## What is File Handling?

File handling allows Python programs to store and retrieve data from files.

```text
Program
   ↓
Open File
   ↓
Read / Write
   ↓
Close File
```

Files provide persistent storage, unlike normal variables that disappear when the program ends.

---

# open()

Used to open a file.

```python
file = open("notes.txt", "r")
```

Syntax:

```python
open(filename, mode)
```

Example:

```python
file = open("data.txt", "r")
```

```text
"data.txt" → Filename
"r"        → Mode
file       → File object
```

---

# File Modes

| Mode | Purpose |
|---|---|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `x` | Create new file |
| `t` | Text mode |
| `b` | Binary mode |
| `+` | Reading and writing |

---

# Read Mode — r

Opens an existing file for reading.

```python
file = open("notes.txt", "r")
```

If the file doesn't exist:

```text
FileNotFoundError
```

Example:

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
```

Memory Tip:

```text
r → Read
```

---

# Write Mode — w

Opens a file for writing.

```python
with open(
    "notes.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Hello Python")
```

If the file doesn't exist:

```text
Creates it
```

If the file already exists:

```text
Existing content is cleared
```

Memory Tip:

```text
w → Write / Overwrite
```

---

# Append Mode — a

Adds data to the end of a file.

```python
with open(
    "notes.txt",
    "a",
    encoding="utf-8"
) as file:
    file.write("\nNew content")
```

Existing content remains.

```text
Before:

Python
Java

Append C++

After:

Python
Java
C++
```

Memory Tip:

```text
a → Add to End
```

---

# Create Mode — x

Creates a new file.

```python
with open(
    "notes.txt",
    "x",
    encoding="utf-8"
) as file:
    file.write("New file")
```

If the file already exists:

```text
FileExistsError
```

Memory Tip:

```text
x → Create Exclusively
```

---

# Reading a File

Use:

```python
file.read()
```

Example:

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()

print(content)
```

`read()` returns the file contents as a string in text mode.

---

# Writing to a File

Use:

```python
file.write()
```

Example:

```python
with open(
    "notes.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Learning Python")
```

Result:

```text
Learning Python
```

---

# Writing Multiple Lines

Use `\n` for a new line.

```python
with open(
    "languages.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Python\n")
    file.write("Java\n")
    file.write("C++\n")
```

Result:

```text
Python
Java
C++
```

---

# close()

Closes an opened file.

```python
file = open(
    "notes.txt",
    "r",
    encoding="utf-8"
)
content = file.read()
file.close()
```

Closing files releases the associated system resources.

---

# with open()

Preferred way to work with files.

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
```

The file is automatically closed when the `with` block ends.

Prefer:

```python
with open(...)
```

instead of manually managing:

```python
file = open(...)
file.close()
```

---

# File Object

`open()` returns a file object.

```python
file = open("notes.txt", "r")
```

Common operations:

```python
file.read()
file.write()
file.close()
```

Common properties:

```python
file.name
file.mode
file.closed
```

---

# file.name

Returns the file name/path associated with the file object.

```python
with open("notes.txt", "r") as file:
    print(file.name)
```

Possible output:

```text
notes.txt
```

---

# file.mode

Returns the mode used to open the file.

```python
with open("notes.txt", "r") as file:
    print(file.mode)
```

Output:

```text
r
```

---

# file.closed

Checks whether the file is closed.

```python
file = open("notes.txt", "r")
print(file.closed)
file.close()
print(file.closed)
```

Output:

```text
False
True
```

Remember:

```text
False → Open
True  → Closed
```

---

# Text Mode

Text mode works with strings.

```python
open("notes.txt", "rt")
```

`"t"` means text mode.
Text mode is the default, so:

```python
open("notes.txt", "r")
```

is equivalent to:

```python
open("notes.txt", "rt")
```

---

# Binary Mode

Binary mode works with bytes.

```python
with open("photo.jpg", "rb") as file:
    data = file.read()
```

```text
r → Read
b → Binary
```

Common binary modes:

```text
rb → Read binary
wb → Write binary
ab → Append binary
```

---

# Encoding

For text files, specifying an encoding is a good practice.

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
```

UTF-8 supports a wide range of Unicode characters.

```text
encoding="utf-8"
↓
How text is converted between strings and bytes
```

---

# Relative Path

A relative path is interpreted from the current working directory.

```python
open("notes.txt", "r")
```

Another example:

```python
open("data/students.txt", "r")
```

Structure:

```text
data/
└── students.txt
```

---

# Absolute Path

An absolute path gives the complete location.

Example on Windows:

```python
path = r"C:\Users\User\Documents\notes.txt"

with open(path, "r") as file:
    print(file.read())
```

---

# Current Working Directory

Check the current working directory using:

```python
import os
print(os.getcwd())
```

Relative paths are resolved from this directory.

---

# FileNotFoundError

Occurs when trying to read a file that doesn't exist.

```python
open("missing.txt", "r")
```

Handle it:

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

# FileExistsError

Can occur when `"x"` mode tries to create a file that already exists.

```python
try:
    with open("notes.txt", "x") as file:
        file.write("Hello")
except FileExistsError:
    print("File already exists.")
```

---

# PermissionError

Occurs when Python doesn't have the required permission to perform the requested file operation.

```text
PermissionError
```

Example situations include trying to write to a protected location or accessing a file without sufficient permissions.

---

# r vs w vs a vs x

| Mode | File must exist? | Creates file? | Existing data |
|---|---:|---:|---|
| `r` | Yes | No | Preserved |
| `w` | No | Yes | Cleared |
| `a` | No | Yes | Preserved |
| `x` | Must not exist | Yes | Never overwrites |

---

# open() vs with open()

## Manual

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```

## Context Manager

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

Prefer the context manager because file cleanup happens automatically even when execution leaves the block because of an exception.

---

# Basic Student Record

Write:

```python
name = "Akhil"
marks = 90
with open(
    "student.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}")
```

Result:

```text
Name: Akhil
Marks: 90
```

Read:

```python
with open(
    "student.txt",
    "r",
    encoding="utf-8"
) as file:
    print(file.read())
```

---

# Common Mistakes

## Using w When You Mean a

This:

```python
open("notes.txt", "w")
```
can erase existing content.

Use:

```python
open("notes.txt", "a")
```

when you want to preserve existing data and append new content.

---

## Forgetting to Close

Avoid:

```python
file = open("notes.txt", "r")
content = file.read()
```

Prefer:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

---

## Reading a Missing File

```python
open("missing.txt", "r")
```

raises:

```text
FileNotFoundError
```

---

## Incorrect Relative Path

If:

```python
open("notes.txt", "r")
```

cannot find the file, check:

```python
import os

print(os.getcwd())
```

---

# Best Practices

- Prefer `with open()`.
- Use `encoding="utf-8"` for text files when appropriate.
- Choose file modes carefully.
- Remember that `w` can erase existing content.
- Use `a` when adding to existing content.
- Use `x` when accidental overwriting must be prevented.
- Use `b` for binary data.
- Understand the current working directory when using relative paths.
- Handle expected file-related exceptions.

---

# Memory Map

```text
open()
  ↓
Open File

r
↓
Read

w
↓
Write / Overwrite

a
↓
Append

x
↓
Create New

t
↓
Text

b
↓
Binary

read()
↓
Retrieve Data

write()
↓
Store Data

close()
↓
Close File

with open()
↓
Automatic Cleanup
```

---

# Quick Revision

| Need | Use |
|---|---|
| Open file | `open()` |
| Read | `"r"` |
| Write | `"w"` |
| Append | `"a"` |
| Create new | `"x"` |
| Text | `"t"` |
| Binary | `"b"` |
| Read + write | `"+"` |
| Read content | `read()` |
| Write content | `write()` |
| Close manually | `close()` |
| Automatic closing | `with open()` |
| File name | `file.name` |
| File mode | `file.mode` |
| Check closed | `file.closed` |
| Text encoding | `encoding="utf-8"` |