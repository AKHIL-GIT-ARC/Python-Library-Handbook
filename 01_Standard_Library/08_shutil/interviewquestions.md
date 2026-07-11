# Shutil Module Interview Questions

## Beginner Level

### 1. What is the `shutil` module?

**Answer:**
The `shutil` module is a built-in Python library that provides high-level file and directory operations such as copying, moving, deleting directories, and creating archives.

---

### 2. How do you import the `shutil` module?

```python
import shutil
```

---

### 3. Which function copies a file?

**Answer**

```python
shutil.copy(src, dst)
```

---

### 4. Which function moves a file or folder?

**Answer**

```python
shutil.move(src, dst)
```

---

### 5. Which function deletes an entire directory?

**Answer**

```python
shutil.rmtree(path)
```

---

## Intermediate Level

### 6. Difference between `copy()` and `copy2()`?

| `copy()` | `copy2()` |
|-----------|-----------|
| Copies file contents | Copies file and metadata |
| Faster | Preserves timestamps and permissions (where supported) |

---

### 7. Difference between `copy()` and `copytree()`?

| `copy()` | `copytree()` |
|-----------|--------------|
| Copies one file | Copies an entire directory |

---

### 8. What does `disk_usage()` return?

**Answer**

It returns disk space information.

```python
usage = shutil.disk_usage("/")
```

Returns:

```python
(total, used, free)
```

---

### 9. What is the purpose of `make_archive()`?

**Answer**

Creates compressed archives such as ZIP files.

```python
shutil.make_archive("backup", "zip", "source")
```

---

### 10. What is the purpose of `unpack_archive()`?

**Answer**

Extracts an archive into a directory.

```python
shutil.unpack_archive("backup.zip", "restore")
```

---

## Advanced Level

### 11. Why would you use `copy2()` instead of `copy()`?

**Answer**

When preserving file metadata such as timestamps and permissions is important.

---

### 12. Why is `rmtree()` considered dangerous?

**Answer**

Because it permanently deletes a directory and all of its contents.

---

### 13. What does `shutil.which()` do?

**Answer**

Finds the full path of an executable in the system's PATH.

```python
shutil.which("python")
```

---

### 14. Difference between `os.rename()` and `shutil.move()`?

| `os.rename()` | `shutil.move()` |
|----------------|-----------------|
| Mainly renames or moves within the same filesystem | Can move files across directories or drives |

---

### 15. Why should destructive operations be wrapped in `try-except`?

**Answer**

To safely handle:
- File not found
- Permission denied
- Destination already exists
- Invalid paths

---

## Scenario-Based Questions

### 16. You need to back up an entire project folder. Which function will you use?

**Answer**

```python
shutil.copytree()
```

---

### 17. You need to create a ZIP backup of a project. Which function will you use?

**Answer**

```python
shutil.make_archive()
```

---

### 18. You need to restore files from a ZIP archive. Which function will you use?

**Answer**

```python
shutil.unpack_archive()
```

---

### 19. You need to permanently remove a folder with all its files. Which function will you use?

**Answer**

```python
shutil.rmtree()
```

---

# Best Practices

- Prefer `copy2()` when metadata matters.
- Verify paths before moving or deleting files.
- Test `rmtree()` only inside a practice directory.
- Create backups before destructive operations.

---

# Quick Revision

| Function | Purpose |
|----------|---------|
| `copy()` | Copy file |
| `copy2()` | Copy file with metadata |
| `copytree()` | Copy folder |
| `move()` | Move file/folder |
| `rmtree()` | Delete folder recursively |
| `disk_usage()` | Disk usage |
| `make_archive()` | Create ZIP archive |
| `unpack_archive()` | Extract ZIP archive |
| `which()` | Find executable |