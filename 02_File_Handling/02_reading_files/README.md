# Reading Files in Python

Python provides several methods to read data from files.

## Open a File

Use `open()` with `"r"` mode:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

`with` automatically closes the file after use.

---

## read()

Reads the remaining content of a file.

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```

Read only a limited number of characters:

```python
content = file.read(6)
```

---

## readline()

Reads one line at a time.

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    line = file.readline()
print(line)
```

Calling it again reads the next line.

---

## readlines()

Reads the remaining lines into a list.

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)
```

Example:

```python
['Python\n', 'Java\n', 'C++\n']
```

---

## Read Line by Line

A file can be directly iterated:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

This is preferred when processing large files line by line.

---

## File Position

Reading moves the current file position.

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read(6))
    print(file.read(4))
```

The second `read()` continues from where the first one stopped.

---

## tell()

Returns the current stream position.

```python
print(file.tell())
```

Think:

```text
tell() → Where am I?
```

---

## seek()

Changes the stream position.

```python
file.seek(0)
```

`seek(0)` returns to the beginning.

Example:

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    print(file.read(6))
    file.seek(0)
    print(file.read(6))
```

---

## Remove Newline

Lines often contain `\n`.

```python
line = line.strip()
```

Example:

```python
for line in file:
    print(line.strip())
```

---

## Methods Summary

| Method | Purpose |
|---|---|
| `read()` | Read remaining content |
| `read(n)` | Read up to `n` characters |
| `readline()` | Read one line |
| `readlines()` | Read lines into a list |
| `for line in file` | Process line by line |
| `tell()` | Get current position |
| `seek(0)` | Return to beginning |

## Key Points

- Use `"r"` mode for reading.
- The file must exist when using `"r"`.
- `read()` returns a string in text mode.
- `readlines()` returns a list.
- Reading advances the file position.
- Use `seek(0)` to return to the beginning.
- Prefer iteration for large files.
- Use `with open()` for automatic closing.