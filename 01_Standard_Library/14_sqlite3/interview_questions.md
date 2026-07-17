# SQLite3 Module Interview Questions

## Beginner Level

### 1. What is SQLite?

**Answer:**

SQLite is a lightweight, serverless relational database that stores data in a single database file.

---

### 2. What is the `sqlite3` module?

**Answer:**

The `sqlite3` module is a built-in Python library used to create and manage SQLite databases.

---

### 3. How do you import the `sqlite3` module?

```python
import sqlite3
```

---

### 4. What is a database?

**Answer:**

A database is an organized collection of data stored in tables.

---

### 5. What are the main database components?

| Component | Description |
|-----------|-------------|
| Database | Stores tables |
| Table | Stores records |
| Row | One record |
| Column | One field |
| Primary Key | Unique identifier |

---

## Intermediate Level

### 6. What does `sqlite3.connect()` do?

**Answer**

Connects to a SQLite database. If the database does not exist, it is created automatically.

```python
connection = sqlite3.connect("students.db")
```

---

### 7. What is a cursor?

**Answer**

A cursor is an object used to execute SQL statements and retrieve results from the database.

```python
cursor = connection.cursor()
```

---

### 8. What does `execute()` do?

**Answer**

Executes a single SQL statement.

```python
cursor.execute("SELECT * FROM students")
```

---

### 9. What does `executemany()` do?

**Answer**

Executes the same SQL statement multiple times with different values.

```python
cursor.executemany(sql_query, data)
```

---

### 10. Why is `commit()` important?

**Answer**

`commit()` saves database changes permanently after `INSERT`, `UPDATE`, or `DELETE`.

```python
connection.commit()
```

---

## Advanced Level

### 11. Difference between `fetchone()` and `fetchall()`?

| `fetchone()` | `fetchall()` |
|---------------|--------------|
| Returns one row | Returns all rows |
| Tuple | List of tuples |

---

### 12. Difference between `execute()` and `executemany()`?

| `execute()` | `executemany()` |
|-------------|-----------------|
| Executes one SQL statement | Executes multiple SQL statements |
| One record | Multiple records |

---

### 13. Why should parameterized queries (`?`) be used?

**Answer**

Parameterized queries prevent SQL Injection and safely pass user input to SQL statements.

```python
cursor.execute(
    "SELECT * FROM students WHERE id=?",
    (student_id,)
)
```

---

### 14. What happens if `commit()` is not called?

**Answer**

The changes are not saved permanently and may be lost when the program ends.

---

### 15. Why should `close()` always be called?

**Answer**

It closes the database connection and releases system resources.

```python
connection.close()
```

---

## Scenario-Based Questions

### 16. You want to create a new SQLite database. Which method will you use?

**Answer**

```python
sqlite3.connect()
```

---

### 17. You need to retrieve every student from the database. Which SQL statement will you use?

**Answer**

```sql
SELECT * FROM students
```

---

### 18. You need to update a student's course. Which SQL statement will you use?

**Answer**

```sql
UPDATE students
SET course = ?
WHERE id = ?
```

---

### 19. You need to delete a student record. Which SQL statement will you use?

**Answer**

```sql
DELETE FROM students
WHERE id = ?
```

---

# SQL Commands

| Command | Purpose |
|---------|---------|
| `CREATE TABLE` | Create a table |
| `INSERT INTO` | Insert records |
| `SELECT` | Read records |
| `UPDATE` | Update records |
| `DELETE` | Delete records |

---

# Best Practices

- Always close the database connection.
- Use parameterized queries (`?`).
- Call `commit()` after modifying data.
- Use `fetchone()` for one record.
- Use `fetchall()` for multiple records.

---

# Common Mistakes

- Forgetting `commit()`.
- Forgetting `close()`.
- Using string concatenation in SQL queries.
- Executing SQL without creating a cursor.

---

# Quick Revision

| Method | Purpose |
|---------|---------|
| `connect()` | Connect database |
| `cursor()` | Create cursor |
| `execute()` | Execute SQL |
| `executemany()` | Execute multiple SQL statements |
| `commit()` | Save changes |
| `fetchone()` | Get one row |
| `fetchall()` | Get all rows |
| `close()` | Close database |