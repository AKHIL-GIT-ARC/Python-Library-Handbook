# Pathlib Module Interview Questions

## Beginner Level

### 1. What is the `pathlib` module?

**Answer:**
The `pathlib` module is a built-in Python library that provides an object-oriented way to work with file and directory paths. It is the modern replacement for many `os.path` operations.

---

### 2. How do you import `pathlib`?

```python
from pathlib import Path
```

---

### 3. How do you create a Path object?

**Answer**

```python
from pathlib import Path

path = Path("notes.txt")
```

---

### 4. How do you get the current working directory?

**Answer**

```python
Path.cwd()
```

---

### 5. How do you get the user's home directory?

**Answer**

```python
Path.home()
```

---

## Intermediate Level

### 6. How do you check whether a path exists?

**Answer**

```python
path.exists()
```

---

### 7. Difference between `is_file()` and `is_dir()`?

| `is_file()` | `is_dir()` |
|--------------|------------|
| Checks whether the path is a file | Checks whether the path is a directory |

---

### 8. How do you create a directory?

**Answer**

```python
Path("Projects").mkdir()
```

---

### 9. How do you rename a file or folder?

**Answer**

```python
old_path.rename(new_path)
```

---

### 10. How do you delete a file?

**Answer**

```python
path.unlink()
```

---

## Advanced Level

### 11. Difference between `glob()` and `rglob()`?

| `glob()` | `rglob()` |
|-----------|------------|
| Searches only the current directory | Searches current directory and all subdirectories |

---

### 12. What does `iterdir()` do?

**Answer**

It iterates through all files and folders inside a directory.

```python
for item in Path("folder").iterdir():
    print(item.name)
```

---

### 13. What is the difference between `name`, `stem`, and `suffix`?

| Property | Example Output |
|-----------|----------------|
| `name` | `notes.txt` |
| `stem` | `notes` |
| `suffix` | `.txt` |

---

### 14. What does `touch()` do?

**Answer**

Creates an empty file if it does not already exist.

```python
Path("notes.txt").touch()
```

---

### 15. What information does `stat()` provide?

**Answer**

Returns file metadata such as:
- File size
- Last modified time
- Permissions
- Creation time (platform dependent)

---

## Pathlib vs OS

### 16. Why is `pathlib` preferred over `os.path`?

**Answer**

- Object-oriented
- Cleaner syntax
- More readable
- Easier path manipulation
- Recommended for modern Python

---

### 17. Replace this `os` code with `pathlib`.

```python
os.path.exists(path)
```

**Answer**

```python
Path(path).exists()
```

---

### 18. Replace this code.

```python
os.listdir()
```

**Answer**

```python
Path.cwd().iterdir()
```

---

### 19. Replace this code.

```python
os.remove("notes.txt")
```

**Answer**

```python
Path("notes.txt").unlink()
```

---

### 20. Replace this code.

```python
os.mkdir("Projects")
```

**Answer**

```python
Path("Projects").mkdir()
```

---

## Scenario-Based Questions

### 21. You need to search for all Python files inside a project, including subfolders. Which method will you use?

**Answer**

```python
Path("project").rglob("*.py")
```

---

### 22. You need to display only the filename without its extension. Which property will you use?

**Answer**

```python
path.stem
```

---

### 23. Which method would you use to create an empty file?

**Answer**

```python
touch()
```
---

### 25. When should you choose `pathlib` instead of `os.path`?

**Answer**

Use `pathlib` for modern Python projects because it provides cleaner, object-oriented, and cross-platform path handling.

---

# Common Coding Questions

### 26. Create a folder if it doesn't exist.

**Hint**

```python
Path.exists()
Path.mkdir()
```

---

### 27. Print all `.txt` files in a directory.

**Hint**

```python
Path.glob("*.txt")
```

---

### 28. Recursively search all `.py` files.

**Hint**

```python
Path.rglob("*.py")
```
---

### 29. Print the file name, extension, and parent directory.

**Hint**

```python
path.name
path.stem
path.suffix
path.parent
```

---

### 30. Display the size of a file.

**Hint**

```python
path.stat().st_size
```

---

# Quick Revision

| Method | Purpose |
|---------|---------|
| `Path()` | Create path object |
| `cwd()` | Current directory |
| `home()` | Home directory |
| `exists()` | Check existence |
| `is_file()` | Check file |
| `is_dir()` | Check directory |
| `mkdir()` | Create folder |
| `rename()` | Rename |
| `unlink()` | Delete file |
| `rmdir()` | Delete folder |
| `iterdir()` | List directory |
| `glob()` | Search files |
| `rglob()` | Recursive search |
| `touch()` | Create empty file |
| `stat()` | File metadata |