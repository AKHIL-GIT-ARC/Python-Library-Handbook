# CSV Module Interview Questions

## Beginner Level

### 1. What is a CSV file?

**Answer:**

CSV (Comma-Separated Values) is a file format used to store tabular data in rows and columns. Each value is separated by a comma.

---

### 2. What is the `csv` module?

**Answer:**

The `csv` module is a built-in Python library used to read, write, and manage CSV files.

---

### 3. How do you import the `csv` module?

```python
import csv
```

---

### 4. Which classes are commonly used in the `csv` module?

**Answer**
- `csv.reader()`
- `csv.writer()`
- `csv.DictReader()`
- `csv.DictWriter()`

---

### 5. Why are CSV files widely used?

**Answer**

- Human-readable
- Lightweight
- Excel compatible
- Easy to import and export
- Supported by many applications

---

## Intermediate Level

### 6. What does `csv.reader()` do?

**Answer**

Reads rows from a CSV file.

```python
reader = csv.reader(file)
```

Each row is returned as a list.

---

### 7. What does `csv.writer()` do?

**Answer**

Writes rows to a CSV file.

```python
writer = csv.writer(file)
```

---

### 8. What does `csv.DictReader()` do?

**Answer**

Reads CSV rows as dictionaries using the header row as keys.

```python
reader = csv.DictReader(file)
```

---

### 9. What does `csv.DictWriter()` do?

**Answer**

Writes dictionaries to a CSV file.

```python
writer = csv.DictWriter(file, fieldnames=columns)
```

---

### 10. Why do we use `newline=""` while writing CSV files?

**Answer**

It prevents extra blank lines from appearing in the CSV file and allows the `csv` module to handle line breaks correctly.

```python
with open("employees.csv", "w", newline="") as file:
```

---

## Advanced Level

### 11. Difference between `reader()` and `DictReader()`?

| `reader()` | `DictReader()` |
|------------|----------------|
| Returns lists | Returns dictionaries |
| Access by index | Access by column name |

---

### 12. Difference between `writer()` and `DictWriter()`?

| `writer()` | `DictWriter()` |
|------------|----------------|
| Writes lists | Writes dictionaries |
| No field names | Requires field names |

---

### 13. Difference between `writerow()` and `writerows()`?

| `writerow()` | `writerows()` |
|--------------|---------------|
| Writes one row | Writes multiple rows |

---

### 14. Why does `DictWriter()` need `fieldnames`?

**Answer**

`fieldnames` defines the column names and determines the order in which data is written to the CSV file.

---

### 15. Why are all values read from a CSV file returned as strings?

**Answer**

Because CSV files store data as plain text. Convert values using functions like `int()` or `float()` when needed.

Example:

```python
age = int(row["Age"])
```

---

## Scenario-Based Questions

### 16. You need to export employee data to Excel. Which module will you use?

**Answer**

```python
csv
```

---

### 17. You want to access values using column names instead of indexes. Which class will you use?

**Answer**

```python
csv.DictReader()
```

---

### 18. You have employee information stored as dictionaries. Which class will you use to save it?

**Answer**

```python
csv.DictWriter()
```

---

### 19. You need to write several employee records at once. Which method will you use?

**Answer**

```python
writer.writerows()
```

---

# Best Practices

- Always use `with` statements.
- Use `newline=""` while writing CSV files.
- Write the header before writing records.
- Use `DictReader()` and `DictWriter()` for better readability.
- Validate data before saving.

---

# Memory Trick

```
reader()
↓

Reads Lists

writer()
↓

Writes Lists

DictReader()
↓

Reads Dictionaries

DictWriter()
↓

Writes Dictionaries
```

**"Dict" = Dictionary**

---

# Quick Revision

| Class / Method | Purpose |
|----------------|---------|
| `reader()` | Read CSV |
| `writer()` | Write CSV |
| `DictReader()` | Read dictionaries |
| `DictWriter()` | Write dictionaries |
| `writerow()` | Write one row |
| `writerows()` | Write multiple rows |
| `writeheader()` | Write header row |