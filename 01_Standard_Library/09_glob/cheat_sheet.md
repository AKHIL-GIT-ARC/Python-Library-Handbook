# Glob Module Cheat Sheet

## Import

```python
import glob
```

The `glob` module is used to search for files and directories using wildcard patterns.

---

## 1. glob.glob()

**Purpose:** Returns a list of files matching a pattern.

**Syntax**

```python
glob.glob(pattern, recursive=False)
```

**Parameters**

- `pattern` → Search pattern
- `recursive` → Enables recursive searching

**Returns:** `list`

**Example**

```python
glob.glob("*.py")
```

**Output**

```text
app.py
test.py
```

**Real-world Uses**

- Find Python files
- Search log files
- Process datasets
- Locate images

---

## 2. glob.iglob()

**Purpose:** Returns an iterator instead of a list.

**Syntax**

```python
glob.iglob(pattern, recursive=False)
```

**Returns:** Iterator

**Example**

```python
for file in glob.iglob("*.py"):
    print(file)
```

> 💡 **Interview Tip:** `iglob()` is more memory-efficient than `glob()` for large directories.

---

# Wildcards

## `*`

Matches any number of characters.

```python
glob.glob("*.py")
```

Matches:

```text
app.py
main.py
test.py
```

---

## `?`

Matches exactly one character.

```python
glob.glob("file?.txt")
```

Matches:

```text
file1.txt
fileA.txt
```

Does NOT match:

```text
file10.txt
```

---

## `[]`

Matches characters inside brackets.

```python
glob.glob("[ab]*.txt")
```

Matches:

```text
apple.txt
book.txt
```

---

## `**`

Searches recursively through subfolders.

```python
glob.glob("**/*.py", recursive=True)
```

---

# Recursive Search

Enable recursive search by setting:

```python
recursive=True
```

Example:

```python
glob.glob("practice_files/**/*.py", recursive=True)
```

---

# Comparison

## glob() vs iglob()

| glob() | iglob() |
|----------|----------|
| Returns a list | Returns an iterator |
| Loads all results into memory | Memory efficient |
| Suitable for small searches | Better for large searches |

---

## glob vs pathlib

| glob | pathlib |
|-------|----------|
| `glob.glob()` | `Path.glob()` |
| Returns strings | Returns `Path` objects |
| Functional style | Object-oriented style |

---

# Common Patterns

| Pattern | Meaning |
|----------|---------|
| `*.py` | Python files |
| `*.txt` | Text files |
| `*.jpg` | JPG images |
| `*.*` | All files |
| `**/*.py` | Recursive Python search |
| `file?.txt` | Single-character match |
| `[ab]*.txt` | Starts with a or b |

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `glob()` | Search files |
| `iglob()` | Iterator search |

---

# Best Practices

- Use specific search patterns.
- Use `recursive=True` only when necessary.
- Use `iglob()` for large directories.
- Prefer `Path.glob()` in modern Python projects.

---

# Common Mistakes

- Forgetting `recursive=True` when using `**`.
- Using incorrect wildcard patterns.
- Expecting `glob()` to read file contents.
- Assuming `glob()` returns `Path` objects.

---

# When Should I Use This Module?

✅ **Use `glob` when:**

- Searching files
- Finding files by extension
- Batch processing
- Automation scripts
- Data preprocessing

❌ **Avoid `glob` when:**

- Reading or writing file contents.
- Performing advanced file operations.

➡ **Better Alternatives**

- `pathlib` → Modern path handling(object oriented approach) and file
   searching
- `os` → Basic level operating system interaction
- `shutil` → High level file operations.Copying and moving files

---

# Quick Revision

| Need | Pattern / Function |
|------|--------------------|
| Search Python Files | `*.py` |
| Search Text Files | `*.txt` |
| Search Images | `*.jpg` |
| Recursive Search | `**` + `recursive=True` |
| Search Files | `glob()` |
| Iterator Search | `iglob()` |
| Single Character | `?` |
| Character Set | `[]` |
| Any Characters | `*` |