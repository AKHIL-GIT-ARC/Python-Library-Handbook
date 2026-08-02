# File Methods — Interview Questions

## 1. What does `close()` do?

It closes the file and releases system resources.

```python
file.close()
```

---

## 2. What is `file.closed`?

It checks whether a file is closed.

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

## 3. What is `flush()`?

`flush()` immediately writes buffered data to the file.

```python
with open("notes.txt", "w") as file:
    file.write("Python")
    file.flush()
```

---

## 4. What is `truncate()`?

It reduces the file size to the specified number of bytes.

```python
with open("notes.txt", "r+") as file:
    file.truncate(6)
```

Example:

```text
Before : Python Programming
After  : Python
```

---

## 5. What does `readable()` return?

It checks whether the file supports reading.

```python
with open("notes.txt", "r") as file:
    print(file.readable())
```

Output:

```text
True
```

---

## 6. What does `writable()` return?

It checks whether the file supports writing.

```python
with open("notes.txt", "w") as file:
    print(file.writable())
```

Output:

```text
True
```

---

## 7. What does `seekable()` return?

It checks whether the file pointer can be moved using `seek()`.

```python
with open("notes.txt", "r") as file:
    print(file.seekable())
```

Output:

```text
True
```

---

## 8. What is `fileno()`?

It returns the operating system's file descriptor.

```python
with open("notes.txt", "r") as file:
    print(file.fileno())
```

Output:

```text
3
```

*The number may vary.*

---

## 9. What is `isatty()`?

It checks whether the file is connected to a terminal.

```python
with open("notes.txt", "r") as file:
    print(file.isatty())
```

Output:

```text
False
```

---

## 10. Why is `with open()` preferred?

Because it automatically closes the file.

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

No need to call:

```python
file.close()
```

---

## Quick Revision

```text
close()      → Close file
closed       → Check file status
flush()      → Save immediately
truncate()   → Shorten file
readable()   → Can read?
writable()   → Can write?
seekable()   → Can move pointer?
fileno()     → File descriptor
isatty()     → Terminal check
```