# Zipfile Module Interview Questions

## Beginner Level

### 1. What is the `zipfile` module?

**Answer:**

The `zipfile` module is a built-in Python library used to create, read, write, and extract ZIP archives.

---

### 2. How do you import the `zipfile` module?

```python
import zipfile
```

---

### 3. Which class is used to work with ZIP archives?

**Answer**

```python
zipfile.ZipFile()
```

---

### 4. What are the different modes of `ZipFile()`?

| Mode | Purpose |
|------|---------|
| `"r"` | Read an existing ZIP archive |
| `"w"` | Create a new ZIP archive (overwrite existing) |
| `"a"` | Append files to an existing ZIP archive |
| `"x"` | Create a new ZIP archive (fails if it already exists) |

---

### 5. Why are ZIP files used?

**Answer**

- Compress files
- Save storage space
- Create backups
- Share multiple files as one archive
- Organize project files

---

## Intermediate Level

### 6. What does `write()` do?

**Answer**

Adds a file to a ZIP archive.

```python
zip_file.write("notes.txt")
```

---

### 7. What is the purpose of `arcname`?

**Answer**

`arcname` specifies the name stored inside the ZIP archive instead of the original file path.

```python
zip_file.write(file, arcname=file.name)
```

---

### 8. What does `namelist()` return?

**Answer**

Returns a list containing the names of all files inside the ZIP archive.

```python
files = zip_file.namelist()
```

---

### 9. What does `infolist()` return?

**Answer**

Returns information about every file stored in the ZIP archive.

```python
for info in zip_file.infolist():
    print(info.filename)
```

---

### 10. What does `printdir()` do?

**Answer**

Displays the contents of the ZIP archive in a formatted table.

```python
zip_file.printdir()
```

---

## Advanced Level

### 11. What does `read()` return?

**Answer**

It returns the file contents as **bytes**.

```python
content = zip_file.read("notes.txt")
```
---

### 12. Why do we use `decode()` after `read()`?

**Answer**

Because `read()` returns bytes, and `decode()` converts them into a readable string.

```python
print(content.decode())
```

---

### 13. Difference between `extract()` and `extractall()`?

| `extract()` | `extractall()` |
|--------------|----------------|
| Extracts one file | Extracts all files |

---

### 14. Why should `with` statements be used with `ZipFile()`?

**Answer**

They automatically close the ZIP archive after use, preventing resource leaks.

---

### 15. Difference between `namelist()` and `infolist()`?

| `namelist()` | `infolist()` |
|---------------|--------------|
| Returns filenames | Returns metadata such as filename, size, and date |

---

## Scenario-Based Questions

### 16. You need to create a backup of a project folder. Which class will you use?

**Answer**

```python
zipfile.ZipFile()
```

---

### 17. You need to see all files inside a ZIP archive without extracting them. Which method will you use?

**Answer**

```python
zip_file.namelist()
```

or

```python
zip_file.printdir()
```

---

### 18. You need to read a file directly from a ZIP archive without extracting it. Which method will you use?

**Answer**

```python
zip_file.read()
```

---

### 19. Which method is used to extract only one file?

**Answer**

```python
zip_file.extract()
```

---

## Common Coding Questions

### 20. Create a ZIP archive.

```python
with zipfile.ZipFile("files.zip", "w"):
```

---

### 21. Add a file to a ZIP archive.

```python
zip_file.write("notes.txt")
```

---

### 22. Display all files inside a ZIP archive.

```python
zip_file.printdir()
```

or

```python
zip_file.namelist()
```

---

### 23. Read a file from a ZIP archive.

```python
content = zip_file.read("notes.txt")

print(content.decode())
```

---

### 24. Extract all files from a ZIP archive.

```python
zip_file.extractall("output")
```

---

# Best Practices

- Always use `with` statements.
- Use `arcname` to avoid storing unnecessary folder paths.
- Verify archive contents before extracting.
- Use meaningful archive names.
- Keep backup archives in a separate directory.

---

# Quick Revision

| Method | Purpose |
|---------|---------|
| `ZipFile()` | Open/Create ZIP archive |
| `write()` | Add file |
| `printdir()` | Show ZIP contents |
| `namelist()` | List filenames |
| `infolist()` | File metadata |
| `read()` | Read file without extracting |
| `extract()` | Extract one file |
| `extractall()` | Extract all files |