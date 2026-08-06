# String Methods — Interview Questions

## 1. What are string methods?

String methods are built-in functions used to manipulate and analyze strings.

Example:

```python
text = "python"
print(text.upper())
```

Output:

```text
PYTHON
```

---

## 2. What is the difference between `upper()` and `lower()`?

| Method | Purpose |
|---------|---------|
| `upper()` | Converts all characters to uppercase |
| `lower()` | Converts all characters to lowercase |

Example:

```python
print("Python".upper())
print("PYTHON".lower())
```

---

## 3. What is the difference between `title()` and `capitalize()`?

```python
text = "python programming"

print(text.title())
print(text.capitalize())
```

Output:

```text
Python Programming
Python programming
```

- `title()` capitalizes every word.
- `capitalize()` capitalizes only the first character.

---

## 4. What does `strip()` do?

It removes whitespace from both ends of a string.

```python
text = "  Python  "

print(text.strip())
```

---

## 5. What is the difference between `find()` and `count()`?

| Method | Purpose |
|---------|---------|
| `find()` | Returns the first index |
| `count()` | Counts occurrences |

Example:

```python
text = "Python Python"
print(text.find("Python"))
print(text.count("Python"))
```

Output:

```text
0
2
```

---

## 6. What is the difference between `split()` and `join()`?

`split()` converts a string into a list.

```python
text = "Python,Java,C++"
print(text.split(","))
```

`join()` converts a list into a string.

```python
languages = ["Python", "Java", "C++"]
print(", ".join(languages))
```

---

## 7. What does `replace()` do?

It replaces one substring with another.

```python
text = "I like Java"
print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

---

## 8. What are `startswith()` and `endswith()`?

They check the beginning and ending of a string.

```python
text = "Python Programming"
print(text.startswith("Python"))
print(text.endswith("Programming"))
```

Output:

```text
True
True
```

---

## 9. What do validation methods return?

Validation methods return `True` or `False`.

```python
"Python".isalpha()
"123".isdigit()
"Python123".isalnum()
```

---

## 10. Do string methods modify the original string?

No. Strings are immutable.

```python
text = "python"
new_text = text.upper()
print(text)
print(new_text)
```

Output:

```text
python
PYTHON
```

---

## Quick Revision

```text
upper()        → Uppercase
lower()        → Lowercase
title()        → Every word uppercase
capitalize()   → First letter uppercase
swapcase()     → Swap case

strip()        → Remove spaces
replace()      → Replace text
find()         → Find index
count()        → Count occurrences

split()        → String → List
join()         → List → String

startswith()   → Starts with?
endswith()     → Ends with?

isalpha()      → Letters only
isdigit()      → Digits only
isalnum()      → Letters & digits
islower()      → Lowercase?
isupper()      → Uppercase?
isspace()      → Whitespaces only
```