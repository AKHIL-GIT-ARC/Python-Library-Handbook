# SQLite3 Module Cheat Sheet

## Import

```python
import sqlite3
```
The `sqlite3` module is used to create and manage SQLite databases in Python.

---

## Database Components

| Component | Description |
|-----------|-------------|
| Database | Stores tables |
| Table | Stores records |
| Row | One record |
| Column | One field |
| Primary Key | Unique identifier |

---

## 1. connect()

**Purpose:** Connects to a SQLite database.

**Syntax**

```python
sqlite3.connect(database)
```

**Example**

```python
connection = sqlite3.connect("students.db")
```

---

## 2. cursor()

**Purpose:** Creates a cursor to execute SQL statements.

**Syntax**

```python
connection.cursor()
```

**Example**

```python
cursor = connection.cursor()
```

---

## 3. execute()

**Purpose:** Executes a single SQL statement.

**Syntax**

```python
cursor.execute(sql_query)
```

**Example**

```python
cursor.execute("SELECT * FROM students")
```

---

## 4. executemany()

**Purpose:** Executes the same SQL statement multiple times.

**Syntax**

```python
cursor.executemany(sql_query, data)
```

**Example**

```python
cursor.executemany(
    "INSERT INTO students(name, age) VALUES(?, ?)",
    students
)
```

---

## 5. commit()

**Purpose:** Saves changes permanently.

**Syntax**

```python
connection.commit()
```

---

## 6. fetchone()

**Purpose:** Returns one row.

**Syntax**

```python
cursor.fetchone()
```

**Returns**

```python
tuple
```

---

## 7. fetchall()

**Purpose:** Returns all rows.

**Syntax**

```python
cursor.fetchall()
```

**Returns**

```python
list
```

---

## 8. close()

**Purpose:** Closes the database connection.

**Syntax**

```python
connection.close()
```

---

# Common SQL Commands

## CREATE TABLE

```sql
CREATE TABLE students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
```

---

## INSERT

```sql
INSERT INTO students(name, age)
VALUES('Akhil', 20)
```

---

## SELECT

```sql
SELECT * FROM students
```

---

## UPDATE

```sql
UPDATE students
SET age = 21
WHERE id = 1
```

---

## DELETE

```sql
DELETE FROM students
WHERE id = 1
```

---

# execute() vs executemany()

| execute() | executemany() |
|------------|---------------|
| One SQL statement | Multiple SQL statements |
| One record | Multiple records |

---

# fetchone() vs fetchall()

| fetchone() | fetchall() |
|-------------|------------|
| One row | All rows |
| Tuple | List of tuples |

---

# Frequently Used Methods

| Method | Purpose |
|---------|---------|
| `connect()` | Connect database |
| `cursor()` | Create cursor |
| `execute()` | Execute SQL |
| `executemany()` | Execute multiple SQL statements |
| `commit()` | Save changes |
| `fetchone()` | One row |
| `fetchall()` | All rows |
| `close()` | Close database |

---

# SQL Data Types

| Data Type | Purpose |
|-----------|---------|
| `INTEGER` | Whole numbers |
| `REAL` | Decimal numbers |
| `TEXT` | Text values |
| `BLOB` | Binary data |
| `NULL` | Empty value |

---

# Best Practices

- Always close the database connection.
- Use parameterized queries (`?`) instead of string formatting.
- Call `commit()` after INSERT, UPDATE, or DELETE.
- Use `fetchone()` when expecting one result.
- Use `fetchall()` when retrieving multiple records.

---

# Common Mistakes

- Forgetting `commit()`.
- Forgetting `close()`.
- Building SQL queries using string concatenation.
- Executing SQL without creating a cursor.

---

# When Should I Use This Module?

✅ **Use `sqlite3` when:**

- Building desktop applications
- Learning SQL
- Creating small databases
- Storing structured application data
- Developing backend projects

❌ **Avoid `sqlite3` when:**

- Building very large multi-user systems.
- High-concurrency applications.

➡ **Better Alternatives**

- `MySQL` → Large web applications
- `PostgreSQL` → Enterprise databases
- `MongoDB` → NoSQL databases

---

# Quick Revision

| Need | Method |
|------|--------|
| Connect | `connect()` |
| Create Cursor | `cursor()` |
| Execute Query | `execute()` |
| Execute Multiple Queries | `executemany()` |
| Save Changes | `commit()` |
| Get One Row | `fetchone()` |
| Get All Rows | `fetchall()` |
| Close Database | `close()` |