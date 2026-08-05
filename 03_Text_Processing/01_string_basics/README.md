# String Basics in Python

A **string** is a sequence of characters enclosed in quotes.

```python
name = "Python"
```

Strings are one of the most commonly used data types in Python.

---

## Creating Strings

Using single quotes:

```python
language = 'Python'
```

Using double quotes:

```python
language = "Python"
```

Using triple quotes (multi-line strings):

```python
message = """Welcome
to
Python"""
```

---

## Accessing Characters

Strings use **indexing**.

```python
text = "Python"

print(text[0])
print(text[2])
```

Output:

```text
P
t
```

---

## Negative Indexing

Negative indexing starts from the end.

```python
text = "Python"

print(text[-1])
print(text[-2])
```

Output:

```text
n
o
```

---

## String Length

Use `len()` to find the number of characters.

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

---

## String Slicing

Syntax:

```python
string[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])
print(text[2:6])
```

Output:

```text
Pyt
thon
```

---

## String Concatenation

Join strings using `+`.

```python
first = "Hello"
second = "Python"

print(first + " " + second)
```

Output:

```text
Hello Python
```

---

## String Repetition

Repeat a string using `*`.

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

---

## Check Membership

Use `in` and `not in`.

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
```

Output:

```text
True
False
```

---

## Strings are Immutable

Strings cannot be modified after creation.

Incorrect:

```python
text = "Python"

text[0] = "J"
```

This raises:

```text
TypeError
```

Correct:

```python
text = "J" + text[1:]
```

Output:

```text
Jython
```

---

## Key Points

- Strings store text.
- Strings are immutable.
- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Use slicing to extract parts of a string.
- `+` joins strings.
- `*` repeats strings.
- `len()` returns the string length.

---

## Quick Revision

| Operation | Example |
|-----------|---------|
| Create | `"Python"` |
| Index | `text[0]` |
| Negative Index | `text[-1]` |
| Slice | `text[1:4]` |
| Length | `len(text)` |
| Join | `+` |
| Repeat | `*` |
| Membership | `in`, `not in` |
| Immutable | Cannot modify characters |