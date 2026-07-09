# OS Module

## Introduction

The `os` module is a built-in Python library that provides functions to interact with the operating system. It allows you to work with files, directories, environment variables, and system-level operations.

Whether you're automating tasks, managing files, or building command-line tools, the `os` module is an essential part of Python development.

---

## Why Learn This Library?

The `os` module is widely used in:

- Automation Scripts
- File Management Systems
- Backup Tools
- DevOps Scripts
- Data Engineering
- System Administration
- CLI Applications

---

## Features

- Work with files and folders
- Get and change directories
- Create and delete folders
- Rename files and folders
- Check file and folder existence
- Access environment variables
- Build platform-independent applications

---

## Installation

The `os` module is built into Python.

No installation is required.

---

## Import

```python
import os
```

---

## Important Functions

- os.getcwd()
- os.chdir()
- os.listdir()
- os.mkdir()
- os.makedirs()
- os.rename()
- os.remove()
- os.rmdir()
- os.removedirs()
- os.path.exists()
- os.path.isfile()
- os.path.isdir()
- os.path.join()
- os.environ

---

## Real-world Applications

- File Managers
- Backup Software
- Automation Scripts
- Log Management
- Build Systems
- DevOps Tools
- Data Processing Pipelines

---

## Advantages

- Built into Python
- Platform-independent
- Easy file and directory management
- Supports automation tasks

---

## Limitations

- Path handling can become complex (consider `pathlib` for modern code).
- Some functions behave differently across operating systems.

---

## Related Modules

- `pathlib` → Modern path handling
- `shutil` → Copy, move, and archive files
- `glob` → Find files using patterns

---

## Best Practices

- Use `os.path.join()` instead of manually joining paths.
- Check whether a file or directory exists before deleting it.
- Handle file operations with proper error handling.
- Prefer `pathlib` for new projects when appropriate.

---

## Common Mistakes

- Hardcoding file paths.
- Deleting files without checking their existence.
- Using `/` or `\` directly instead of `os.path.join()`.
- Forgetting to handle exceptions during file operations.

---

## Mini Project

### File Manager CLI

Features:

- View Current Directory
- List Files & Folders
- Create Folder
- Rename File/Folder
- Delete File
- Delete Folder
- Check Path Exists

---

## References

Official Python Documentation

https://docs.python.org/3/library/os.html