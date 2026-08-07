# String Formatting — Cheat Sheet

## `%` Formatting

```python
name = "Akhil"
age = 20
print("Name: %s, Age: %d" % (name, age))
```

```text
%s → String
%d → Integer
%f → Float
```

---

## `str.format()`

```python
print("Name: {}, Age: {}".format(name, age))
```

Named values:

```python
print("Name: {name}".format(name="Akhil"))
```

---

## f-Strings ⭐

Preferred modern approach.

```python
name = "Akhil"
age = 20
print(f"Name: {name}, Age: {age}")
```

Expressions:

```python
print(f"Total: {10 + 20}")
```

---

## Decimal Precision

```python
price = 99.5678
print(f"{price:.2f}")
```

```text
99.57
```

`.2f` → 2 decimal places.

---

## Number Formatting

```python
number = 1000000
print(f"{number:,}")
```

```text
1,000,000
```

---

## Percentage

```python
score = 0.875
print(f"{score:.1%}")
```

```text
87.5%
```

---

## Alignment

```python
text = "Python"
f"{text:<10}"   # Left
f"{text:>10}"   # Right
f"{text:^10}"   # Center
```

---

## Width

```python
f"{text:10}"
```

Minimum width = `10` characters.

---

## Combining Specifiers

```python
amount = 1234567.891
print(f"₹{amount:,.2f}")
```

Output:

```text
₹1,234,567.89
```

---

## Quick Revision

```text
%s       → String
%d       → Integer
%f       → Float

.format() → Placeholder formatting
f"{}"     → Modern formatting

:.2f      → 2 decimal places
:,        → Thousands separator
:.1%      → Percentage

:<10      → Left aligned
:>10      → Right aligned
:^10      → Center aligned
```

### Best Practice

```text
Modern Python → Prefer f-strings ⭐
```