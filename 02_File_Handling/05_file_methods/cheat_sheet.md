# File Methods — Cheat Sheet

## File Methods

| Method | Purpose |
|---------|---------|
| `close()` | Close the file |
| `closed` | Check if file is closed |
| `flush()` | Save buffered data immediately |
| `truncate(n)` | Shorten the file |
| `readable()` | Check if file can be read |
| `writable()` | Check if file can be written |
| `seekable()` | Check if file pointer can move |
| `fileno()` | Return file descriptor |
| `isatty()` | Check if file is connected to terminal |

---

## `close()`

```python
file.close()
```

Closes the file.

---

## `closed`

```python
print(file.closed)
```

Output:

```text
False
```

After closing:

```python
file.close()
print(file.closed)
```

Output:

```text
True
```

---

## `flush()`

```python
file.write("Python")
file.flush()
```

Immediately saves buffered data to the file.

---

## `truncate()`

```python
file.truncate(6)
```

Example:

```text
Before : Python Programming
After  : Python
```

---

## `readable()`

```python
file.readable()
```

Returns:

```text
True / False
```

---

## `writable()`

```python
file.writable()
```

Returns:

```text
True / False
```

---

## `seekable()`

```python
file.seekable()
```

Returns:

```text
True / False
```

---

## `fileno()`

```python
file.fileno()
```

Returns the operating system's file descriptor.

---

## `isatty()`

```python
file.isatty()
```

Returns:

```text
True / False
```

Usually `False` for normal files.

---

## Quick Revision

```text
close()      → Close file
closed       → File status
flush()      → Save immediately
truncate()   → Shorten file
readable()   → Can read?
writable()   → Can write?
seekable()   → Can move pointer?
fileno()     → File descriptor
isatty()     → Terminal check
```

---

## Key Points

- `with open()` closes files automatically.
- `flush()` writes buffered data immediately.
- `truncate()` removes content after a specified size.
- `readable()`, `writable()`, and `seekable()` return Boolean values.
- `fileno()` returns an integer.
- `isatty()` is usually `False` for files.