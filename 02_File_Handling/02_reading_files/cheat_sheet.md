# Reading Files — Cheat Sheet

## Open a File

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

`"r"` → Read mode.

---

## Reading Methods

### `read()`

Reads all remaining content.

```python
content = file.read()
```

### `read(n)`

Reads up to `n` characters.

```python
content = file.read(10)
```

### `readline()`

Reads one line.

```python
line = file.readline()
```

### `readlines()`

Reads remaining lines into a list.

```python
lines = file.readlines()
```

---

## Read Line by Line

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```
Preferred for large files because lines can be processed one at a time.

---

## Remove Newline

```python
line.strip()
```

Example:

```python
"Python\n" → "Python"
```

---

## File Position

### `tell()`

Returns the current stream position.

```python
position = file.tell()
```

### `seek()`

Moves the stream position.

```python
file.seek(0)
```

`seek(0)` → return to the beginning.

---

## Line Numbers

```python
for number, line in enumerate(file, start=1):
    print(number, line.strip())
```

---

## Quick Comparison

| Method | Purpose | Returns |
|---|---|---|
| `read()` | Read remaining content | `str` |
| `read(n)` | Read limited content | `str` |
| `readline()` | Read one line | `str` |
| `readlines()` | Read remaining lines | `list` |
| `tell()` | Current position | position value |
| `seek(0)` | Move to beginning | — |

## Key Points

- Use `"r"` to read files.
- `r` requires the file to exist.
- Reading advances the file position.
- `seek(0)` returns to the beginning.
- `readlines()` stores lines in a list.
- Prefer `for line in file` for line-by-line processing.
- Use `with open()` for automatic closing.