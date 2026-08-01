# File Modes — Cheat Sheet

## File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read |
| `w` | Write (Overwrite) |
| `a` | Append |
| `x` | Create New File |
| `r+` | Read & Write |
| `w+` | Write & Read (Overwrite) |
| `a+` | Append & Read |
| `t` | Text Mode (Default) |
| `b` | Binary Mode |

---

## `r` – Read

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

- File must exist.
- Read only.

---

## `w` – Write

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

- Creates file if needed.
- Overwrites existing content.

---

## `a` – Append

```python
with open("notes.txt", "a") as file:
    file.write("\nJava")
```

- Adds data at the end.
- Keeps existing content.

---

## `x` – Create

```python
with open("new.txt", "x") as file:
    file.write("Hello")
```

- Creates a new file.
- Raises `FileExistsError` if the file exists.

---

## `r+`

```python
with open("notes.txt", "r+") as file:
    print(file.read())
    file.write("\nPython")
```

- Read and write.
- File must exist.

---

## `w+`

```python
with open("notes.txt", "w+") as file:
    file.write("Python")
    file.seek(0)
    print(file.read())
```

- Read and write.
- Clears existing content.

---

## `a+`

```python
with open("notes.txt", "a+") as file:
    file.write("\nJava")
    file.seek(0)
    print(file.read())
```

- Read and append.
- Existing content is preserved.

---

## Text & Binary Modes

Text Mode:

```python
open("notes.txt", "rt")
```

Binary Mode:

```python
open("image.jpg", "rb")
```

---

## Quick Comparison

| Mode | Read | Write | Create | Overwrite |
|------|:----:|:-----:|:------:|:---------:|
| `r` | ✅ | ❌ | ❌ | ❌ |
| `w` | ❌ | ✅ | ✅ | ✅ |
| `a` | ❌ | ✅ | ✅ | ❌ |
| `x` | ❌ | ✅ | ✅ | ❌ |
| `r+` | ✅ | ✅ | ❌ | ❌ |
| `w+` | ✅ | ✅ | ✅ | ✅ |
| `a+` | ✅ | ✅ | ✅ | ❌ |

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

---

## Key Points

- `r` requires the file to exist.
- `w` deletes existing content.
- `a` keeps existing content.
- `x` creates a file only if it doesn't exist.
- `r+`, `w+`, and `a+` support both reading and writing.
- `t` is the default mode.
- `b` is used for binary files (images, videos, PDFs).