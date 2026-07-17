# SQLite3 Module

## Introduction

The `sqlite3` module is a built-in Python library used to work with SQLite databases. It allows Python programs to create databases, create tables, insert records, retrieve data, update records, and delete records using SQL.
SQLite is a lightweight, serverless relational database that stores data in a single file.

---

## Why Learn This Library?

The `sqlite3` module is widely used in:
- Backend Development
- Desktop Applications
- Android Applications
- Data Management
- Inventory Systems
- Student Management Systems
- Banking Applications

---

## Features

- Create databases
- Create tables
- Insert records
- Retrieve records
- Update records
- Delete records
- Execute SQL queries

---

## Installation

The `sqlite3` module is built into Python.
No installation is required.

---

## Import

```python
import sqlite3
```

---

## Important Methods

- sqlite3.connect()
- connection.cursor()
- cursor.execute()
- cursor.executemany()
- connection.commit()
- cursor.fetchone()
- cursor.fetchall()
- connection.close()

---

## Database Components

| Component | Description |
|-----------|-------------|
| Database | Stores all tables |
| Table | Stores related records |
| Row | One complete record |
| Column | One attribute of a record |
| Primary Key | Uniquely identifies each row |

---

## Example Table

| ID | Name | Age | Course |
|----|------|-----|---------|
| 101 | Akhil | 19 | CSE |
| 102 | Charan | 19 | AIML |
| 103 | Om | 19 | CSE |

---

## SQL Operations

- CREATE
- INSERT
- SELECT
- UPDATE
- DELETE
These operations are commonly known as **CRUD**:
| Operation | SQL Command |
|-----------|-------------|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

## Real-world Applications

- Student Management Systems
- Employee Management Systems
- Library Management Systems
- Hospital Management Systems
- Inventory Systems
- Billing Software

---

## Advantages

- Built into Python
- No database server required
- Lightweight
- Fast
- Easy to learn
- Cross-platform

---

## Limitations

- Not suitable for very large applications.
- Limited support for many simultaneous users.
- Not designed for distributed databases.

---

## Related Modules

- `json` → File-based structured storage
- `csv` → Spreadsheet/tabular data
- `sqlite3` → Relational database
- `pandas` → Data analysis

---

## Migration from Previous Modules

| JSON | CSV | SQLite |
|------|-----|---------|
| Objects | Rows | Database Tables |
| File Storage | Spreadsheet | SQL Database |
| No SQL | No SQL | SQL Queries |

---

## Best Practices

- Always close the database connection.
- Use parameterized queries instead of string formatting.
- Commit changes after INSERT, UPDATE, or DELETE.
- Use `with` statements when appropriate.
- Handle database exceptions.

---

## Common Mistakes

- Forgetting `commit()`.
- Forgetting `close()`.
- Using string concatenation in SQL queries.
- Executing queries without creating a cursor.

---

## Mini Project

### Student Database Management System

Features:
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

---

## References

Official Python Documentation

https://docs.python.org/3/library/sqlite3.html