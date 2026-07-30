# Reading Files — Interview Questions

## 1. How do you read a file in Python?

Use `open()` with `"r"` mode.

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

---

## 2. What is the difference between `read()`, `readline()`, and `readlines()`?

| Method | Purpose | Returns |
|---|---|---|
| `read()` | Reads remaining content | String |
| `readline()` | Reads one line | String |
| `readlines()` | Reads remaining lines | List |

---

## 3. What does `read(n)` do?

Reads up to `n` characters in text mode.

```python
content = file.read(10)
```

---

## 4. What happens if you call `read()` twice?

The first `read()` moves the file position to the end.

```python
first = file.read()
second = file.read()
```

`second` normally returns:

```python
""
```

because there is nothing left to read.

---

## 5. What is `tell()`?

`tell()` returns the current stream position.

```python
position = file.tell()
```

---

## 6. What is `seek()`?

`seek()` changes the stream position.

```python
file.seek(0)
```

`seek(0)` moves back to the beginning.

---

## 7. How do you read a file line by line?

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

---

## 8. Why is line-by-line reading useful?

It allows files to be processed incrementally instead of loading the entire file into memory at once.
This is useful for large files.

---

## 9. Why is `with open()` preferred?

It automatically closes the file when the block ends.

```python
with open("sample.txt", "r") as file:
    content = file.read()
```

---

## 10. What happens if a file doesn't exist in `r` mode?

Python raises:

```text
FileNotFoundError
```

It can be handled using:

```python
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

---

## Quick Revision

```text
read()       → Remaining content
read(n)      → Limited content
readline()   → One line
readlines()  → List of lines
tell()       → Current position
seek(0)      → Beginning of file
strip()      → Remove surrounding whitespace
```