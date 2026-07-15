# JSON Module Cheat Sheet

## Import

```python
import json
```

The `json` module is used to read, write, and convert JSON data. It is commonly used for APIs, configuration files, and data storage.

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

## 1. json.dump()

**Purpose:** Writes a Python object to a JSON file.

**Syntax**

```python
json.dump(obj, file, indent=4)
```

**Example**

```python
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
```

**Returns**

```
None
```

---

## 2. json.load()

**Purpose:** Reads JSON data from a file.

**Syntax**

```python
json.load(file)
```

**Example**

```python
with open("students.json", "r") as file:
    data = json.load(file)
```

**Returns**

```
Python Object
```

---

## 3. json.dumps()

**Purpose:** Converts a Python object into a JSON string.

**Syntax**

```python
json.dumps(obj, indent=4)
```

**Example**

```python
json_string = json.dumps(data, indent=4)
```

**Returns**

```
String
```

---

## 4. json.loads()

**Purpose:** Converts a JSON string into a Python object.

**Syntax**

```python
json.loads(json_string)
```

**Example**

```python
python_data = json.loads(json_string)
```

**Returns**

```
Python Object
```

---

# dump() vs dumps()

| `dump()` | `dumps()` |
|-----------|-----------|
| Writes to a file | Returns a JSON string |
| Uses a file object | Uses a Python object |

---

# load() vs loads()

| `load()` | `loads()` |
|-----------|-----------|
| Reads from a file | Reads from a JSON string |
| Returns a Python object | Returns a Python object |

---

# File vs String

| Function | Works With |
|----------|------------|
| `dump()` | JSON File |
| `load()` | JSON File |
| `dumps()` | JSON String |
| `loads()` | JSON String |

---

# Pretty Printing

Use `indent` to make JSON readable.

```python
json.dump(data, file, indent=4)
```

or

```python
json.dumps(data, indent=4)
```

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `dump()` | Write JSON file |
| `load()` | Read JSON file |
| `dumps()` | Convert object to JSON string |
| `loads()` | Convert JSON string to object |

---

# Best Practices

- Use `with` statements for file handling.
- Use `indent=4` for readable JSON.
- Store structured data using dictionaries and lists.
- Handle invalid JSON using `try-except`.
- Validate data before saving.

---

# Common Mistakes

- Confusing `dump()` with `dumps()`.
- Confusing `load()` with `loads()`.
- Forgetting `indent` when readability is important.
- Manually editing JSON with invalid syntax.

---

# When Should I Use This Module?

✅ **Use `json` when:**

- Working with APIs
- Saving application data
- Reading configuration files
- Exchanging data between applications
- Storing structured information

❌ **Avoid `json` when:**

- Handling relational data.
- Storing very large datasets requiring complex queries.

➡ **Better Alternatives**

- `csv` → Spreadsheet/tabular data
- `sqlite3` → Relational database
- `pickle` → Python object serialization

---

# Memory Trick

```
dump  → File
load  → File
dumps → String
loads → String
```
**Extra `s` = String**

---

# Quick Revision

| Need | Function |
|------|----------|
| Write JSON File | `dump()` |
| Read JSON File | `load()` |
| Python → JSON String | `dumps()` |
| JSON String → Python | `loads()` |
| Pretty Print | `indent=4` |