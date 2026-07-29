# File Basics in Python

File handling allows a Python program to **store data permanently** and retrieve it later.
Variables exist only while a program is running, but files allow data to remain available even after the program stops.

---

# Why File Handling?

Consider:

```python
name = "Akhil"
marks = 90
```

These values exist in memory while the program runs.
When the program ends, those variables disappear.
If we save the data to a file:
```text
student.txt

Akhil
90
```
the information remains stored and can be accessed later.
Think:
```text
Variable
↓
Temporary storage
↓
Lost when program ends

File
↓
Permanent storage
↓
Available later
```

---

# What is a File?

A file is a collection of data stored on a storage device.
Examples:
```text
notes.txt
students.csv
config.json
photo.jpg
report.pdf
database.db
```

Files can contain:
- Text
- Numbers
- Images
- Audio
- Video
- Structured data
- Binary data

---

# Basic File Handling Process

Most file operations follow this pattern:
```text
Open File
    ↓
Read / Write Data
    ↓
Close File
```

Example:

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

---

# open()

Python provides the built-in `open()` function for working with files.
Basic syntax:

```python
open(filename, mode)
```

Example:

```python
file = open("notes.txt", "r")
```

Here:

```text
"notes.txt" → File name
"r"         → File mode
file        → File object
```

---

# File Object

When we use:

```python
file = open("notes.txt", "r")
```

Python returns a **file object**.
The file object allows us to perform operations such as:
```python
file.read()
file.readline()
file.write()
file.close()
```

Think:

```text
notes.txt
   ↓
open()
   ↓
File Object
   ↓
Read / Write / Close
```

---

# File Modes

The mode tells Python **how we want to open the file**.
| Mode | Meaning |
|---|---|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `x` | Create |
| `t` | Text mode |
| `b` | Binary mode |
| `+` | Read and write |

Example:

```python
file = open("notes.txt", "r")
```
opens the file for reading.

---

# Read Mode — r

`r` opens an existing file for reading.

```python
file = open("notes.txt", "r")
```
Then:

```python
content = file.read()
print(content)
```

Important:

If the file does not exist, Python raises:

```text
FileNotFoundError
```

---

# Write Mode — w

`w` opens a file for writing.

```python
file = open("notes.txt", "w")
```

Write data:

```python
file.write("Hello Python")
```

If the file does not exist:

```text
Python creates it.
```

If the file already exists:

```text
Its existing content is cleared.
```

So be careful with `w`.

---

# Append Mode — a

`a` adds data to the end of a file.

```python
file = open("notes.txt", "a")
```

Then:

```python
file.write("\nNew line")
```
Existing content remains unchanged.

Example:
Before:

```text
Python
Java
```

Append:
```python
file.write("\nC++")
```

After:
```text
Python
Java
C++
```

---

# Create Mode — x

`x` creates a new file.

```python
file = open("new_file.txt", "x")
```

If the file does not exist:

```text
File created successfully
```

If it already exists, Python raises:

```text
FileExistsError
```

---

# Reading a File

Suppose `notes.txt` contains:
```text
Python
Java
C++
```

We can read it using:
```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

Output:
```text
Python
Java
C++
```

---

# Writing to a File

```python
file = open("notes.txt", "w")
file.write("Learning Python")
file.close()
```

The file now contains:
```text
Learning Python
```

---

# Appending to a File

```python
file = open("notes.txt", "a")
file.write("\nFile Handling")
file.close()
```

Now:
```text
Learning Python
File Handling
```

---

# Closing a File

After working with a file, it should be closed.
```python
file.close()
```
Why?

Closing a file:
- Releases system resources
- Ensures buffered data is properly handled
- Prevents unnecessary open file handles

Example:

```python
file = open("notes.txt", "r")
print(file.read())
file.close()
```

---

# with open()

The preferred way to work with files is usually a context manager:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```
Python automatically closes the file when execution leaves the `with` block.

So we don't need:
```python
file.close()
```

---

# Normal open() vs with open()

## Normal

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```
You are responsible for closing the file.

## Using with

```python
with open("notes.txt", "r") as file:
    content = file.read()
```
Python handles closing automatically.

Prefer:
```python
with open(...)
```
for most file-handling tasks.

---

# Text Mode

Text files are opened in text mode by default.

```python
open("notes.txt", "r")
```
is equivalent to:
```python
open("notes.txt", "rt")
```

Here:
```text
r → Read
t → Text
```

---

# Binary Mode

Binary mode is used for binary data such as images or other non-text files.
Example:

```python
with open("photo.jpg", "rb") as file:
    data = file.read()
