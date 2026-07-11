# Shutil Module

## Introduction

The `shutil` module is a built-in Python library that provides high-level operations for working with files and directories. It simplifies tasks such as copying, moving, deleting directories, creating archives, and checking disk usage.

Unlike the `os` module, which offers low-level file operations, `shutil` provides convenient functions for common file management tasks.

---

## Why Learn This Library?

The `shutil` module is widely used in:
- Backup Systems
- File Managers
- Automation Scripts
- DevOps
- Deployment Tools
- Data Migration
- System Administration

---

## Features

- Copy files
- Copy directories
- Move files and folders
- Delete entire directory trees
- Create ZIP archives
- Extract archives
- Check disk usage
- Locate executables

---

## Installation

The `shutil` module is built into Python.

No installation is required.

---

## Import

```python
import shutil
```

---

## Important Functions

- shutil.copy()
- shutil.copy2()
- shutil.copytree()
- shutil.move()
- shutil.rmtree()
- shutil.disk_usage()
- shutil.make_archive()
- shutil.unpack_archive()
- shutil.which()

---

## Migration from Previous Modules

| Task | os/pathlib | shutil |
|------|------------|---------|
| Copy File | Manual file handling | `shutil.copy()` |
| Copy Folder | Multiple operations | `shutil.copytree()` |
| Move File | `os.rename()` (same drive) | `shutil.move()` |
| Delete Folder | `os.rmdir()` (empty only) | `shutil.rmtree()` |
| Create ZIP | Manual process | `shutil.make_archive()` |

---

## Real-world Applications

- Automatic Backups
- File Synchronization
- Deployment Scripts
- Project Archiving
- File Organization Tools
- Data Migration Utilities

---

## Advantages

- High-level API
- Easy to use
- Cross-platform
- Supports archives
- Reduces boilerplate code

---

## Limitations

- Cannot edit file contents
- Some operations permanently modify files
- Requires caution when deleting folders

---

## Related Modules

- `os` → Operating system operations
- `pathlib` → Modern path handling
- `zipfile` → Advanced ZIP file operations

---

## Best Practices

- Verify source and destination paths before copying.
- Use `copy2()` when metadata should be preserved.
- Be careful with `rmtree()` because it permanently deletes directories.
- Test file operations inside a practice folder.

---

## Common Mistakes

- Using `copy()` when metadata preservation is required.
- Running `rmtree()` on the wrong directory.
- Forgetting that `copytree()` requires the destination not to exist (unless using supported options in newer Python versions).

---

## Mini Project

### Backup Manager

Features:

- Copy Files
- Move Files
- Copy Folders
- Delete Folders
- Check Disk Usage
- Create ZIP Backup
- Extract ZIP Backup

---

## References

Official Python Documentation

https://docs.python.org/3/library/shutil.html