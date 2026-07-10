# Pathlib Module

## Introduction

The `pathlib` module is a built-in Python library that provides an object-oriented way to work with file system paths. It simplifies file and directory operations, making code cleaner, more readable, and platform-independent.

Introduced in **Python 3.4**, `pathlib` is the recommended approach for path manipulation in modern Python.

---

## Why Learn This Library?

The `pathlib` module is widely used in:

- Python Automation
- Web Development
- Data Science
- AI & Machine Learning
- DevOps
- File Management Systems
- CLI Applications

---

## Features

- Object-oriented path handling
- Create and manage files & folders
- Read and write files
- Search files using patterns
- Cross-platform path support
- Easy path manipulation

---

## Installation

The `pathlib` module is built into Python.

No installation is required.

---

## Import

```python
from pathlib import Path
```

---

## Important Methods

- Path()
- cwd()
- home()
- exists()
- is_file()
- is_dir()
- mkdir()
- rename()
- unlink()
- rmdir()
- iterdir()
- glob()
- rglob()
- name
- stem
- suffix
- parent

---

## Migration from os

| os | pathlib |
|----|----------|
| `os.getcwd()` | `Path.cwd()` |
| `os.path.exists()` | `Path.exists()` |
| `os.path.isfile()` | `Path.is_file()` |
| `os.path.isdir()` | `Path.is_dir()` |
| `os.mkdir()` | `Path.mkdir()` |
| `os.remove()` | `Path.unlink()` |
| `os.rmdir()` | `Path.rmdir()` |
| `os.listdir()` | `Path.iterdir()` |
| `os.rename()` | `Path.rename()` |

---

## Real-world Applications

- File Explorers
- Backup Utilities
- Automation Scripts
- Log Management
- Data Processing
- Project Generators
- Configuration Management

---

## Advantages

- Clean and readable syntax
- Object-oriented design
- Platform-independent
- Easier than `os.path`
- Recommended for modern Python

---

## Limitations

- Available only in Python 3.4+
- Some advanced OS operations still require the `os` module

---

## Related Modules

- `os` → Operating system interaction
- `shutil` → Copy and move files
- `glob` → Pattern-based file searching

---

## Best Practices

- Prefer `pathlib` over `os.path` in new projects.
- Use `/` operator instead of manually joining paths.
- Check `exists()` before deleting files.
- Use `Path` objects instead of strings whenever possible.

---

## Common Mistakes

- Mixing `Path` objects with string paths.
- Forgetting to check file existence before deleting.
- Using `os.path` when `pathlib` provides a cleaner solution.

---

## Mini Project

### Modern File Explorer

Features:

- View Current Directory
- View Home Directory
- List Files & Folders
- Create Folder
- Rename File/Folder
- Delete File
- Delete Folder
- Search Files
- Display File Information

---

## References

Official Python Documentation

https://docs.python.org/3/library/pathlib.html