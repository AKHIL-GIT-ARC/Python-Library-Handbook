# File Paths — Interview Questions

## 1. What is a file path?

A file path specifies the location of a file or folder.

Example:

```text
C:\Users\Akhil\Documents\notes.txt
```

---

## 2. What is the difference between a relative path and an absolute path?

| Relative Path | Absolute Path |
|---------------|---------------|
| Based on current working directory | Complete location of the file |
| Short | Full path |

---

## 3. What is the current working directory?

It is the directory from which Python is currently running.

```python
import os
print(os.getcwd())
```

---

## 4. How do you change the current working directory?

Use `os.chdir()`.

```python
import os
os.chdir(r"C:\Users\Akhil\Documents")
```

---

## 5. How do you check whether a file or folder exists?

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

## 6. What is `os.path.isfile()`?

It checks whether the given path is a file.

```python
print(os.path.isfile("notes.txt"))
```

Output:

```text
True
```

---

## 7. What is `os.path.isdir()`?

It checks whether the given path is a directory (folder).

```python
print(os.path.isdir("sample_folder"))
```

Output:

```text
True
```

---

## 8. What is `os.path.abspath()`?

It returns the complete (absolute) path of a file or folder.

```python
import os
print(os.path.abspath("notes.txt"))
```

---

## 9. What is `os.path.basename()`?

It returns only the file or folder name.

```python
path = r"C:\Users\Akhil\Documents\notes.txt"
print(os.path.basename(path))
```

Output:

```text
notes.txt
```

---

## 10. What is `os.path.dirname()`?

It returns the directory part of a path.

```python
path = r"C:\Users\Akhil\Documents\notes.txt"
print(os.path.dirname(path))
```

Output:

```text
C:\Users\Akhil\Documents
```

---

## Quick Revision

```text
Relative Path        → Current directory based
Absolute Path        → Complete path

os.getcwd()          → Current directory
os.chdir()           → Change directory
os.path.exists()     → Path exists?
os.path.isfile()     → Is file?
os.path.isdir()      → Is folder?
os.path.abspath()    → Absolute path
os.path.basename()   → File name
os.path.dirname()    → Folder path
```