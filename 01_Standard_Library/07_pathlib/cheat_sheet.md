# Pathlib Module Cheat Sheet

## Import

```python
from pathlib import Path
```

The `pathlib` module provides an object-oriented way to work with file and directory paths. It is the modern replacement for many `os.path` operations.

---

## 1. Path()

**Purpose:** Creates a Path object.

**Syntax**

```python
Path(path)
```

**Example**

```python
path = Path("notes.txt")
```

**Real-world Uses**
- File management
- Directory operations
- Path manipulation

> 💡 **Interview Tip:** Almost every operation in `pathlib` starts with a `Path` object.

---

## 2. Path.cwd()

**Purpose:** Returns the current working directory.

**Syntax**

```python
Path.cwd()
```

**Returns:** `Path`

**Example**

```python
print(Path.cwd())
```

---

## 3. Path.home()

**Purpose:** Returns the current user's home directory.

**Syntax**

```python
Path.home()
```

**Example**

```python
print(Path.home())
```

---

## 4. exists()

**Purpose:** Checks whether a file or folder exists.

**Syntax**

```python
path.exists()
```

**Returns:** `bool`

**Example**

```python
path = Path("notes.txt")
print(path.exists())
```

---

## 5. is_file()

**Purpose:** Checks whether the path is a file.

**Syntax**

```python
path.is_file()
```

**Example**

```python
path.is_file()
```

---

## 6. is_dir()

**Purpose:** Checks whether the path is a directory.

**Syntax**

```python
path.is_dir()
```

**Example**

```python
path.is_dir()
```

---

## 7. mkdir()

**Purpose:** Creates a directory.

**Syntax**

```python
path.mkdir()
```

**Example**

```python
Path("Projects").mkdir()
```

---

## 8. rename()

**Purpose:** Renames a file or folder.

**Syntax**

```python
path.rename(new_path)
```

**Example**

```python
old.rename(new)
```

---

## 9. unlink()

**Purpose:** Deletes a file.

**Syntax**

```python
path.unlink()
```

**Example**

```python
Path("notes.txt").unlink()
```

> ⚠️ Permanently deletes the file.

---

## 10. rmdir()

**Purpose:** Deletes an empty directory.

**Syntax**

```python
path.rmdir()
```

**Example**

```python
Path("Projects").rmdir()
```

> ⚠️ Works only for empty folders.

---

## 11. iterdir()

**Purpose:** Iterates through files and folders inside a directory.

**Syntax**

```python
path.iterdir()
```

**Example**

```python
for item in Path("practice_files").iterdir():
    print(item.name)
```

---

## 12. glob()

**Purpose:** Searches files matching a pattern.

**Syntax**

```python
path.glob(pattern)
```

**Example**

```python
Path("practice_files").glob("*.txt")
```

**Common Patterns**

| Pattern | Meaning |
|----------|---------|
| `*.txt` | All text files |
| `*.py` | All Python files |
| `*` | Everything |

---

## 13. rglob()

**Purpose:** Searches recursively through all subdirectories.

**Syntax**

```python
path.rglob(pattern)
```

**Example**

```python
Path("practice_files").rglob("*.py")
```

---

## 14. name

**Purpose:** Returns the filename.

**Example**

```python
Path("notes.txt").name
```

**Output**

```
notes.txt
```

---

## 15. stem

**Purpose:** Returns the filename without extension.

**Example**

```python
Path("notes.txt").stem
```

**Output**

```
notes
```

---

## 16. suffix

**Purpose:** Returns the file extension.

**Example**

```python
Path("notes.txt").suffix
```

**Output**

```
.txt
```

---

## 17. parent

**Purpose:** Returns the parent directory.

**Example**

```python
Path("Documents/notes.txt").parent
```

**Output**

```
Documents
```

---

## 18. touch()

**Purpose:** Creates an empty file.

**Syntax**

```python
path.touch()
```

**Example**

```python
Path("notes.txt").touch()
```

---

## 19. stat()

**Purpose:** Returns file metadata.

**Syntax**

```python
path.stat()
```

**Example**

```python
size = Path("notes.txt").stat().st_size
print(size)
```

**Common Uses**
- File size
- Last modified time
- File information

---

# Migration from os

| os | pathlib |
|----|----------|
| `os.getcwd()` | `Path.cwd()` |
| `os.path.exists()` | `Path.exists()` |
| `os.path.isfile()` | `Path.is_file()` |
| `os.path.isdir()` | `Path.is_dir()` |
| `os.listdir()` | `Path.iterdir()` |
| `os.mkdir()` | `Path.mkdir()` |
| `os.remove()` | `Path.unlink()` |
| `os.rmdir()` | `Path.rmdir()` |
| `os.rename()` | `Path.rename()` |
| `os.path.join()` | `Path() / "file"` |

---

# Frequently Used Methods

| Method | Purpose |
|---------|---------|
| `Path()` | Create path object |
| `cwd()` | Current directory |
| `home()` | Home directory |
| `exists()` | Path exists |
| `is_file()` | Check file |
| `is_dir()` | Check folder |
| `mkdir()` | Create folder |
| `rename()` | Rename |
| `unlink()` | Delete file |
| `rmdir()` | Delete folder |
| `iterdir()` | List contents |
| `glob()` | Search files |
| `rglob()` | Recursive search |
| `touch()` | Create empty file |
| `stat()` | File information |

---

# Best Practices

- Use `Path` objects instead of string paths.
- Prefer `pathlib` over `os.path` in new projects.
- Use `/` instead of manually joining paths.
- Check `exists()` before deleting files.
- Use `glob()` for searching files.

---

# Common Mistakes

- Mixing `Path` objects with strings.
- Calling `unlink()` on a directory.
- Calling `rmdir()` on a non-empty folder.
- Forgetting to check `exists()` before file operations.

---

# When Should I Use This Module?

✅ **Use `pathlib` when:**
- Working with files and folders
- Building automation scripts
- Creating CLI tools
- Managing project directories
- Writing modern Python applications

❌ **Avoid `pathlib` when:**
- You need low-level operating system functionality.

➡ **Better Alternatives**
- `os` → OS-level operations
- `shutil` → Copying and moving files
- `glob` → File searching (though `Path.glob()` often replaces it)

---
# Quick Revision

| Need | Method |
|------|--------|
| Create Path | `Path()` |
| Current Directory | `cwd()` |
| Home Directory | `home()` |
| Check Exists | `exists()` |
| Check File | `is_file()` |
| Check Folder | `is_dir()` |
| Create Folder | `mkdir()` |
| Rename | `rename()` |
| Delete File | `unlink()` |
| Delete Folder | `rmdir()` |
| List Files | `iterdir()` |
| Search Files | `glob()` |
| Recursive Search | `rglob()` |
| File Name | `name` |
| File Name Without Extension | `stem` |
| File Extension | `suffix` |
| Parent Folder | `parent` |
| Create Empty File | `touch()` |
| File Metadata | `stat()` |