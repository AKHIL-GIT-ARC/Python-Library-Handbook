# File Paths in Python

A file path tells Python **where a file or folder is located**.
There are two types of file paths:
- Relative Path
- Absolute Path

---

## Relative Path

A relative path is based on the **current working directory**.

Example:

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

If `notes.txt` is in the same folder as your program, only the filename is needed.

Example:

```text
Project/
│
├── main.py
└── notes.txt
```

---

## Absolute Path

An absolute path gives the complete location of a file.
Windows Example:

```python
path = r"C:\Users\Akhil\Documents\notes.txt"
with open(path, "r") as file:
    print(file.read())
```

---

## Current Working Directory

The current working directory is the folder from which Python is running.

Get it using:

```python
import os
print(os.getcwd())
```

Example Output:

```text
C:\Projects\Python
```

---

## Change Working Directory

Use `os.chdir()`.

```python
import os
os.chdir("C:\\Projects")
```

Check the new location:

```python
print(os.getcwd())
```

---

## Check if a Path Exists

Use `os.path.exists()`.

```python
import os
print(os.path.exists("notes.txt"))
```

Output:

```text
True
```

---

## Check if it is a File

Use `os.path.isfile()`.

```python
import os
print(os.path.isfile("notes.txt"))
```

Output:

```text
True
```

---

## Check if it is a Directory

Use `os.path.isdir()`.

```python
import os
print(os.path.isdir("data"))
```

Output:

```text
True
```

---

## Relative vs Absolute Path

| Relative Path | Absolute Path |
|---------------|---------------|
| Depends on current working directory | Complete file location |
| Short | Full path |
| Easy inside a project | Useful outside the project |

---

## Key Points

- Relative paths are based on the current working directory.
- Absolute paths specify the complete location.
- `os.getcwd()` returns the current working directory.
- `os.chdir()` changes the working directory.
- `os.path.exists()` checks whether a path exists.
- `os.path.isfile()` checks for a file.
- `os.path.isdir()` checks for a directory.

---

## Quick Revision

| Function | Purpose |
|----------|---------|
| `os.getcwd()` | Current working directory |
| `os.chdir()` | Change working directory |
| `os.path.exists()` | Path exists? |
| `os.path.isfile()` | Is it a file? |
| `os.path.isdir()` | Is it a directory? |
| Relative Path | Current folder based |
| Absolute Path | Complete path |