# String Formatting — Interview Questions

## 1. What is string formatting?

String formatting is the process of inserting values into a string and controlling their display.

```python
name = "Akhil"
print(f"Hello, {name}")
```

---

## 2. What are the main ways to format strings?

```text
% formatting
str.format()
f-strings
```

---

## 3. What are f-strings?

f-strings allow expressions and variables to be directly embedded inside strings.

```python
name = "Akhil"
age = 20
print(f"{name} is {age} years old.")
```

---

## 4. Why are f-strings preferred?

They are:
- Easy to read
- Concise
- Fast
- Support expressions directly

```python
a = 10
b = 20
print(f"Total = {a + b}")
```

---

## 5. What does `:.2f` mean?

It formats a floating-point number to **2 decimal places**.

```python
price = 99.567
print(f"{price:.2f}")
```

Output:

```text
99.57
```

---

## 6. How do you add commas to numbers?

Use `:,`.

```python
number = 1000000
print(f"{number:,}")
```

Output:

```text
1,000,000
```

---

## 7. How do you format a percentage?

Use `%` in the format specifier.

```python
score = 0.875
print(f"{score:.1%}")
```

Output:

```text
87.5%
```

---

## 8. How do you align text?

```python
text = "Python"
print(f"{text:<10}")  # Left
print(f"{text:>10}")  # Right
print(f"{text:^10}")  # Center
```

---

## 9. What is the difference between `format()` and f-strings?

```python
name = "Akhil"
print("Hello {}".format(name))
print(f"Hello {name}")
```

Both work, but **f-strings are generally preferred in modern Python**.

---

## 10. Can f-strings contain expressions?

Yes.

```python
a = 10
b = 5
print(f"Sum: {a + b}")
print(f"Product: {a * b}")
```

---

## Quick Revision

```text
% formatting  → Older style
.format()     → Placeholder-based
f-string      → Modern & preferred

:.2f          → 2 decimal places
:,            → Thousands separator
:.1%          → Percentage

:<10          → Left
:>10          → Right
:^10          → Center
```