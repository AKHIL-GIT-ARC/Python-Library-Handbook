# OS Module Interview Questions

## Beginner Level

### 1. What is the `os` module?

**Answer:**  
The `os` module is a built-in Python library used to interact with the operating system. It provides functions for working with files, directories, environment variables, and system paths.

---

### 2. How do you import the `os` module?

```python
import os
```

---

### 3. How do you get the current working directory?

**Answer**

```python
os.getcwd()
```

---

### 4. Which function changes the current working directory?

**Answer**

```python
os.chdir(path)
```

---

### 5. Which function lists all files and folders in a directory?

**Answer**

```python
os.listdir()
```

---

## Intermediate Level

### 6. Difference between `mkdir()` and `makedirs()`?

| `mkdir()` | `makedirs()` |
|------------|--------------|
| Creates one directory | Creates multiple nested directories |

---

### 7. Difference between `remove()` and `rmdir()`?

| `remove()` | `rmdir()` |
|-------------|-----------|
| Deletes a file | Deletes an empty directory |

---

### 8. What does `os.path.exists()` do?

**Answer**

Checks whether a file or directory exists.

```python
os.path.exists(path)
```

---

### 9. Difference between `isfile()` and `isdir()`?

| `isfile()` | `isdir()` |
|-------------|-----------|
| Checks if the path is a file | Checks if the path is a directory |

---

### 10. Why should you use `os.path.join()`?

**Answer**

It joins file paths safely and works across different operating systems.

Example:

```python
os.path.join("Documents", "notes.txt")
```

---

## Advanced Level

### 11. What is `os.environ`?

**Answer**

It provides access to environment variables.

Example:

```python
os.environ.get("USERNAME")
```

---

### 12. Why is `pathlib` preferred over `os.path` in modern Python?

**Answer**

`pathlib` provides an object-oriented, cleaner, and more readable way to work with file paths.

---

### 13. What happens if you call `os.remove()` on a folder?

**Answer**

A `IsADirectoryError` (or similar OS-specific exception) is raised because `os.remove()` only deletes files.

---

### 14. What happens if you call `os.rmdir()` on a non-empty folder?

**Answer**

Python raises an `OSError` because `os.rmdir()` only removes empty directories.

---

### 15. Why should file operations be wrapped in `try-except` blocks?

**Answer**

To handle errors such as:
- File not found
- Permission denied
- Invalid path
- File already exists

---

## Scenario-Based Questions

### 16. You need to create a folder only if it doesn't already exist. Which functions will you use?

**Answer**

```python
if not os.path.exists(folder):
    os.mkdir(folder)
```

---

### 17. You need to check whether a path points to a file or a folder. Which functions will you use?

**Answer**

```python
os.path.isfile(path)
os.path.isdir(path)
```

---

### 18. You are building a file manager. Which `os` functions are commonly used?

**Answer**

- `getcwd()`
- `listdir()`
- `mkdir()`
- `rename()`
- `remove()`
- `rmdir()`
- `path.exists()`

---

### 19. Which function is best for creating nested folders?

**Answer**

```python
os.makedirs()
```
---

# Common Coding Questions

### 21. Write a program to list all files in a directory.

**Hint**

```python
os.listdir()
```
---

### 22. Write a program to create a folder if it doesn't exist.

**Hint**

```python
os.path.exists()
os.mkdir()
```
---

### 23. Write a program to rename a file.

**Hint**

```python
os.rename()
```

---

### 24. Write a program to check whether a path is a file or a directory.

**Hint**

```python
os.path.isfile()
os.path.isdir()
```

---

### 25. Write a program to delete an empty directory.

**Hint**

```python
os.rmdir()
```

---

# Quick Revision

| Function | Purpose |
|----------|---------|
| `getcwd()` | Current working directory |
| `chdir()` | Change directory |
| `listdir()` | List files and folders |
| `mkdir()` | Create a folder |
| `makedirs()` | Create nested folders |
| `rename()` | Rename a file/folder |
| `remove()` | Delete a file |
| `rmdir()` | Delete an empty folder |
| `exists()` | Check path exists |
| `isfile()` | Check file |
| `isdir()` | Check directory |
| `join()` | Join file paths |
| `environ` | Environment variables |