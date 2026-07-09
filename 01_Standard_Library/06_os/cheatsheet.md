## ⚠️ Safety Notes

- Always verify a file exists before deleting it.
- Never hardcode absolute paths.
- Use `os.path.join()` for portability.
- Test file operations in a temporary folder.

# OS Module Cheat Sheet

## Import

```python
import os
```

The `os` module provides functions to interact with the operating system, including file management, directory operations, path handling, and environment variables.

---

## 1. os.getcwd()

**Purpose:** Returns the current working directory.

**Syntax**

```python
os.getcwd()
```

**Returns:** `str`

**Example**

```python
print(os.getcwd())
```

**Real-world Uses**
- Display current project location
- CLI applications

---

## 2. os.chdir()

**Purpose:** Changes the current working directory.

**Syntax**

```python
os.chdir(path)
```

**Parameters:** `path`

**Example**

```python
os.chdir("Documents")
```

> ⚠️ Make sure the directory exists before changing it.

---

## 3. os.listdir()

**Purpose:** Lists files and folders in a directory.

**Syntax**

```python
os.listdir(path=".")
```

**Returns:** `list`

**Example**

```python
print(os.listdir())
```

**Real-world Uses**
- File managers
- Backup utilities
- Directory scanners

---

## 4. os.mkdir()

**Purpose:** Creates a single directory.

**Syntax**

```python
os.mkdir(path)
```

**Example**

```python
os.mkdir("Projects")
```

---

## 5. os.makedirs()

**Purpose:** Creates multiple nested directories.

**Syntax**

```python
os.makedirs(path)
```

**Example**

```python
os.makedirs("Python/Projects/OS")
```

---

## 6. os.rename()

**Purpose:** Renames a file or folder.

**Syntax**

```python
os.rename(old_name, new_name)
```

**Example**

```python
os.rename("old.txt", "new.txt")
```

---

## 7. os.remove()

**Purpose:** Deletes a file.

**Syntax**

```python
os.remove(path)
```

**Example**

```python
os.remove("notes.txt")
```

> ⚠️ Deletes the file permanently.

---

## 8. os.rmdir()

**Purpose:** Deletes an empty directory.

**Syntax**

```python
os.rmdir(path)
```

**Example**

```python
os.rmdir("Projects")
```

> ⚠️ Works only for empty folders.

---

## 9. os.removedirs()

**Purpose:** Removes nested empty directories.

**Syntax**

```python
os.removedirs(path)
```

**Example**

```python
os.removedirs("Python/Projects/OS")
```

---

## 10. os.path.exists()

**Purpose:** Checks whether a path exists.

**Syntax**

```python
os.path.exists(path)
```

**Returns:** `True` or `False`

**Example**

```python
os.path.exists("notes.txt")
```

---

## 11. os.path.isfile()

**Purpose:** Checks whether the path is a file.

**Syntax**

```python
os.path.isfile(path)
```

**Example**

```python
os.path.isfile("notes.txt")
```

---

## 12. os.path.isdir()

**Purpose:** Checks whether the path is a directory.

**Syntax**

```python
os.path.isdir(path)
```

**Example**

```python
os.path.isdir("Projects")
```

---

## 13. os.path.join()

**Purpose:** Joins paths safely across operating systems.

**Syntax**

```python
os.path.join(path1, path2)
```

**Example**

```python
os.path.join("Projects", "notes.txt")
```

> 💡 Always prefer `os.path.join()` over manually using `/` or `\`.

---

## 14. os.environ

**Purpose:** Accesses environment variables.

**Example**

```python
print(os.environ.get("USERNAME"))
```

**Real-world Uses**
- API keys
- Configuration settings
- User information

---

# Comparison

## mkdir() vs makedirs()

| mkdir() | makedirs() |
|----------|------------|
| Creates one folder | Creates nested folders |

---

## remove() vs rmdir()

| remove() | rmdir() |
|-----------|----------|
| Deletes files | Deletes empty folders |

---

## isfile() vs isdir()

| isfile() | isdir() |
|-----------|----------|
| Checks for files | Checks for directories |

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `getcwd()` | Current directory |
| `chdir()` | Change directory |
| `listdir()` | List files/folders |
| `mkdir()` | Create folder |
| `makedirs()` | Create nested folders |
| `rename()` | Rename file/folder |
| `remove()` | Delete file |
| `rmdir()` | Delete empty folder |
| `removedirs()` | Delete nested folders |
| `exists()` | Check path exists |
| `isfile()` | Check file |
| `isdir()` | Check directory |
| `join()` | Join paths |
| `environ` | Environment variables |

---

# Best Practices

- Use `os.path.join()` for cross-platform paths.
- Check with `exists()` before deleting files.
- Handle file operations using `try-except`.
- Keep file operations inside a dedicated workspace.

---

# Common Mistakes

- Hardcoding file paths.
- Deleting files without checking existence.
- Using `rmdir()` on non-empty folders.
- Forgetting to close opened files.

---

# Safety Notes

> ⚠️ Always test file operations inside a practice folder.
> ⚠️ Avoid deleting important files directly.
> ⚠️ Use `exists()` before `remove()` or `rmdir()`.

---

# When Should I Use This Module?

✅ **Use `os` when:**

- Managing files and folders
- Automating file operations
- Accessing environment variables
- Building command-line tools

❌ **Avoid `os` when:**

- You only need modern path manipulation.

➡ **Better Alternatives**

- `pathlib` → Modern path handling
- `shutil` → Copying and moving files
- `glob` → Searching files using patterns

---