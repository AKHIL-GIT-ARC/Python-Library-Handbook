# File Methods in Python

Python provides several built-in methods to perform operations on file objects.
These methods help in checking file properties, managing file contents, and controlling file behavior.

---

## Common File Methods

| Method | Purpose |
|---------|---------|
| `close()` | Close the file |
| `flush()` | Save buffered data immediately |
| `truncate()` | Remove file content after a given size |
| `readable()` | Check if file can be read |
| `writable()` | Check if file can be written |
| `seekable()` | Check if file pointer can move |
| `fileno()` | Return file descriptor |
| `isatty()` | Check if file is connected to a terminal |
| `closed` | Check whether file is closed |

---

## close()

Closes an open file.

```python
file = open("notes.txt", "r")
file.close()
```
Always close files if you are not using `with open()`.

---

## closed

Checks whether a file is closed.

```python
file = open("notes.txt", "r")
print(file.closed)
file.close()
print(file.closed)
```
Output:

```text
False
True
```
---

## flush()

Writes buffered data immediately to the file.

```python
with open("notes.txt", "w") as file:
    file.write("Python")
    file.flush()
```

Useful when data must be saved immediately.

---

## truncate()

Removes file content after a specified position.

```python
with open("notes.txt", "r+") as file:
    file.truncate(6)
```

If the file contains:

```text
Python Programming
```

After:

```python
file.truncate(6)
```

Result:

```text
Python
```

---

## readable()

Checks whether the file supports reading.

```python
with open("notes.txt", "r") as file:
    print(file.readable())
```

Output:

```text
True
```

---

## writable()

Checks whether the file supports writing.

```python
with open("notes.txt", "w") as file:
    print(file.writable())
```

Output:

```text
True
```

---

## seekable()

Checks whether the file pointer can be moved using `seek()`.

```python
with open("notes.txt", "r") as file:
    print(file.seekable())
```

Output:

```text
True
```

---

## fileno()

Returns the file descriptor (an integer used internally by the operating system).

```python
with open("notes.txt", "r") as file:
    print(file.fileno())
```

Output:

```text
3
```
*(The actual number may vary.)*

---

## isatty()

Checks whether the file is connected to a terminal.

```python
with open("notes.txt", "r") as file:
    print(file.isatty())
```

Output:

```text
False
```

---

## Quick Revision

| Method | Returns |
|---------|---------|
| `close()` | Closes file |
| `closed` | `True` / `False` |
| `flush()` | Saves buffered data |
| `truncate(n)` | Shortens file |
| `readable()` | `True` / `False` |
| `writable()` | `True` / `False` |
| `seekable()` | `True` / `False` |
| `fileno()` | File descriptor |
| `isatty()` | `True` / `False` |

---

## Key Points

- `with open()` automatically closes files.
- `flush()` forces pending data to be written.
- `truncate()` reduces file size.
- `readable()`, `writable()`, and `seekable()` return Boolean values.
- `fileno()` returns the OS file descriptor.
- `isatty()` is usually `False` for normal files.