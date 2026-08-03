# File Paths — Cheat Sheet

## Relative Path

Path based on the current working directory.

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

Example:

```text
Project/
│
├── main.py
└── notes.txt
```

---

## Absolute Path

Complete location of a file.

```python
path = r"C:\Users\Akhil\Documents\notes.txt"
with open(path, "r") as file:
    print(file.read())
```

---

## Current Working Directory

```python
import os
os.getcwd()
```

Returns the current working directory.

---

## Change Directory

```python
import os

os.chdir(r"C:\Users\Akhil\Documents")
```

Changes the current working directory.

---

## Check Path Exists

```python
import os

os.path.exists("notes.txt")
```

Returns:

```text
True / False
```

---

## Check File

```python
os.path.isfile("notes.txt")
```

Returns:

```text
True / False
```

---

## Check Folder

```python
os.path.isdir("sample_folder")
```

Returns:

```text
True / False
```

---

## Get Absolute Path

```python
os.path.abspath("notes.txt")
```

Returns the complete path.

---

## Get File Name

```python
os.path.basename(path)
```

Example:

```text
notes.txt
```

---

## Get Folder Path

```python
os.path.dirname(path)
```

Example:

```text
C:\Users\Akhil\Documents
```

---

## Relative vs Absolute Path

| Relative Path | Absolute Path |
|---------------|---------------|
| Based on current directory | Complete file location |
| Short | Full path |

---

## Quick Revision

```text
os.getcwd()          → Current directory
os.chdir()           → Change directory
os.path.exists()     → Path exists?
os.path.isfile()     → Is file?
os.path.isdir()      → Is folder?
os.path.abspath()    → Absolute path
os.path.basename()   → File name
os.path.dirname()    → Folder path
```

---

## Key Points

- Relative paths depend on the current working directory.
- Absolute paths specify the complete location.
- Use `os.getcwd()` to know where Python is running.
- Use `os.path.exists()` before opening a file.
- `os.path.isfile()` checks for files.
- `os.path.isdir()` checks for folders.