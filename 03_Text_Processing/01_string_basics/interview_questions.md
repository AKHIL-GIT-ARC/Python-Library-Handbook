# String Basics — Interview Questions

## 1. What is a string in Python?

A string is a sequence of characters enclosed in single, double, or triple quotes.

```python
text = "Python"
```

---

## 2. How do you create a string?

```python
text1 = 'Python'
text2 = "Python"
text3 = """Python"""
```

---

## 3. What is indexing?

Indexing is used to access individual characters in a string.

```python
text = "Python"
print(text[0])
print(text[3])
```

Output:

```text
P
h
```

---

## 4. What is negative indexing?

Negative indexing accesses characters from the end of the string.

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

## 5. What is string slicing?

Slicing extracts a part of a string.

```python
text = "Python"
print(text[1:4])
```

Output:

```text
yth
```

---

## 6. How do you find the length of a string?

Use the `len()` function.

```python
text = "Python"
print(len(text))
```

Output:

```text
6
```

---

## 7. What is string concatenation?

Concatenation joins two or more strings using `+`.

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

## 8. How do you repeat a string?

Use the `*` operator.

```python
print("Hi " * 3)
```

Output:

```text
Hi Hi Hi
```

---

## 9. How do you check whether a substring exists?

Use `in` or `not in`.

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

## 10. Are strings mutable?

No. Strings are **immutable**, meaning they cannot be modified after creation.

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
String           → Sequence of characters
Indexing         → text[0]
Negative Index   → text[-1]
Slicing          → text[1:4]
Length           → len(text)
Concatenation    → +
Repetition       → *
Membership       → in, not in
Immutable        → Cannot modify directly
```