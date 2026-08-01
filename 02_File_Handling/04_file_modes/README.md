# File Modes in Python

File modes tell Python **how a file should be opened**.

Syntax:

```python
open(filename, mode)
```

Example:

```python
with open("notes.txt", "r") as file:
    content = file.read()
```

---

## File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read |
| `w` | Write (Overwrite) |
| `a` | Append |
| `x` | Create New File |
| `r+` | Read & Write |
| `w+` | Read & Write (Overwrite) |
| `a+` | Read & Append |
| `t` | Text Mode (Default) |
| `b` | Binary Mode |

---

## Read Mode (`r`)

- Opens an existing file.
- Used only for reading.
- File must exist.

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

## Write Mode (`w`)

- Creates a new file if it doesn't exist.
- Overwrites existing content.

```python
with open("notes.txt", "w") as file:
    file.write("Hello Python")
```

---

## Append Mode (`a`)

- Adds data to the end of a file.
- Existing content is preserved.

```python
with open("notes.txt", "a") as file:
    file.write("\nNew Line")
```

---

## Create Mode (`x`)

- Creates a new file.
- Raises `FileExistsError` if the file already exists.

```python
with open("new_file.txt", "x") as file:
    file.write("Created Successfully")
```

---

## Read & Write Mode (`r+`)

- Read and write using the same file.
- File must already exist.

```python
with open("notes.txt", "r+") as file:
    print(file.read())
    file.write("\nPython")
```

---

## Write & Read Mode (`w+`)

- Creates a new file if needed.
- Clears existing content.
- Allows both reading and writing.

```python
with open("notes.txt", "w+") as file:
    file.write("Python")
    file.seek(0)
    print(file.read())
```

---

## Append & Read Mode (`a+`)

- Appends new data.
- Reading is also allowed.
- Existing content is not removed.

```python
with open("notes.txt", "a+") as file:
    file.write("\nJava")
    file.seek(0)
    print(file.read())
```

---

## Text Mode (`t`)

Works with text files.

```python
open("notes.txt", "rt")
```
 
`"r"` is the same as `"rt"` because text mode is the default.

---

## Binary Mode (`b`)

Used for binary files like images, videos, and PDFs.

```python
with open("photo.jpg", "rb") as file:
    data = file.read()
```

---

## Mode Comparison

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

## Key Points

- `r` → Read only.
- `w` → Write and overwrite.
- `a` → Append to the end.
- `x` → Create a new file only.
- `r+` → Read and write.
- `w+` → Read, write, and overwrite.
- `a+` → Read and append.
- `t` → Text mode.
- `b` → Binary mode.

---

## Quick Revision

| Need | Mode |
|------|------|
| Read file | `r` |
| Write file | `w` |
| Append data | `a` |
| Create new file | `x` |
| Read & Write | `r+` |
| Write & Read | `w+` |
| Append & Read | `a+` |
| Text file | `t` |
| Binary file | `b` |