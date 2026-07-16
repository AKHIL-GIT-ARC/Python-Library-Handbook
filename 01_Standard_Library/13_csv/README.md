# CSV Module

## Introduction

The `csv` module is a built-in Python library used to read, write, and manipulate CSV (Comma-Separated Values) files. CSV files store data in rows and columns, making them one of the most common formats for spreadsheets, reports, and datasets.

The `csv` module is widely used in data analysis, machine learning, business applications, and Excel automation.

---

## Why Learn This Library?

The `csv` module is widely used in:
- Data Science
- Machine Learning
- Excel Automation
- Business Reports
- Inventory Systems
- Banking Applications
- Data Import & Export

---

## Features

- Read CSV files
- Write CSV files
- Read rows as dictionaries
- Write dictionaries to CSV
- Handle headers automatically
- Process tabular data

---

## Installation

The `csv` module is built into Python.
No installation is required.

---

## Import

```python
import csv
```

---

## Important Classes & Functions

- csv.reader()
- csv.writer()
- csv.DictReader()
- csv.DictWriter()

---

## CSV File Structure

Example:

```csv
ID,Name,Age,Department
101,Akhil,20,CSE
102,Rahul,21,AIML
103,Priya,19,CSE
```

The first row is called the **header**, and each subsequent row represents a record.

---

## Real-world Applications

- Employee Records
- Student Databases
- Sales Reports
- Kaggle Datasets
- Excel Files
- Financial Reports
- Data Migration

---

## Advantages

- Human-readable
- Lightweight
- Excel compatible
- Easy to import and export
- Supported by almost every programming language

---

## Limitations

- Supports only flat (tabular) data.
- Does not support nested structures.
- No built-in data validation.
- Data types are stored as text.

---

## Related Modules

- `json` → Structured data
- `sqlite3` → Relational database
- `pandas` → Advanced data analysis

---

## Migration from Previous Modules

| JSON | CSV |
|------|-----|
| Objects | Rows |
| Dictionaries | Columns |
| Nested Data | Flat Data |
| APIs | Excel & Reports |

---

## Best Practices

- Always use `with` statements.
- Use `newline=""` when opening CSV files for writing.
- Write headers before writing records.
- Use `DictReader()` and `DictWriter()` when working with named columns.
- Validate data before saving.

---

## Common Mistakes

- Forgetting `newline=""` while writing.
- Skipping the header row.
- Mixing column order.
- Assuming values are automatically converted to integers or floats.

---

## Mini Project

### Employee Management System

Features:

- Add Employee
- View Employees
- Search Employee
- Update Employee
- Delete Employee
- Save Data to CSV

---

## References

Official Python Documentation

https://docs.python.org/3/library/csv.html