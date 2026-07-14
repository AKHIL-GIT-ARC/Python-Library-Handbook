# Zipfile Module Cheat Sheet

## Import

```python
import zipfile
```

The `zipfile` module is used to create, read, write, extract, and manage ZIP archives.

---

## 1. zipfile.ZipFile()

**Purpose:** Opens or creates a ZIP archive.

**Syntax**

```python
zipfile.ZipFile(file, mode)
```

**Modes**

| Mode | Purpose |
|------|---------|
| `"r"` | Read an existing ZIP |
| `"w"` | Create a new ZIP (overwrite existing) |
| `"a"` | Add files to an existing ZIP |
| `"x"` | Create a new ZIP (error if it exists) |

**Example**

```python
with zipfile.ZipFile("files.zip", "w") as zip_file:
    pass
```

---

## 2. write()

**Purpose:** Adds a file to a ZIP archive.

**Syntax**

```python
zip_file.write(filename, arcname=None)
```

**Example**

```python
zip_file.write("notes.txt")
```

**Using `arcname`**

```python
zip_file.write(file, arcname=file.name)
```

> 💡 Stores only the filename inside the ZIP instead of the complete path.

---

## 3. printdir()

**Purpose:** Displays the contents of a ZIP archive.

**Syntax**

```python
zip_file.printdir()
```

---

## 4. namelist()

**Purpose:** Returns a list of filenames inside the archive.

**Syntax**

```python
zip_file.namelist()
```

**Returns**

```python
list
```

---

## 5. infolist()

**Purpose:** Returns information about every file.

**Syntax**

```python
zip_file.infolist()
```

**Example**

```python
for info in zip_file.infolist():
    print(info.filename)
```

---

## 6. read()

**Purpose:** Reads a file directly from the ZIP archive.

**Syntax**

```python
zip_file.read(filename)
```

**Returns**

```python
bytes
```

**Example**

```python
content = zip_file.read("notes.txt")

print(content.decode())
```

> 💡 Use `decode()` to convert bytes into readable text.

---

## 7. extract()

**Purpose:** Extracts one file.

**Syntax**

```python
zip_file.extract(filename, path)
```

**Example**

```python
zip_file.extract("notes.txt", "output")
```

---

## 8. extractall()

**Purpose:** Extracts all files.

**Syntax**

```python
zip_file.extractall(path)
```

**Example**

```python
zip_file.extractall("output")
```

---

# Comparison

## extract() vs extractall()

| extract() | extractall() |
|------------|--------------|
| Extracts one file | Extracts all files |

---

## namelist() vs infolist()

| namelist() | infolist() |
|-------------|------------|
| Returns filenames | Returns file metadata |

---

## write() vs read()

| write() | read() |
|----------|--------|
| Adds file to ZIP | Reads file from ZIP |

---

# Frequently Used Methods

| Method | Purpose |
|---------|---------|
| `ZipFile()` | Open/Create ZIP |
| `write()` | Add file |
| `printdir()` | Show ZIP contents |
| `namelist()` | List filenames |
| `infolist()` | File information |
| `read()` | Read file |
| `extract()` | Extract one file |
| `extractall()` | Extract all files |

---

# Best Practices

- Always use `with` statements.
- Use `arcname` to avoid storing unnecessary folder paths.
- Check archive contents before extracting.
- Store backups in a separate location.
- Close ZIP files properly.

---

# Common Mistakes

- Forgetting to use the correct mode (`r`, `w`, `a`, `x`).
- Forgetting to decode bytes returned by `read()`.
- Storing unnecessary directory paths inside the archive.
- Extracting files into the wrong directory.

---

# When Should I Use This Module?

✅ **Use `zipfile` when:**

- Creating backups
- Compressing projects
- Sharing multiple files
- Reading ZIP archives
- Extracting compressed files

❌ **Avoid `zipfile` when:**

- Working with non-ZIP archive formats.
- Performing general file operations.

➡ **Better Alternatives**

- `shutil` → Copying and moving files
- `pathlib` → Path management
- `tarfile` → TAR archive handling

---

# Quick Revision

| Need | Method |
|------|--------|
| Create/Open ZIP | `ZipFile()` |
| Add File | `write()` |
| Show Contents | `printdir()` |
| List Files | `namelist()` |
| File Details | `infolist()` |
| Read File | `read()` |
| Extract One | `extract()` |
| Extract All | `extractall()` |