# Glob Module

## Introduction

The `glob` module is a built-in Python library used to search for files and directories using wildcard patterns. It makes finding files simple without manually traversing directories.

The `glob` module is commonly used for locating files by extension, filename patterns, and recursive searches.

---

## Why Learn This Library?

The `glob` module is widely used in:

- Automation Scripts
- Data Science
- Machine Learning
- Log Analysis
- File Management Systems
- Backup Utilities
- Batch Processing

---

## Features

- Search files using wildcard patterns
- Recursive file searching
- Find files by extension
- Iterate through search results
- Cross-platform support

---

## Installation

The `glob` module is built into Python.

No installation is required.

---

## Import

```python
import glob
```

---

## Important Functions

- glob.glob()
- glob.iglob()

---

## Wildcards

| Wildcard | Meaning | Example |
|----------|---------|---------|
| `*` | Matches any number of characters | `*.py` |
| `?` | Matches exactly one character | `file?.txt` |
| `[]` | Matches a range or set of characters | `file[1-3].txt` |
| `**` | Recursive directory search | `**/*.py` |

---

## Real-world Applications

- Finding Python files
- Searching log files
- Loading datasets
- Processing images
- Finding configuration files
- Batch file processing

---

## Advantages

- Very easy to use
- Supports wildcard searching
- Recursive search support
- Platform-independent
- Faster than manually checking filenames

---

## Limitations

- Only searches file paths
- Cannot read file contents
- Less flexible than `pathlib` for file operations

---

## Related Modules

- `pathlib` → Modern path handling(object oriented approach) and file
   searching
- `os` → Basic level operating system interaction
- `shutil` → High level file operations.Copying and moving files

---

## Migration from Previous Modules

| Task | pathlib | glob |
|------|----------|------|
| Search Python files | `Path.glob("*.py")` | `glob.glob("*.py")` |
| Recursive search | `Path.rglob("*.py")` | `glob.glob("**/*.py", recursive=True)` |

---

## Best Practices

- Use specific patterns whenever possible.
- Use `recursive=True` only when needed.
- Prefer `pathlib.Path.glob()` in modern projects.
- Verify that search results are not empty before processing them.

---

## Common Mistakes

- Forgetting `recursive=True` when using `**`.
- Using incorrect wildcard patterns.
- Assuming `glob()` reads file contents (it only returns file paths).

---
## Mini Project

### File Search Utility

Features:

- Search Python files
- Search Text files
- Search Images
- Search Custom Extensions
- Recursive Search

---

## References

Official Python Documentation

https://docs.python.org/3/library/glob.html