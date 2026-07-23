# fractions Module Interview Questions

## Beginner Level

### 1. What is the `fractions` module?

**Answer:**

The `fractions` module is a built-in Python library that provides the `Fraction` class for representing and performing exact rational number arithmetic.

---

### 2. What is a `Fraction` object?

**Answer:**

A `Fraction` object represents a rational number as a numerator and denominator.

Example

```python
from fractions import Fraction
fraction = Fraction(3, 4)
print(fraction)
```

Output

```python
3/4
```

---

### 3. Why use `Fraction` instead of `float`?

**Answer:**

`Fraction` stores values exactly, while `float` may introduce rounding and precision errors.

Example

```python
from fractions import Fraction
print(Fraction(1, 3))
```

Output

```python
1/3
```

---

### 4. How do you import the `Fraction` class?

**Answer**

```python
from fractions import Fraction
```

---

### 5. Does `Fraction` simplify values automatically?

**Answer:**

Yes.

Example

```python
Fraction(8, 12)
```

Output

```python
2/3
```

---

## Intermediate Level

### 6. How do you access the numerator?

**Answer**

```python
fraction.numerator
```

Example

```python
Fraction(5, 8).numerator
```

Output

```python
5
```

---

### 7. How do you access the denominator?

**Answer**

```python
fraction.denominator
```

Example

```python
Fraction(5, 8).denominator
```

Output

```python
8
```

---

### 8. What does `limit_denominator()` do?

**Answer:**

It returns the closest simple fraction to a given value.

Example

```python
Fraction(3.1415926535).limit_denominator()
```

Output

```python
355/113
```

---

### 9. How do you convert a fraction to a float?

**Answer**

```python
float(fraction)
```

Example

```python
float(Fraction(3, 4))
```

Output

```python
0.75
```

---

### 10. How do you create a fraction from a float?

**Answer**

```python
Fraction.from_float(0.75)
```

Output

```python
3/4
```

---

## Advanced Level

### 11. Difference between `Fraction` and `float`?

| Fraction | float |
|----------|--------|
| Exact values | Approximate values |
| No precision loss | Precision errors possible |
| Rational arithmetic | Floating-point arithmetic |
| Best for mathematics | Best for general calculations |

---

### 12. Difference between `Fraction(2, 4)` and `Fraction(1, 2)`?

**Answer:**

There is no difference.
Python automatically simplifies:

```python
Fraction(2, 4)
```

Result

```python
1/2
```

---

### 13. Can a `Fraction` be created from a string?

**Answer**

Yes.

Example

```python
Fraction("7/8")
```

Output

```python
7/8
```

---

### 14. What happens if the denominator is zero?

**Answer:**

Python raises a `ZeroDivisionError`.

Example

```python
Fraction(1, 0)
```

---

### 15. Can fractions be compared?

**Answer:**

Yes.

Example

```python
Fraction(1, 2) > Fraction(1, 3)
```

Output

```python
True
```

---
## Frequently Used Methods

| Method | Purpose |
|---------|---------|
| `Fraction()` | Create fraction |
| `.numerator` | Get numerator |
| `.denominator` | Get denominator |
| `limit_denominator()` | Approximate fraction |
| `Fraction.from_float()` | Create from float |
| `Fraction.from_decimal()` | Create from Decimal |
| `float()` | Convert to float |

---

## Best Practices

- Use `Fraction` whenever exact rational arithmetic is required.
- Let Python simplify fractions automatically.
- Use `limit_denominator()` for readable approximations.
- Convert to `float` only when necessary.
- Validate user input when accepting fractions.

---

## Common Mistakes

- Using `float` instead of `Fraction` for exact calculations.
- Expecting fractions to remain unsimplified.
- Dividing by zero.
- Converting to `float` too early and losing precision.
- Forgetting that fractions can be created directly from strings.

---
## Quick Revision

| Need | Function / Method |
|------|--------------------|
| Create fraction | `Fraction()` |
| Simplify fraction | Automatic |
| Numerator | `.numerator` |
| Denominator | `.denominator` |
| Convert to float | `float()` |
| Create from float | `Fraction.from_float()` |
| Create from Decimal | `Fraction.from_decimal()` |
| Approximate fraction | `limit_denominator()` |
| Add fractions | `+` |
| Compare fractions | `==`, `>`, `<` |