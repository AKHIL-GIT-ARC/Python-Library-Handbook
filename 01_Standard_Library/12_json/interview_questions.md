# JSON Module Interview Questions

## Beginner Level

### 1. What is JSON?

**Answer:**

JSON (JavaScript Object Notation) is a lightweight, human-readable format used to store and exchange data between applications.

---

### 2. What is the `json` module?

**Answer:**

The `json` module is a built-in Python library used to read, write, and convert JSON data.

---

### 3. How do you import the `json` module?

```python
import json
```

---

### 4. What are the four main functions of the `json` module?

**Answer**

- `json.dump()`
- `json.load()`
- `json.dumps()`
- `json.loads()`

---

### 5. Why is JSON widely used?

**Answer**

- Human-readable
- Lightweight
- Easy to exchange data
- Supported by almost every programming language
- Commonly used in APIs and web applications

---

## Intermediate Level

### 6. What does `json.dump()` do?

**Answer**

Writes a Python object to a JSON file.

```python
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

### 7. What does `json.load()` do?

**Answer**

Reads JSON data from a file and converts it into a Python object.

```python
with open("students.json", "r") as file:
    data = json.load(file)
```

---

### 8. What does `json.dumps()` do?

**Answer**

Converts a Python object into a JSON string.

```python
json_string = json.dumps(data)
```

---

### 9. What does `json.loads()` do?

**Answer**

Converts a JSON string into a Python object.

```python
python_data = json.loads(json_string)
```

---

### 10. What is the purpose of `indent=4`?

**Answer**

It formats JSON data with proper indentation, making it easier to read.

---

## Advanced Level

### 11. Difference between `dump()` and `dumps()`?

| `dump()` | `dumps()` |
|-----------|-----------|
| Writes to a JSON file | Returns a JSON string |
| Uses a file object | Uses a Python object |

---

### 12. Difference between `load()` and `loads()`?

| `load()` | `loads()` |
|-----------|-----------|
| Reads from a JSON file | Reads from a JSON string |
| Returns a Python object | Returns a Python object |

---

### 13. How are Python data types converted to JSON?

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

### 14. Why should `with` statements be used with JSON files?

**Answer**

Because they automatically close the file after reading or writing, preventing resource leaks.

---

### 15. What happens if a JSON file contains invalid syntax?

**Answer**

Python raises a `json.JSONDecodeError`.

Example:

```python
try:
    with open("students.json", "r") as file:
        data = json.load(file)
except json.JSONDecodeError:
    print("Invalid JSON file.")
```

---

## Scenario-Based Questions

### 16. You need to save application settings permanently. Which function will you use?

**Answer**

```python
json.dump()
```

---

### 17. You receive JSON data from an API as a string. Which function will you use?

**Answer**

```python
json.loads()
```

---

### 18. You need to convert a Python dictionary into a JSON string before sending it to a web service. Which function will you use?

**Answer**

```python
json.dumps()
```

---

### 19. You need to read student records stored in a JSON file. Which function will you use?

**Answer**

```python
json.load()
```

---

# Best Practices

- Use `with` statements for file operations.
- Use `indent=4` for readable JSON.
- Validate JSON before processing.
- Handle `JSONDecodeError` using `try-except`.
- Store structured data using dictionaries and lists.

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

| Function | Purpose |
|----------|---------|
| `dump()` | Write JSON file |
| `load()` | Read JSON file |
| `dumps()` | Python object → JSON string |
| `loads()` | JSON string → Python object |
| `indent=4` | Pretty-print JSON |