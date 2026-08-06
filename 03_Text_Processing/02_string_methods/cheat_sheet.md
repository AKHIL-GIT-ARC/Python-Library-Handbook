# String Methods — Cheat Sheet

## Change Case

### `upper()`

```python
text.upper()
```

Converts all characters to uppercase.

---

### `lower()`

```python
text.lower()
```

Converts all characters to lowercase.

---

### `title()`

```python
text.title()
```

Capitalizes the first letter of every word.

---

### `capitalize()`

```python
text.capitalize()
```

Capitalizes only the first character.

---

### `swapcase()`

```python
text.swapcase()
```

Swaps uppercase and lowercase letters.

---

## Remove Spaces

### `strip()`

```python
text.strip()
```

Removes spaces from both ends.

---

### `lstrip()`

```python
text.lstrip()
```

Removes spaces from the left.

---

### `rstrip()`

```python
text.rstrip()
```

Removes spaces from the right.

---

## Search & Replace

### `replace()`

```python
text.replace("Java", "Python")
```

Replaces a substring.

---

### `find()`

```python
text.find("Python")
```

Returns the first index or `-1` if not found.

---

### `count()`

```python
text.count("Python")
```

Counts occurrences.

---

## Check Beginning & End

### `startswith()`

```python
text.startswith("Python")
```

Returns `True` if the string starts with the given text.

---

### `endswith()`

```python
text.endswith(".")
```

Returns `True` if the string ends with the given text.

---

## Split & Join

### `split()`

```python
text.split(",")
```

Converts a string into a list.

---

### `join()`

```python
", ".join(items)
```

Joins list elements into a string.

---

## Validation Methods

```python
text.isalpha()
text.isdigit()
text.isalnum()
text.islower()
text.isupper()
text.isspace()
```

| Method | Checks |
|---------|--------|
| `isalpha()` | Letters only |
| `isdigit()` | Digits only |
| `isalnum()` | Letters & digits |
| `islower()` | Lowercase |
| `isupper()` | Uppercase |
| `isspace()` | Whitespaces only |

---

## Quick Revision

```text
upper()        → Uppercase
lower()        → Lowercase
title()        → Title Case
capitalize()   → First letter uppercase
swapcase()     → Swap letter case

strip()        → Remove spaces
lstrip()       → Remove left spaces
rstrip()       → Remove right spaces

replace()      → Replace text
find()         → Find index
count()        → Count occurrences

startswith()   → Starts with?
endswith()     → Ends with?

split()        → String → List
join()         → List → String

isalpha()      → Letters only
isdigit()      → Digits only
isalnum()      → Letters & digits
islower()      → Lowercase?
isupper()      → Uppercase?
isspace()      → Spaces only
```

---

## Key Points

- String methods return a **new string**.
- Strings are **immutable**.
- `find()` returns `-1` if the text is not found.
- `split()` returns a list.
- `join()` combines list elements into a string.
- Validation methods return `True` or `False`.