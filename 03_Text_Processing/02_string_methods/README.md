# String Methods in Python

String methods are built-in functions used to manipulate and analyze strings.

They **do not modify the original string** because strings are immutable. Instead, they return a new string.

---

## Change Case

### `upper()`

Converts all characters to uppercase.

```python
text = "Python"
print(text.upper())
```

Output:

```text
PYTHON
```

---

### `lower()`

Converts all characters to lowercase.

```python
print("PYTHON".lower())
```

Output:

```text
python
```

---

### `title()`

Converts the first letter of every word to uppercase.

```python
print("python programming".title())
```

Output:

```text
Python Programming
```

---

### `capitalize()`

Capitalizes only the first character.

```python
print("python programming".capitalize())
```

Output:

```text
Python programming
```

---

### `swapcase()`

Swaps uppercase and lowercase letters.

```python
print("Python".swapcase())
```

Output:

```text
pYTHON
```

---

## Remove Spaces

### `strip()`

Removes spaces from both ends.

```python
text = "  Python  "
print(text.strip())
```

---

### `lstrip()`

Removes spaces from the left.

```python
print(text.lstrip())
```

---

### `rstrip()`

Removes spaces from the right.

```python
print(text.rstrip())
```

---

## Replace Text

### `replace()`

Replaces one substring with another.

```python
text = "I like Java"
print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

---

## Search

### `find()`

Returns the index of the first occurrence.

```python
text = "Python Programming"
print(text.find("Program"))
```

Output:

```text
7
```

Returns `-1` if not found.

---

### `count()`

Counts the number of occurrences.

```python
text = "Python Python"
print(text.count("Python"))
```

Output:

```text
2
```

---

## Check Beginning & End

### `startswith()`

```python
text = "Python Programming"
print(text.startswith("Python"))
```

Output:

```text
True
```

---

### `endswith()`

```python
print(text.endswith("Programming"))
```

Output:

```text
True
```

---

## Split & Join

### `split()`

Splits a string into a list.

```python
text = "Python,Java,C++"
print(text.split(","))
```

Output:

```text
['Python', 'Java', 'C++']
```

---

### `join()`

Joins list elements into a string.

```python
languages = ["Python", "Java", "C++"]
print(", ".join(languages))
```

Output:

```text
Python, Java, C++
```

---

## Validation Methods

### `isalpha()`

```python
print("Python".isalpha())
```

Returns `True` if all characters are letters.

---

### `isdigit()`

```python
print("123".isdigit())
```

Returns `True` if all characters are digits.

---

### `isalnum()`

```python
print("Python123".isalnum())
```

Returns `True` if all characters are letters or digits.

---

### `islower()`

```python
print("python".islower())
```

Returns `True` if all letters are lowercase.

---

### `isupper()`

```python
print("PYTHON".isupper())
```

Returns `True` if all letters are uppercase.

---

### `isspace()`

```python
print("   ".isspace())
```

Returns `True` if the string contains only whitespace.

---

## Key Points

- String methods return a new string.
- Strings are immutable.
- `find()` returns `-1` if not found.
- `split()` returns a list.
- `join()` combines list elements into a string.
- Validation methods return `True` or `False`.

---

## Quick Revision

| Method | Purpose |
|---------|---------|
| `upper()` | Uppercase |
| `lower()` | Lowercase |
| `title()` | Title Case |
| `capitalize()` | First letter uppercase |
| `swapcase()` | Swap letter case |
| `strip()` | Remove spaces |
| `replace()` | Replace text |
| `find()` | Find index |
| `count()` | Count occurrences |
| `startswith()` | Starts with? |
| `endswith()` | Ends with? |
| `split()` | String → List |
| `join()` | List → String |
| `isalpha()` | Letters only |
| `isdigit()` | Digits only |
| `isalnum()` | Letters & digits |
| `islower()` | Lowercase? |
| `isupper()` | Uppercase? |
| `isspace()` | Whitespace only |