# Writing Files — Cheat Sheet

## Write Mode — `w`

Creates a file or overwrites existing content.

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python")
```

```text
w → Write / Overwrite
```

---

## Append Mode — `a`

Adds content without deleting existing data.

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("\nFile Handling")
```

```text
a → Add to End
```

---

## `write()`

Writes a single string.

```python
file.write("Python")
```

It does not add a newline automatically.

```python
file.write("Python\n")
file.write("Java\n")
```

---

## `writelines()`

Writes multiple strings.

```python
languages = [
    "Python\n",
    "Java\n",
    "C++\n"
]
file.writelines(languages)
```

`writelines()` does not add `\n` automatically.

---

## Writing Variables

```python
name = "Akhil"
marks = 90
file.write(f"Name: {name}\n")
file.write(f"Marks: {marks}")
```

`write()` expects strings.

```python
file.write(str(90))
```

---

## `w` vs `a` vs `x`

| Mode | Purpose | Existing Content |
|---|---|---|
| `w` | Write | Cleared |
| `a` | Append | Preserved |
| `x` | Create new file | Error if file exists |

---

## Quick Revision

```text
write()       → Write one string
writelines()  → Write multiple strings
w              → Write / Overwrite
a              → Append
x              → Create only
\n             → New line
str()          → Convert value to string
```

## Key Points

- `w` can erase existing content.
- `a` preserves existing content.
- `write()` and `writelines()` don't add newlines automatically.
- Use `\n` when needed.
- Convert numbers and other non-string values before writing.
- Prefer `with open()` for automatic closing.