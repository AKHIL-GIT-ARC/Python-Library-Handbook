# Writing Files in Python

Writing files allows Python programs to store data permanently in a file.

The two main modes are:

```text
w → Write / Overwrite
a → Append
```

---

## Write Mode — `w`

`"w"` opens a file for writing.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python")
```

If the file:

- Does not exist → Python creates it.
- Already exists → Existing content is cleared.

---

## `write()`

`write()` writes a string to a file.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python")
```

Result:

```text
Python
```

`write()` does **not** automatically add a new line.

```python
file.write("Python")
file.write("Java")
```

Result:

```text
PythonJava
```

Use `\n`:

```python
file.write("Python\n")
file.write("Java\n")
```

Result:

```text
Python
Java
```

---

## Writing Variables

Use f-strings to write variable values.

```python
name = "Akhil"
marks = 90

with open("student.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Marks: {marks}")
```

---

## `writelines()`

`writelines()` writes multiple strings.

```python
languages = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(languages)
```

Result:

```text
Python
Java
C++
```

`writelines()` also **does not add `\n` automatically**.

---

## Append Mode — `a`

`"a"` adds new data to the end of a file.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nFile Handling")
```

Existing content is preserved.

```text
Before:
Python

After:
Python
File Handling
```

---

## `w` vs `a`

| Mode | Creates File | Existing Content |
|---|---|---|
| `w` | Yes | Cleared |
| `a` | Yes | Preserved |
| `x` | Yes | Fails if file exists |

Use:

```text
w → Replace content
a → Add content
x → Create without overwriting
```

---

## Writing Numbers

`write()` expects a string.

Incorrect:

```python
marks = 90
file.write(marks)
```

Correct:

```python
file.write(str(marks))
```

or:

```python
file.write(f"{marks}")
```

---

## Key Points

- `write()` writes one string.
- `writelines()` writes multiple strings.
- Neither adds newlines automatically.
- `"w"` can erase existing content.
- `"a"` preserves existing content.
- `"w"` and `"a"` create the file if needed.
- Convert non-string values before using `write()`.
- Prefer `with open()` for automatic file closing.
- Use `encoding="utf-8"` for text files when appropriate.

---

## Quick Revision

| Need | Use |
|---|---|
| Write/overwrite | `"w"` |
| Append | `"a"` |
| Write string | `write()` |
| Write multiple strings | `writelines()` |
| New line | `\n` |
| Convert value | `str()` |
| Automatic closing | `with open()` |