# JSON Module

## Introduction

The `json` module is a built-in Python library used to work with JSON (JavaScript Object Notation) data. It allows Python programs to read, write, convert, and exchange data in a lightweight, human-readable format.

JSON is one of the most widely used data formats for APIs, configuration files, databases, and data exchange between applications.

---

## Why Learn This Library?

The `json` module is widely used in:

- REST APIs
- Web Development
- Mobile Applications
- AI Applications
- Configuration Files
- Cloud Services
- Data Storage

---

## Features

- Read JSON files
- Write JSON files
- Convert Python objects to JSON
- Convert JSON to Python objects
- Pretty print JSON data
- Exchange data between applications

---

## Installation

The `json` module is built into Python.

No installation is required.

---

## Import

```python
import json
```

---

## Important Functions

- json.dump()
- json.dumps()
- json.load()
- json.loads()

---

## Python ↔ JSON Conversion

| Python | JSON |
|---------|------|
| `dict` | Object |
| `list` | Array |
| `str` | String |
| `int` | Number |
| `float` | Number |
| `True` | `true` |
| `False` | `false` |
| `None` | `null` |

---

## Real-world Applications

- API Communication
- User Data Storage
- Configuration Files
- Machine Learning Datasets
- Web Applications
- Mobile Apps
- Cloud Services

---

## Advantages

- Human-readable
- Lightweight
- Platform-independent
- Easy to parse
- Supported by almost every programming language

---

## Limitations

- Does not support Python-specific objects directly.
- Cannot store functions or classes.
- Less efficient than some binary formats for very large datasets.

---

## Related Modules

- `csv` → Tabular data
- `sqlite3` → Database storage
- `pickle` → Python object serialization

---

## Migration from Previous Modules

| Previous Storage | JSON Alternative |
|------------------|------------------|
| Text Files | Structured JSON Files |
| Manual Parsing | `json.load()` |
| Manual Writing | `json.dump()` |

---

## Best Practices

- Always use `with` statements when reading or writing files.
- Validate JSON data before processing.
- Use `indent=4` for readable output.
- Handle exceptions when loading JSON files.
- Store structured data using dictionaries and lists.

---

## Common Mistakes

- Confusing `dump()` with `dumps()`.
- Confusing `load()` with `loads()`.
- Forgetting to close files.
- Writing invalid JSON syntax manually.

---

## Importance

Essential for APIs, backend development, automation, AI, and cloud applications.

---

## Mini Project

### Student Record Manager

Features:

- Add Student
- View Students
- Search Student
- Update Student
- Delete Student
- Save Data to JSON

---

## References

Official Python Documentation

https://docs.python.org/3/library/json.html