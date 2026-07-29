# File Basics Interview Questions

## Beginner Level

### 1. What is file handling in Python?

**Answer:**

File handling is the process of creating, opening, reading, writing, and managing files using Python.
Files allow programs to store data permanently so it can be accessed later.

---

### 2. Why do we need files?

**Answer:**

Variables store data temporarily while a program is running.
```python
name = "Akhil"
```

When the program ends, the variable disappears.
A file can store the information permanently:

```text
student.txt
↓
Name: Akhil
```

---

### 3. Which function is used to open a file in Python?

**Answer:**

The built-in `open()` function.

```python
file = open("notes.txt", "r")
```

Syntax:

```python
open(filename, mode)
```

---

### 4. What does `open()` return?

**Answer:**

`open()` returns a **file object**.

```python
file = open("notes.txt", "r")
```

The file object can then be used for operations such as:
```python
file.read()
file.write()
file.close()
```

---

### 5. What are file modes?

**Answer:**

File modes specify how a file should be opened.

| Mode | Purpose |
|---|---|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `x` | Create |
| `t` | Text |
| `b` | Binary |
| `+` | Read and write |

---

### 6. What is `r` mode?

**Answer:**

`r` opens a file for reading.

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

The file must already exist.

Otherwise:
```text
FileNotFoundError
```

---

### 7. What is `w` mode?

**Answer:**

`w` opens a file for writing.

```python
with open("notes.txt", "w") as file:
    file.write("Hello")
```

If the file doesn't exist, it is created.
If it already exists, its previous content is cleared.

---

### 8. What is `a` mode?

**Answer:**

`a` opens a file for appending.

```python
with open("notes.txt", "a") as file:
    file.write("\nPython")
```

New data is added to the end of the file without removing existing content.

---

### 9. What is `x` mode?

**Answer:**

`x` is used for exclusive file creation.

```python
with open("notes.txt", "x") as file:
    file.write("Hello")
```

If the file already exists, Python raises:

```text
FileExistsError
```

---

### 10. What is the difference between `w` and `a`?

**Answer:**

`w` can remove existing content, while `a` preserves it and adds new data at the end.

```text
w → Write / Overwrite
a → Append
```

---

## Intermediate Level

### 11. How do you read the contents of a file?

**Answer:**

Use `read()`.

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()

print(content)
```

---

### 12. How do you write data to a file?

**Answer:**

Open the file in a writing mode and use `write()`.

```python
with open(
    "notes.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Learning Python")
```

---

### 13. Why should a file be closed?

**Answer:**

Closing a file releases its associated system resources and ensures file operations are properly finalized.

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```

---

### 14. What is `with open()`?

**Answer:**

`with open()` uses a **context manager** to manage the file.

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

When execution leaves the `with` block, Python closes the file automatically.

---

### 15. Why is `with open()` preferred?

**Answer:**

It handles cleanup automatically.

Instead of:

```python
file = open("notes.txt", "r")
content = file.read()
file.close()
```

we can use:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

This is safer because the context manager closes the file even if an exception occurs inside the block.

---

### 16. What does `file.closed` do?

**Answer:**

It tells us whether the file is currently closed.

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

### 17. What does `file.name` return?

**Answer:**

It returns the name or path associated with the file object.

```python
with open("notes.txt", "r") as file:
    print(file.name)
```

Possible output:

```text
notes.txt
```

---

### 18. What does `file.mode` return?

**Answer:**

It tells us which mode was used to open the file.

```python
with open("notes.txt", "r") as file:
    print(file.mode)
```

Output:

```text
r
```

---

### 19. What is text mode?

**Answer:**

Text mode is used when working with textual data.

```python
open("notes.txt", "rt")
```

`t` means text mode.

It is the default, so:
```python
open("notes.txt", "r")
```

is equivalent to:
```python
open("notes.txt", "rt")
```

---

### 20. What is binary mode?

**Answer:**

Binary mode works with data as bytes rather than strings.

```python
with open("photo.jpg", "rb") as file:
    data = file.read()
```

`rb` means:
```text
r → Read
b → Binary
```

Binary mode is commonly used for files such as images, audio, and other non-text data.

---

## Advanced Level

### 21. What is the difference between text mode and binary mode?

**Answer:**

Text mode works with `str` and performs text encoding/decoding.
Binary mode works directly with `bytes`.

```python
open("notes.txt", "r")
```

works with text.

```python
open("photo.jpg", "rb")
```

works with bytes.

---

### 22. What is file encoding?

**Answer:**

Encoding defines how text characters are represented as bytes.

Example:

```python
with open(
    "notes.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
```

`UTF-8` is a widely used Unicode encoding.

---

### 23. What is a relative file path?

**Answer:**

A relative path is interpreted relative to the program's current working directory.

```python
open("notes.txt", "r")
```

or:

```python
open("data/students.txt", "r")
```

---

### 24. What is an absolute file path?

**Answer:**

An absolute path specifies the complete location of a file.

Example on Windows:

