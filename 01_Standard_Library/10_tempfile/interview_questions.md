# Tempfile Module Interview Questions

## Beginner Level

### 1. What is the `tempfile` module?

**Answer:**

The `tempfile` module is a built-in Python library used to create temporary files and directories securely. These resources are automatically removed when they are no longer needed.

---

### 2. How do you import the `tempfile` module?

```python
import tempfile
```

---

### 3. Which function returns the system temporary directory?

**Answer**

```python
tempfile.gettempdir()
```

---

### 4. What is a temporary file?

**Answer**

A temporary file is a file created for short-term use during program execution. It is usually deleted automatically after use.

---

### 5. Why should we use temporary files?

**Answer**

- Avoid unnecessary files
- Improve security
- Automatic cleanup
- Ideal for temporary data

---

## Intermediate Level

### 6. What is the difference between `TemporaryFile()` and `NamedTemporaryFile()`?

| `TemporaryFile()` | `NamedTemporaryFile()` |
|-------------------|------------------------|
| No visible filename | Has a filename |
| Used internally | Can be accessed by other programs |
| Automatically deleted | Automatically deleted |

---

### 7. What does `TemporaryDirectory()` do?

**Answer**

It creates a temporary directory that is automatically deleted when the context ends.

```python
with tempfile.TemporaryDirectory() as folder:
    print(folder)
```

---

### 8. What is the purpose of `SpooledTemporaryFile()`?

**Answer**

It stores small data in memory and automatically switches to disk storage when the data becomes large.

---

### 9. What does `mkstemp()` return?

**Answer**

```python
fd, path = tempfile.mkstemp()
```

Returns:

- File Descriptor (`fd`)
- File Path (`path`)

---

### 10. What does `mkdtemp()` do?

**Answer**

Creates a secure temporary directory that must be deleted manually.

---

## Advanced Level

### 11. Why is `TemporaryFile()` preferred over creating a normal file?

**Answer**

Because it provides automatic cleanup, improves security, and prevents unnecessary temporary files from remaining on the system.

---

### 12. Why should `mkstemp()` be cleaned manually?

**Answer**

Because Python does not automatically remove files created using `mkstemp()`.

Example:

```python
import os

fd, path = tempfile.mkstemp()

os.close(fd)
os.remove(path)
```

---

### 13. What is the purpose of `seek(0)`?

**Answer**

It moves the file pointer to the beginning of the file before reading.

```python
file.seek(0)
```

---

### 14. Why are `with` statements commonly used with `tempfile`?

**Answer**

Because they automatically close and clean up temporary resources after use.

---

### 15. Which temporary resources are deleted automatically?

| Function | Automatic Cleanup |
|-----------|-------------------|
| `TemporaryFile()` | ✅ Yes |
| `NamedTemporaryFile()` | ✅ Yes |
| `TemporaryDirectory()` | ✅ Yes |
| `mkstemp()` | ❌ No |
| `mkdtemp()` | ❌ No |

---

## Scenario-Based Questions

### 16. A web application needs to process an uploaded image before saving it permanently. Which function would you use?

**Answer**

```python
tempfile.TemporaryFile()
```

---

### 17. You need a temporary folder for extracting ZIP files. Which function will you use?

**Answer**

```python
tempfile.TemporaryDirectory()
```

---

### 18. Which `tempfile` function stores data in memory before using disk storage?

**Answer**

```python
tempfile.SpooledTemporaryFile()
```

---

# Best Practices

- Use `with` statements whenever possible.
- Use `NamedTemporaryFile()` when another program needs the filename.
- Clean up `mkstemp()` and `mkdtemp()` manually.
- Do not use temporary files for permanent storage.

---

# Quick Revision

| Function | Purpose |
|----------|---------|
| `gettempdir()` | System temp directory |
| `TemporaryFile()` | Anonymous temp file |
| `NamedTemporaryFile()` | Named temp file |
| `TemporaryDirectory()` | Temp directory |
| `SpooledTemporaryFile()` | Memory-to-disk temp file |
| `mkstemp()` | Secure temp file |
| `mkdtemp()` | Secure temp directory |