# Regular Expressions in Python

Regular expressions (**regex**) are patterns used to search, match, extract, and replace text.

Python provides regex through the built-in `re` module.

```python
import re
```

---

## Basic Pattern

```python
pattern = r"\d+"
text = "My age is 20"
result = re.findall(pattern, text)
print(result)
```

Output:

```text
['20']
```

Use `r"..."` for **raw strings**, which are recommended for regex patterns.

---

## Common Patterns

| Pattern | Meaning |
|---|---|
| `\d` | Digit |
| `\D` | Not a digit |
| `\w` | Word character |
| `\W` | Not a word character |
| `\s` | Whitespace |
| `\S` | Not whitespace |
| `.` | Any character |
| `^` | Start of string |
| `$` | End of string |

---

## Character Classes

```text
[abc]     → a, b, or c
[a-z]     → Lowercase letters
[A-Z]     → Uppercase letters
[0-9]     → Digits
[^0-9]    → Not a digit
```

Example:

```python
re.findall(r"[A-Z]", "Python ABC")
```

---

## Quantifiers

```text
*       → 0 or more
+       → 1 or more
?       → 0 or 1
{3}     → Exactly 3
{2,5}   → Between 2 and 5
```

Example:

```python
re.findall(r"\d+", "A12 B345")
```

Output:

```text
['12', '345']
```

---

## `re.search()`

Searches for the first match anywhere in the string.

```python
result = re.search(r"\d+", "Age: 20")
print(result.group())
```

Output:

```text
20
```

---

## `re.match()`

Checks for a match **at the beginning** of the string.

```python
result = re.match(r"Hello", "Hello Python")
print(result.group())
```

---

## `re.findall()`

Returns all matches as a list.

```python
numbers = re.findall(r"\d+", "A12 B34 C56")
print(numbers)
```

Output:

```text
['12', '34', '56']
```

---

## `re.sub()`

Replaces matching text.

```python
text = "Python is easy"
result = re.sub(r"easy", "powerful", text)

print(result)
```

Output:

```text
Python is powerful
```

---

## `re.split()`

Splits text using a regex pattern.

```python
text = "Python,Java;C++"
result = re.split(r"[,;]", text)
print(result)
```

Output:

```text
['Python', 'Java', 'C++']
```

---

## Groups

Parentheses create groups.

```python
text = "Name: Akhil"
result = re.search(r"Name: (\w+)", text)
print(result.group(1))
```

Output:

```text
Akhil
```

---

## Simple Email Pattern

```python
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
email = "user@example.com"
print(bool(re.match(pattern, email)))
```

---

## Quick Revision

```text
re.search()   → First match anywhere
re.match()    → Match at beginning
re.findall()  → All matches
re.sub()      → Replace matches
re.split()    → Split using pattern

\d            → Digit
\w            → Word character
\s            → Whitespace
+             → 1 or more
*             → 0 or more
?             → 0 or 1
^             → Start
$             → End
()            → Group
```

### Key Point

Regex is especially useful for **validation, extraction, searching, and cleaning text**.