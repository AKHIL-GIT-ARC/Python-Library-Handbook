## Prerequisites
Before learning `shutil`, you should know:
- Basic file paths
- The `os` module
- The `pathlib` module

# Shutil Module Cheat Sheet

## Import

```python
import shutil
```

The `shutil` module provides high-level file and directory operations such as copying, moving, deleting folders, creating archives, and checking disk usage.

---

## 1. shutil.copy()

**Purpose:** Copies a file.

**Syntax**

```python
shutil.copy(src, dst)
```
**Returns:** Destination path.

**Example**

```python
shutil.copy("source/file.txt", "destination/")
```

**Real-world Uses**
- File backups
- Duplicate files
- Deployment scripts

---

## 2. shutil.copy2()

**Purpose:** Copies a file along with its metadata.

**Syntax**

```python
shutil.copy2(src, dst)
```

**Example**

```python
shutil.copy2("source/file.txt", "destination/")
```

> 💡 **Interview Tip:** Use `copy2()` when you want to preserve timestamps and metadata.

---

## 3. shutil.copytree()

**Purpose:** Copies an entire directory.

**Syntax**

```python
shutil.copytree(src, dst)
```

**Example**

```python
shutil.copytree("source", "backup")
```

**Real-world Uses**
- Project backups
- Folder duplication

---

## 4. shutil.move()

**Purpose:** Moves or renames files and folders.

**Syntax**

```python
shutil.move(src, dst)
```

**Example**

```python
shutil.move("source/file.txt", "backup/")
```

---

## 5. shutil.rmtree()

**Purpose:** Deletes a directory and all of its contents.

**Syntax**

```python
shutil.rmtree(path)
```

**Example**

```python
shutil.rmtree("backup")
```

> ⚠️ Permanently deletes the entire folder.

---

## 6. shutil.disk_usage()

**Purpose:** Returns disk usage statistics.

**Syntax**

```python
shutil.disk_usage(path)
```

**Returns**

```python
(total, used, free)
```

**Example**

```python
usage = shutil.disk_usage("/")
```

---

## 7. shutil.make_archive()

**Purpose:** Creates an archive (ZIP, TAR, etc.).

**Syntax**

```python
shutil.make_archive(base_name, format, root_dir)
```

**Example**

```python
shutil.make_archive("backup", "zip", "source")
```

---

## 8. shutil.unpack_archive()

**Purpose:** Extracts an archive.

**Syntax**

```python
shutil.unpack_archive(filename, extract_dir)
```

**Example**

```python
shutil.unpack_archive("backup.zip", "restore")
```

---

## 9. shutil.which()

**Purpose:** Finds the location of an executable.

**Syntax**

```python
shutil.which(command)
```

**Example**

```python
shutil.which("python")
```

---

# Comparison

## copy() vs copy2()

| copy() | copy2() |
|----------|----------|
| Copies only file content | Copies file and metadata |

---

## move() vs rename()

| move() | rename() |
|----------|-----------|
| Moves across directories/drives | Mainly renames or moves within the same filesystem |

---

## copytree() vs copy()

| copy() | copytree() |
|----------|------------|
| Copies one file | Copies an entire directory |

---

## rmdir() vs rmtree()

| os.rmdir() | shutil.rmtree() |
|-------------|-----------------|
| Deletes only empty folders | Deletes folders with all contents |

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `copy()` | Copy file |
| `copy2()` | Copy file with metadata |
| `copytree()` | Copy folder |
| `move()` | Move file/folder |
| `rmtree()` | Delete folder recursively |
| `disk_usage()` | Disk information |
| `make_archive()` | Create archive |
| `unpack_archive()` | Extract archive |
| `which()` | Find executable |

---

# Best Practices

- Use `copy2()` when metadata is important.
- Verify source and destination paths before copying.
- Test destructive operations in a practice folder.
- Use `make_archive()` for quick project backups.
- Handle file operations using `try-except`.

---

# Common Mistakes

- Using `copy()` when metadata should be preserved.
- Running `rmtree()` on the wrong directory.
- Copying into a destination that already exists with `copytree()`.
- Forgetting to check file existence before moving.

---

# ⚠️ Dangerous Operations

The following functions permanently modify or delete data:

- `move()`
- `rmtree()`
- `make_archive()` (may overwrite existing archives)

Always:

- Verify the source path.
- Verify the destination path.
- Work inside a practice folder.
- Keep backups of important files.

---

# When Should I Use This Module?

✅ **Use `shutil` when:**

- Copying files
- Moving files
- Backing up folders
- Creating ZIP archives
- Restoring backups

❌ **Avoid `shutil` when:**

- Working with individual file contents.
- Performing low-level OS operations.

➡ **Better Alternatives**

- `pathlib` → Modern path handling
- `os` → Low-level OS operations
- `zipfile` → Advanced ZIP file management

---

# Quick Revision
| Need | Function |
|------|----------|
| Copy File | `copy()` |
| Copy with Metadata | `copy2()` |
| Copy Folder | `copytree()` |
| Move File | `move()` |
| Delete Folder | `rmtree()` |
| Disk Usage | `disk_usage()` |
| Create ZIP | `make_archive()` |
| Extract ZIP | `unpack_archive()` |
| Find Executable | `which()` |