```python
path = r"C:\Users\User\Documents\notes.txt"
```

---

### 25. What is the current working directory?

**Answer:**

The current working directory is the directory Python uses as the starting point for resolving relative paths.

It can be checked using:

```python
import os
print(os.getcwd())
```

The current working directory does not necessarily have to be the directory containing the Python script.

---

### 26. What happens if you open a nonexistent file using `r`?

**Answer:**

Python raises:

```text
FileNotFoundError
```

Example:

```python
with open("missing.txt", "r") as file:
    content = file.read()
```

---

### 27. What happens if you use `x` on an existing file?

**Answer:**

Python raises:

```text
FileExistsError
```

because `x` is designed to create a new file without overwriting an existing one.

---

### 28. What is `PermissionError`?

**Answer:**

`PermissionError` occurs when the program does not have sufficient permission to perform the requested file operation.

For example, a program may try to write to a protected location without write permission.

---

## Scenario-Based Questions

### 29. You want to read an existing text file. Which mode should you use?

**Answer:**

Use:

```python
"r"
```

Example:

```python
with open("data.txt", "r") as file:
    content = file.read()
```

---

### 30. You want to replace the contents of a file. Which mode should you use?

**Answer:**

Use:

```python
"w"
```

Example:

```python
with open("data.txt", "w") as file:
    file.write("New content")
```

Be careful because existing content is cleared.

---

### 31. You want to add data without deleting existing content. Which mode should you use?

**Answer:**

Use:

```python
"a"
```

Example:

```python
with open("data.txt", "a") as file:
    file.write("\nNew data")
```

---

### 32. You want to create a file only if it doesn't already exist. Which mode should you use?

**Answer:**

Use:

```python
"x"
```

This prevents accidental overwriting.

---

### 33. You want to read an image file. Which mode should you use?

**Answer:**

Use binary read mode:

```python
"rb"
```

Example:

```python
with open("photo.jpg", "rb") as file:
    data = file.read()
```

---

### 34. A file is not being found even though it exists. What should you check?

**Answer:**

Check the current working directory:

```python
import os
print(os.getcwd())
```

A relative path is resolved from the current working directory, so the program may be looking in a different location than expected.

---

## Coding Questions

### 35. Write a program to create a text file and store a message.

**Answer:**

```python
with open(
    "message.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("Hello Python")
```

---

### 36. Write a program to read and print a text file.

**Answer:**

```python
with open(
    "message.txt",
    "r",
    encoding="utf-8"
) as file:
    content = file.read()
print(content)
```

---

### 37. Write a program to append a new line to a file.

**Answer:**

```python
with open(
    "message.txt",
    "a",
    encoding="utf-8"
) as file:
    file.write("\nLearning File Handling")
```

---

### 38. Handle a missing file without crashing the program.

**Answer:**

```python
try:
    with open(
        "missing.txt",
        "r",
        encoding="utf-8"
    ) as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

### 39. Write a student record to a file.

**Answer:**

```python
name = "Akhil"
roll_no = 101
marks = 90
with open(
    "student.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll_no}\n")
    file.write(f"Marks: {marks}\n")
```

---

### 40. How can you check whether a file was automatically closed after a `with` block?

**Answer:**

```python
with open("notes.txt", "r") as file:
    print(file.closed)
print(file.closed)
```

Output:

```text
False
True
```

Inside the block the file is open.

After leaving the block it is closed.

---

# Quick Interview Comparison

| Question | Answer |
|---|---|
| Open a file? | `open()` |
| Read existing file? | `r` |
| Write/overwrite? | `w` |
| Append? | `a` |
| Create only if absent? | `x` |
| Text mode? | `t` |
| Binary mode? | `b` |
| Read contents? | `read()` |
| Write contents? | `write()` |
| Close manually? | `close()` |
| Automatic cleanup? | `with open()` |
| Missing file in `r`? | `FileNotFoundError` |
| Existing file in `x`? | `FileExistsError` |
| Check closed? | `file.closed` |
| File name/path? | `file.name` |
| Opening mode? | `file.mode` |

---

# Common Interview Traps

### Does `w` only write to an existing file?

No.

It creates the file if necessary, but if the file already exists, its existing contents are truncated.

---

### Does `a` overwrite existing data?

No. It preserves existing content and writes at the end.

---

### Does `r` create a missing file?

No.

It raises:

```text
FileNotFoundError
```

---

### Is `file.close()` required with `with open()`?

No.

The context manager handles closing automatically.

---

### Are relative paths always relative to the Python script?

No.

They are resolved relative to the **current working directory**.

---

# Memory Map

```text
File Handling
      │
      ├── open()
      │
      ├── r → Read
      ├── w → Write / Overwrite
      ├── a → Append
      ├── x → Create New
      │
      ├── t → Text
      ├── b → Binary
      │
      ├── read()  → Retrieve
      ├── write() → Store
      ├── close() → Close
      │
      └── with open()
              ↓
        Automatic Cleanup
```