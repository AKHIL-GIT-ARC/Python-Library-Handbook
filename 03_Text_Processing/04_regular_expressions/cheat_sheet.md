# Regular Expressions — Cheat Sheet

## Import

```python
import re
```

## Main Functions

```python
re.search(pattern, text)    # First match anywhere
re.match(pattern, text)     # Match at beginning
re.findall(pattern, text)   # All matches
re.sub(pattern, repl, text) # Replace matches
re.split(pattern, text)     # Split using pattern
```

---

## Character Classes

```text
\d       → Digit
\D       → Not a digit
\w       → Word character
\W       → Not a word character
\s       → Whitespace
\S       → Not whitespace
.        → Any character
```

---

## Custom Character Classes

```text
[abc]    → a, b, or c
[a-z]    → Lowercase letters
[A-Z]    → Uppercase letters
[0-9]    → Digits
[^0-9]   → Not a digit
```

---

## Quantifiers

```text
*        → 0 or more
+        → 1 or more
?        → 0 or 1
{3}      → Exactly 3
{2,5}    → 2 to 5
```

Example:

```python
re.findall(r"\d+", "A12 B345")
```

---

## Anchors

```text
^        → Start of string
$        → End of string
\b       → Word boundary
```

Example:

```python
r"^\d+$"
```

Matches a string containing only digits.

---

## Groups

```python
result = re.search(r"Name: (\w+)", "Name: Akhil")
print(result.group(1))
```

```text
()       → Create a group
group(1) → Get first group
```

---

## Common Patterns

```python
# Digits
r"\d+"

# Word
r"\w+"

# 10-digit phone number
r"\d{10}"

# Simple email
r"^[\w.-]+@[\w.-]+\.\w+$"
```

---

## Quick Revision

```text
search()    → First match
match()     → Beginning match
findall()   → All matches
sub()       → Replace
split()     → Split

\d          → Digit
\w          → Word
\s          → Whitespace

+           → 1+
*           → 0+
?           → 0 or 1
{n}         → Exactly n

^           → Start
$           → End
()          → Group
```

### Best Practice

Use raw strings for regex patterns:

```python
r"\d+"
```