```

Here:
```text
r → Read
b → Binary
```

The result is bytes rather than normal text.
We'll study binary files in detail later.

---

# File Paths

Python needs to know where a file is located.
There are two common types of paths:
```text
Relative Path
Absolute Path
```
---

# Relative Path

A relative path is interpreted relative to the program's **current working directory**.

Example:
```python
open("notes.txt", "r")
```

Or:
```python
open("data/students.txt", "r")
```

The second example refers to:
```text
data/
└── students.txt
```
relative to the current working directory.

---

# Absolute Path

An absolute path describes the full location of a file.

Example on Windows:

```text
C:\Users\User\Documents\notes.txt
```

In Python, a raw string can make Windows paths easier to write:

```python
path = r"C:\Users\User\Documents\notes.txt"

with open(path, "r") as file:
    print(file.read())
```

---

# Current Working Directory

Relative paths are resolved from the **current working directory**, which is not always the same as the folder containing the Python script.

You can check it using:
```python
import os
print(os.getcwd())
```

Example output:
```text
C:\Projects\Python
```
This is important when troubleshooting:

```text
FileNotFoundError
```

---

# Checking Whether a File is Closed

A file object has a `closed` attribute.

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

---

# Basic File Information

A file object also provides information such as:
```python
file.name
file.mode
file.closed
```

Example:
```python
file = open("notes.txt", "r")
print(file.name)
print(file.mode)
print(file.closed)
file.close()
```

Possible output:
```text
notes.txt
r
False
```

---

# Common File Errors

## FileNotFoundError

```python
open("missing.txt", "r")
```
If the file doesn't exist:
```text
FileNotFoundError
```

---

## FileExistsError

```python
open("notes.txt", "x")
```

If `notes.txt` already exists:
```text
FileExistsError
```

---

## PermissionError

A program may fail if it does not have permission to access a file.

```text
PermissionError
```
We'll cover safe exception handling in a later module.

---

# Real-World Applications

File handling is used for:
- Saving user data
- Reading configuration files
- Processing datasets
- Creating reports
- Logging application events
- Reading CSV files
- Working with JSON
- Handling uploaded files
- Storing application output
- Processing documents

---

# Example — Student Record

```python
name = "Akhil"
marks = 90
with open("student.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}")
```

The resulting file:
```text
Name: Akhil
Marks: 90
```

Read it:
```python
with open("student.txt", "r") as file:
    print(file.read())
```

---

# File Handling Flow

```text
Choose File
    ↓
Choose Mode
    ↓
open()
    ↓
File Object
    ↓
Read / Write
    ↓
Close File
```

Using a context manager:

```text
with open(...)
      ↓
Perform Operations
      ↓
Leave with Block
      ↓
File Closed Automatically
```

---

# Best Practices

- Prefer `with open()` for normal file operations.
- Choose the correct file mode.
- Be careful when using `w` because it truncates existing content.
- Use `a` when existing content must remain.
- Use explicit encodings such as `encoding="utf-8"` for text files when appropriate.
- Use clear and meaningful file names.
- Understand what directory relative paths are resolved from.
- Handle expected file errors when building real applications.

---

# Common Mistakes

## Forgetting to Close a File

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

## Accidentally Overwriting Data

This:

```python
open("notes.txt", "w")
```

truncates an existing file when it is opened successfully.
Use `a` if you want to add data without removing the existing content.

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

## Confusing Relative Paths

If Python cannot find:

```python
open("data.txt", "r")
```

check:

```python
import os

print(os.getcwd())
```

The relative path is based on the current working directory.

---

# Learning Outcomes

After completing this module, you'll understand:

- What file handling is
- Why files are used
- How `open()` works
- What a file object is
- Basic file modes
- Reading files
- Writing files
- Appending data
- Creating files
- Closing files
- `with open()`
- Relative and absolute paths
- Basic file-related errors

---

# Quick Revision

| Need | Use |
|---|---|
| Open file | `open()` |
| Read | `"r"` |
| Write | `"w"` |
| Append | `"a"` |
| Create new | `"x"` |
| Text mode | `"t"` |
| Binary mode | `"b"` |
| Close file | `file.close()` |
| Read content | `file.read()` |
| Write content | `file.write()` |
| Automatic closing | `with open()` |
| File name | `file.name` |
| File mode | `file.mode` |
| Check closed | `file.closed` |

---