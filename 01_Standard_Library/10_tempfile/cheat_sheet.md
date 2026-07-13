# Tempfile Module Cheat Sheet

## Resource Lifetime
TemporaryFile()
→ Deleted automatically when closed.

NamedTemporaryFile()
→ Lifetime depends on parameters.

TemporaryDirectory()
→ Deleted automatically when the context ends.

## Import

```python
import tempfile
```

The `tempfile` module is used to create temporary files and directories securely. Temporary resources are useful for storing data that is only needed while a program is running.

---

## 1. tempfile.gettempdir()

**Purpose:** Returns the system's temporary directory.

**Syntax**

```python
tempfile.gettempdir()
```

**Returns:** `str`

**Example**

```python
tempfile.gettempdir()
```

**Output**

```
C:\Users\User\AppData\Local\Temp
```

---

## 2. tempfile.TemporaryFile()

**Purpose:** Creates an anonymous temporary file.

**Syntax**

```python
tempfile.TemporaryFile(mode="w+t")
```

**Example**

```python
with tempfile.TemporaryFile(mode="w+t") as file:
    file.write("Hello")
```

**Features**

- Automatically deleted
- No filename
- Suitable for temporary storage

---

## 3. tempfile.NamedTemporaryFile()

**Purpose:** Creates a temporary file with a filename.

**Syntax**

```python
tempfile.NamedTemporaryFile(mode="w+t")
```

**Example**

```python
with tempfile.NamedTemporaryFile(mode="w+t") as file:
    print(file.name)
```

**Features**

- Has a filename
- Automatically deleted
- Can be shared with other programs

---

## 4. tempfile.TemporaryDirectory()

**Purpose:** Creates a temporary directory.

**Syntax**

```python
tempfile.TemporaryDirectory()
```

**Example**

```python
with tempfile.TemporaryDirectory() as folder:
    print(folder)
```

**Features**

- Automatically deleted
- Good for temporary project folders

---

## 5. tempfile.SpooledTemporaryFile()

**Purpose:** Stores data in memory until it becomes large, then moves it to disk.

**Syntax**

```python
tempfile.SpooledTemporaryFile(mode="w+t")
```

**Example**

```python
with tempfile.SpooledTemporaryFile(mode="w+t") as file:
    file.write("Hello")
```

**Real-world Uses**

- Large uploads
- Report generation
- Data processing

---

## 6. tempfile.mkstemp()

**Purpose:** Creates a secure temporary file.

**Syntax**

```python
tempfile.mkstemp()
```

**Returns**

```python
(fd, path)
```

**Example**

```python
fd, path = tempfile.mkstemp()
```

> ⚠️ Must be deleted manually.

---

## 7. tempfile.mkdtemp()

**Purpose:** Creates a secure temporary directory.

**Syntax**

```python
tempfile.mkdtemp()
```

**Example**

```python
folder = tempfile.mkdtemp()
```

> ⚠️ Must be deleted manually.

---

# Resource Lifetime

| Function | Deleted Automatically? |
|----------|------------------------|
| `TemporaryFile()` | ✅ Yes |
| `NamedTemporaryFile()` | ✅ Yes |
| `TemporaryDirectory()` | ✅ Yes |
| `mkstemp()` | ❌ No |
| `mkdtemp()` | ❌ No |

---

# Comparison

## TemporaryFile() vs NamedTemporaryFile()

| TemporaryFile() | NamedTemporaryFile() |
|-----------------|----------------------|
| No filename | Has filename |
| Internal use | Can be shared with other programs |

---

## TemporaryDirectory() vs mkdtemp()

| TemporaryDirectory() | mkdtemp() |
|----------------------|-----------|
| Automatic cleanup | Manual cleanup |
| Used with `with` | Must delete manually |

---

## TemporaryFile() vs mkstemp()

| TemporaryFile() | mkstemp() |
|-----------------|-----------|
| Automatic cleanup | Manual cleanup |
| File object | File descriptor & path |

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `gettempdir()` | System temp directory |
| `TemporaryFile()` | Anonymous temporary file |
| `NamedTemporaryFile()` | Named temporary file |
| `TemporaryDirectory()` | Temporary folder |
| `SpooledTemporaryFile()` | Memory-to-disk temporary file |
| `mkstemp()` | Secure temp file |
| `mkdtemp()` | Secure temp directory |

---

# Best Practices

- Use `with` statements whenever possible.
- Use `NamedTemporaryFile()` if another program needs the filename.
- Delete files created by `mkstemp()` manually.
- Delete folders created by `mkdtemp()` manually.
- Use temporary files only for short-term storage.

---

# Common Mistakes

- Forgetting `seek(0)` before reading.
- Assuming `mkstemp()` deletes files automatically.
- Assuming temporary files are permanent.
- Using temporary storage for long-term data.

---

# When Should I Use This Module?

✅ **Use `tempfile` when:**

- Processing uploaded files
- Creating temporary reports
- Testing applications
- Working with temporary data
- Creating temporary workspaces

❌ **Avoid `tempfile` when:**

- Data needs to be stored permanently.

➡ **Better Alternatives**

- `pathlib` → Permanent file management (Object oriented approach)
- `os` → Basic Operating system operations
- `shutil` → High level file operations like Copying and moving files

---

# Quick Revision

| Need | Function |
|------|----------|
| Temp Folder | `gettempdir()` |
| Temp File | `TemporaryFile()` |
| Named Temp File | `NamedTemporaryFile()` |
| Temp Directory | `TemporaryDirectory()` |
| Memory Temp File | `SpooledTemporaryFile()` |
| Secure Temp File | `mkstemp()` |
| Secure Temp Directory | `mkdtemp()` |