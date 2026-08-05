# String Basics — Cheat Sheet

## Creating Strings

```python
text = "Python"
text = 'Python'
text = """Python"""
```

---

## Indexing

Access a character using its index.

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

Access characters from the end.

```python
print(text[-1])
print(text[-2])
```

Output:

```text
n
o
```

---

## Slicing

```python
text[start:end]
```

Example:

```python
text = "Python"

print(text[0:3])
print(text[2:])
print(text[:4])
```

Output:

```text
Pyt
thon
Pyth
```

---

## String Length

```python
len(text)
```

Example:

```python
print(len("Python"))
```

Output:

```text
6
```

---

## Concatenation

Join strings using `+`.

```python
first = "Hello"
second = "World"
print(first + " " + second)
```

Output:

```text
Hello World
```

---

## Repetition

Repeat a string using `*`.

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

---

## Membership

```python
text = "Python Programming"
print("Python" in text)
print("Java" not in text)
```

Output:

```text
True
True
```

---

## Immutability

Strings cannot be modified directly.

❌ Incorrect

```python
text = "Python"
text[0] = "J"
```

✅ Correct

```python
text = "J" + text[1:]
```

---

## Quick Revision

```text
text[0]      → First character
text[-1]     → Last character
text[1:4]    → Slice
len(text)    → Length
+            → Concatenate
*            → Repeat
in           → Check substring
not in       → Check absence
```

---

## Key Points

- Strings are immutable.
- Indexing starts from `0`.
- Negative indexing starts from `-1`.
- Slicing extracts part of a string.
- `+` joins strings.
- `*` repeats strings.
- `in` checks substring existence.