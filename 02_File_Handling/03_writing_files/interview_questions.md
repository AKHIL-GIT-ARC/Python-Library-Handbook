# Writing Files — Interview Questions

## 1. How do you write to a file in Python?

Open the file in `"w"` mode and use `write()`.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
```

---

## 2. What happens when a file is opened in `w` mode?

- If the file doesn't exist → it is created.
- If it exists → existing content is cleared.

---

## 3. What is append mode?

`"a"` adds new content to the end without deleting existing content.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("New note\n")
```

---

## 4. What is the difference between `write()` and `writelines()`?

`write()` writes one string:

```python
file.write("Python")
```

`writelines()` writes multiple strings:

```python
file.writelines(["Python\n", "Java\n"])
```

---

## 5. Does `writelines()` add newlines automatically?

No.

```python
file.writelines(["Python\n", "Java\n"])
```

You must include `\n` yourself when needed.

---

## 6. What is the difference between `w` and `a`?

| `w` | `a` |
|---|---|
| Writes/overwrites | Appends |
| Clears existing content | Preserves content |
| Writes from beginning | Writes at end |

---

## 7. Can `write()` directly write an integer?

No. `write()` expects a string in text mode.

```python
marks = 90
file.write(str(marks))
```

or:

```python
file.write(f"{marks}")
```

---

## 8. What does `write()` return?

It returns the number of characters written.

```python
count = file.write("Python")
print(count)
```
Output:
```text
6
```
---

## 9. What is `x` mode?

`"x"` creates a new file.

```python
open("notes.txt", "x")
```

If the file already exists:

```text
FileExistsError
```

---

## 10. Why is `with open()` preferred?

It automatically closes the file after the block finishes.

```python
with open("notes.txt", "w") as file:
    file.write("Python")
```

---

## Quick Revision

```text
w              → Write / Overwrite
a              → Append
x              → Create new
write()        → Write one string
writelines()   → Write multiple strings
\n             → New line
str()          → Convert to string
```