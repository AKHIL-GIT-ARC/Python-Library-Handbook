# File Modes — Interview Questions

## 1. What are file modes in Python?

File modes specify how a file should be opened.

Example:

```python
open("notes.txt", "r")
```

---

## 2. What is the difference between `r`, `w`, and `a`?

| Mode | Purpose |
|------|---------|
| `r` | Read existing file |
| `w` | Write (Overwrite) |
| `a` | Append data |

---

## 3. What happens if you open a file in `r` mode and the file doesn't exist?

Python raises:

```text
FileNotFoundError
```

---

## 4. What happens if you open a file in `w` mode?

- Creates the file if it doesn't exist.
- Overwrites existing content.

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

---

## 5. What is append mode (`a`)?

It adds new data to the end of a file without deleting existing content.

```python
with open("notes.txt", "a") as file:
    file.write("\nJava")
```

---

## 6. What is `x` mode?

Creates a new file.
If the file already exists:

```text
FileExistsError
```

---

## 7. What is the difference between `r+`, `w+`, and `a+`?

| Mode | Description |
|------|-------------|
| `r+` | Read and write (file must exist) |
| `w+` | Read and write (overwrites file) |
| `a+` | Read and append |

---

## 8. What is the difference between text mode and binary mode?

| Mode | Used For |
|------|----------|
| `t` | Text files |
| `b` | Binary files (images, videos, PDFs) |

Example:

```python
open("photo.jpg", "rb")
```

---

## 9. Why is `seek(0)` used with `w+` or `a+`?

After writing, the file pointer is at the end.
`seek(0)` moves it back to the beginning so the data can be read.

```python
file.seek(0)
```

---

## 10. Which mode should you use?

| Situation | Mode |
|-----------|------|
| Read a file | `r` |
| Create or overwrite | `w` |
| Add new data | `a` |
| Create only if absent | `x` |
| Read & Write | `r+` |
| Write & Read | `w+` |
| Append & Read | `a+` |

---

## Quick Revision

```text
r   → Read
w   → Write / Overwrite
a   → Append
x   → Create New

r+  → Read + Write
w+  → Write + Read
a+  → Append + Read

t   → Text Mode
b   → Binary Mode
```