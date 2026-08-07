# String Formatting in Python

String formatting lets you insert values into strings and control how they are displayed.

---

## 1. `%` Formatting

Older formatting style.

```python
name = "Akhil"
age = 20
print("Name: %s, Age: %d" % (name, age))
```

Common specifiers:

```text
%s → String
%d → Integer
%f → Float
```

---

## 2. `str.format()`

Uses `{}` placeholders.

```python
name = "Akhil"
age = 20
print("Name: {}, Age: {}".format(name, age))
```

Named placeholders:

```python
print("Name: {name}, Age: {age}".format(name="Akhil", age=20))
```

---

## 3. f-Strings ⭐

Modern and recommended approach.

```python
name = "Akhil"
age = 20
print(f"Name: {name}, Age: {age}")
```

Expressions can be used directly:

```python
a = 10
b = 20
print(f"Total: {a + b}")
```

---

## 4. Decimal Precision

Use `:.2f` for 2 decimal places.

```python
price = 99.5678
print(f"Price: ₹{price:.2f}")
```

Output:

```text
Price: ₹99.57
```

---

## 5. Number Formatting

Comma separators:

```python
number = 1000000
print(f"{number:,}")
```

Output:

```text
1,000,000
```

Percentage:

```python
score = 0.875
print(f"{score:.1%}")
```

Output:

```text
87.5%
```

---

## 6. Alignment

```python
name = "Python"
print(f"{name:<10}")   # Left
print(f"{name:>10}")   # Right
print(f"{name:^10}")   # Center
```

```text
< → Left
> → Right
^ → Center
```

---

## 7. Width

```python
name = "Python"
print(f"{name:10}")
```

The value occupies a minimum width of `10` characters.

---

## 8. Combining Format Specifiers

```python
price = 1234.567
print(f"{price:,.2f}")
```

Output:

```text
1,234.57
```

---

## Quick Revision

```text
% formatting    → Older style
.format()       → Placeholder-based
f-string        → Modern & preferred

:.2f            → 2 decimal places
:,              → Thousands separator
:.1%            → Percentage
:<10            → Left aligned
:>10            → Right aligned
:^10            → Center aligned
```

---

## Key Point

For modern Python code, **prefer f-strings** for most string-formatting tasks.