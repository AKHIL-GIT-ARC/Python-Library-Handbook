# Glob Module Interview Questions

## Beginner Level

### 1. What is the `glob` module?

**Answer:**

The `glob` module is a built-in Python library used to search for files and directories using wildcard patterns.

---

### 2. How do you import the `glob` module?

```python
import glob
```

---

### 3. Which function returns a list of matching files?

**Answer**

```python
glob.glob(pattern)
```

---

### 4. Which function returns an iterator instead of a list?

**Answer**

```python
glob.iglob(pattern)
```

---

### 5. What is the purpose of wildcard patterns?

**Answer**

Wildcard patterns help search files based on names or extensions without specifying the exact filename.

Example:

```python
glob.glob("*.py")
```

---

## Intermediate Level

### 6. What does `*` represent?

**Answer**

Matches any number of characters.

Example:

```python
glob.glob("*.txt")
```

---

### 7. What does `?` represent?

**Answer**

Matches exactly one character.

Example:

```python
glob.glob("file?.txt")
```

Matches:

```
file1.txt
fileA.txt
```

Does not match:

```
file10.txt
```

---

### 8. What does `[]` represent?

**Answer**

Matches a character set or range.

Example:

```python
glob.glob("[ab]*.txt")
```

Matches files starting with **a** or **b**.

---

### 9. What does `**` represent?

**Answer**

Searches recursively through subdirectories.

Example:

```python
glob.glob("**/*.py", recursive=True)
```

---

### 10. Why is `recursive=True` required?

**Answer**

Without `recursive=True`, the `**` wildcard will not search subdirectories.

---

## Advanced Level

### 11. Difference between `glob()` and `iglob()`?

| `glob()` | `iglob()` |
|-----------|------------|
| Returns a list | Returns an iterator |
| Uses more memory | Memory efficient |
| Suitable for small searches | Better for large searches |

---

### 12. Difference between `glob` and `pathlib.Path.glob()`?

| `glob` | `pathlib` |
|----------|-----------|
| Returns strings | Returns `Path` objects |
| Functional approach | Object-oriented approach |

---

### 13. Why is `iglob()` more memory-efficient?

**Answer**

Because it generates one result at a time instead of loading all matches into memory.

---

### 14. Can `glob` search file contents?

**Answer**

No.

It only searches filenames and directory paths.

---

### 15. Why is `glob` useful in automation?

**Answer**

Because it can automatically locate files based on patterns without knowing their exact names.

---

## Scenario-Based Questions

### 16. You need to process every Python file in a project. Which pattern will you use?

**Answer**

```python
glob.glob("**/*.py", recursive=True)
```

---

### 17. You need to find every text file in the current folder.

**Answer**

```python
glob.glob("*.txt")
```

---

### 18. You need to search only image files.

**Answer**

```python
glob.glob("*.jpg")
glob.glob("*.png")
```

---

### 19. Which function did we use for recursive searching in our mini project?

**Answer**

```python
glob.glob(pattern, recursive=True)
```

---

## Common Coding Questions

### 21. Print all Python files in a folder.

```python
glob.glob("*.py")
```

---

### 22. Print all text files recursively.

```python
glob.glob("**/*.txt", recursive=True)
```

---

### 23. Search files by extension entered by the user.

```python
extension = input()

glob.glob(f"*.{extension}")
```

---

### 24. Print all matching files using an iterator.

```python
glob.iglob("*.py")
```

---

### 25. Count the total number of Python files.

```python
files = glob.glob("**/*.py", recursive=True)

print(len(files))
```

---

# Best Practices

- Use specific wildcard patterns.
- Use `recursive=True` only when needed.
- Use `iglob()` for large directories.
- Prefer `Path.glob()` in modern Python projects.

---

# Quick Revision

| Pattern / Function | Purpose |
|--------------------|---------|
| `glob()` | Search files |
| `iglob()` | Iterator search |
| `*` | Any characters |
| `?` | Single character |
| `[]` | Character set |
| `**` | Recursive search |
| `recursive=True` | Enable recursive search |