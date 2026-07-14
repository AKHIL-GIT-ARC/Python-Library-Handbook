# Zipfile Module

## Introduction

The `zipfile` module is a built-in Python library used to create, read, write, extract, and manage ZIP archives. It allows multiple files and directories to be compressed into a single archive, making storage, backups, and file sharing more efficient.

The `zipfile` module is widely used in automation, backup systems, software distribution, and cloud applications.

---

## Why Learn This Library?

The `zipfile` module is widely used in:

- File Backup Systems
- Software Distribution
- Cloud Storage
- Automation Scripts
- Data Compression
- Project Archiving
- Deployment Tools

---

## Features

- Create ZIP archives
- Add files to archives
- Read files without extracting
- View archive contents
- Extract individual files
- Extract complete archives
- Access archive metadata

---

## Installation

The `zipfile` module is built into Python.

No installation is required.

---

## Import

```python
import zipfile
```

---

## Important Classes & Methods

- zipfile.ZipFile()
- write()
- extract()
- extractall()
- namelist()
- infolist()
- read()
- printdir()

---

## Real-world Applications

- Project Backups
- Email Attachments
- Software Installers
- Cloud Storage
- Log Archiving
- Data Compression
- File Sharing

---

## Advantages

- Built into Python
- Easy archive management
- Supports reading without extraction
- Cross-platform
- Simple API

---

## Limitations

- Works only with ZIP archives.
- Compression may not significantly reduce already compressed files.
- Password protection support is limited.

---

## Related Modules

- `shutil` → Copy and move files (High level)
- `pathlib` → Modern path handling (object oriented approach)
- `tempfile` → Temporary storage
- `os` → Operating system operations (basic)

---

## Migration from Previous Modules

| Previous Module | zipfile Alternative |
|-----------------|---------------------|
| `shutil.make_archive()` | `ZipFile()` |
| Manual compression | Automatic ZIP creation |
| Manual extraction | `extract()` / `extractall()` |

---

## Best Practices

- Use `with` statements when working with ZIP files.
- Close ZIP files properly.
- Validate archive contents before extraction.
- Use meaningful archive names.
- Store backups separately from source files.

---

## Common Mistakes

- Forgetting to close ZIP files.
- Using the wrong mode (`r`, `w`, `a`).
- Extracting archives into the wrong directory.
- Assuming compressed files are always smaller.

---

## Importance

Essential for automation, backup utilities, deployment tools, and file sharing.

---

## Mini Project

### ZIP Archive Manager

Features:
- Create ZIP Archive
- Add Files
- View Archive Contents
- Read Files
- Extract One File
- Extract Entire Archive

---

## References

Official Python Documentation

https://docs.python.org/3/library/zipfile.html