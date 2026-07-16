# CSV Module Cheat Sheet
## Import

```python
import csv
```
The `csv` module is used to read, write, and manage CSV (Comma-Separated Values) files.

---

## CSV File Structure

```csv
ID,Name,Age,Department
101,Akhil,20,CSE
102,Rahul,21,AIML
```
- First row → Header
- Remaining rows → Records

---

## 1. csv.reader()

**Purpose:** Reads rows from a CSV file.

**Syntax**

```python
csv.reader(file)
```

**Example**

```python
with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Returns**

```
List
```

Example Output

```python
['101', 'Akhil', '20', 'CSE']
```

---

## 2. csv.writer()

**Purpose:** Writes rows to a CSV file.

**Syntax**

```python
csv.writer(file)
```

**Example**

```python
with open("employees.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([101, "Akhil", 20, "CSE"])
# "a" will append new values again and again by changing it , "w" overwrites the current values 
# Which is better?
# I would suggest you to use "w"
```

---

## 3. writerow()

**Purpose:** Writes a single row.

**Syntax**

```python
writer.writerow(row)
```

**Example**

```python
writer.writerow([101, "Akhil", 20, "CSE"])
```

---

## 4. writerows()

**Purpose:** Writes multiple rows.

**Syntax**

```python
writer.writerows(rows)
```

**Example**

```python
writer.writerows(employees)
```

---

## 5. csv.DictReader()

**Purpose:** Reads CSV rows as dictionaries.

**Syntax**

```python
csv.DictReader(file)
```

**Example**

```python
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

**Returns**

```python
{
    "ID": "101",
    "Name": "Akhil",
    "Age": "20",
    "Department": "CSE"
}
```
<!-- Imagine you have this row:
101,Akhil,20,CSE

Using reader():
['101', 'Akhil', '20', 'CSE']

You must remember:
0 → ID
1 → Name
2 → Age
3 → Department

Using DictReader():
{
    "ID": "101",
    "Name": "Akhil",
    "Age": "20",
    "Department": "CSE"
}
Now you can simply write:
employee["Department"]

instead of:
employee[3] -->
---

## 6. csv.DictWriter()

**Purpose:** Writes dictionaries to a CSV file.

**Syntax**

```python
csv.DictWriter(file, fieldnames=columns)
```

**Example**

```python
fieldnames = ["ID", "Name", "Age", "Department"]

writer = csv.DictWriter(file, fieldnames=fieldnames)
```

---

## 7. writeheader()

**Purpose:** Writes the header row.

**Syntax**

```python
writer.writeheader()
```

---

# reader() vs DictReader()

| `reader()` | `DictReader()` |
|------------|----------------|
| Returns lists | Returns dictionaries |
| Access by index | Access by column name |

---

# writer() vs DictWriter()

| `writer()` | `DictWriter()` |
|------------|----------------|
| Writes lists | Writes dictionaries |
| No field names | Requires field names |

---

# writerow() vs writerows()

| `writerow()` | `writerows()` |
|--------------|---------------|
| One row | Multiple rows |

---

# Frequently Used Classes

| Class | Purpose |
|-------|---------|
| `reader()` | Read CSV |
| `writer()` | Write CSV |
| `DictReader()` | Read dictionaries |
| `DictWriter()` | Write dictionaries |
| `writeheader()` | Write column names |

---

# Best Practices

- Always use `with` statements.
- Use `newline=""` when writing CSV files.
- Write the header before writing records.
- Use `DictReader()` for better readability.
- Validate data before saving.

---

# Common Mistakes

- Forgetting `newline=""`.
- Skipping the header row.
- Mixing column order.
- Assuming numeric values are automatically converted.

---

# When Should I Use This Module?

✅ **Use `csv` when:**

- Working with Excel files
- Processing datasets
- Creating reports
- Importing/exporting data
- Handling tabular information

❌ **Avoid `csv` when:**

- Working with nested data.
- Building relational databases.

➡ **Better Alternatives**

- `json` → Structured data
- `sqlite3` → Database storage
- `pandas` → Advanced data analysis

# Important

<!-- newline="" prevents extra blank lines from appearing in a CSV file while writing. It allows the csv module to handle line breaks correctly.
Example:
with open("employees.csv", "w", newline="") as file:
Memory Tip:
Writing CSV → Always use newline="" ✅ -->
---
# Quick Revision

| Need | Function |
|------|----------|
| Read CSV | `reader()` |
| Write CSV | `writer()` |
| Read Dictionaries | `DictReader()` |
| Write Dictionaries | `DictWriter()` |
| One Row | `writerow()` |
| Multiple Rows | `writerows()` |
| Header | `writeheader()` |