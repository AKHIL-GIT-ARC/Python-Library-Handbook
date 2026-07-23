# fractions Module Cheat Sheet

## Import

```python
from fractions import Fraction
```
The `fractions` module provides exact rational number arithmetic using the `Fraction` class.

---

# Functions & Methods Overview

| Function / Method | Purpose |
|-------------------|---------|
| `Fraction()` | Create a fraction |
| `.numerator` | Get numerator |
| `.denominator` | Get denominator |
| `limit_denominator()` | Approximate with a simple fraction |
| `Fraction.from_float()` | Create fraction from float |
| `Fraction.from_decimal()` | Create fraction from Decimal |
| `float()` | Convert fraction to float |

---

# 1. Fraction()

**Purpose:** Creates a fraction object.

**Syntax**

```python
Fraction(numerator, denominator)
```

**Example**

```python
from fractions import Fraction
fraction = Fraction(3, 4)
print(fraction)
```

**Output**

```python
3/4
```

---

# 2. Automatic Simplification

Fractions are automatically reduced to their simplest form.

**Example**

```python
Fraction(12, 18)
```

**Output**

```python
2/3
```

---

# 3. Addition

```python
from fractions import Fraction
a = Fraction(1, 2)
b = Fraction(1, 3)
print(a + b)
```

**Output**

```python
5/6
```

---

# 4. Subtraction

```python
print(a - b)
```

**Output**

```python
1/6
```

---

# 5. Multiplication

```python
print(a * b)
```

**Output**

```python
1/6
```

---

# 6. Division

```python
print(a / b)
```

**Output**

```python
3/2
```

---

# 7. numerator

**Purpose:** Returns the numerator.

**Example**

```python
fraction = Fraction(5, 8)
print(fraction.numerator)
```

**Output**

```python
5
```

---

# 8. denominator

**Purpose:** Returns the denominator.

**Example**

```python
fraction = Fraction(5, 8)
print(fraction.denominator)
```

**Output**

```python
8
```

---

# 9. Convert to Float

**Purpose:** Converts a fraction to a floating-point number.

**Example**

```python
fraction = Fraction(3, 4)
print(float(fraction))
```

**Output**

```python
0.75
```

---

# 10. Fraction.from_float()

**Purpose:** Creates a fraction from a float.

**Syntax**

```python
Fraction.from_float(value)
```

**Example**

```python
Fraction.from_float(0.75)
```

**Output**

```python
3/4
```

---

# 11. Fraction.from_decimal()

**Purpose:** Creates a fraction from a Decimal object.

**Example**

```python
from decimal import Decimal
Fraction.from_decimal(Decimal("2.5"))
```

**Output**

```python
5/2
```

---

# 12. limit_denominator()

**Purpose:** Finds the closest simple fraction.

**Syntax**

```python
fraction.limit_denominator()
```

**Example**

```python
Fraction(3.1415926535).limit_denominator()
```

**Output**

```python
355/113
```

---

# Fraction vs Float

| Fraction | Float |
|-----------|-------|
| Exact value | Approximate value |
| No precision loss | Precision errors possible |
| Rational arithmetic | Decimal arithmetic |
| Best for mathematics | Best for general calculations |

---

# Fraction Creation Methods

| Method | Example |
|--------|---------|
| Two integers | `Fraction(3, 4)` |
| Integer | `Fraction(5)` |
| String | `Fraction("7/8")` |
| Float | `Fraction.from_float(0.5)` |
| Decimal | `Fraction.from_decimal(Decimal("1.25"))` |

---

# Arithmetic Operators

| Operator | Example |
|----------|---------|
| Addition | `a + b` |
| Subtraction | `a - b` |
| Multiplication | `a * b` |
| Division | `a / b` |

---

# Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

---

# Best Practices

- Use `Fraction` when exact rational values are required.
- Let Python simplify fractions automatically.
- Use `limit_denominator()` for readable approximations.
- Convert to `float` only when necessary.
- Use fractions for educational, engineering, and mathematical applications.

---

# Common Mistakes

❌ Expecting fractions to remain unsimplified.

```python
Fraction(8, 12)
```

Result

```python
2/3
```

---

❌ Converting to `float` too early.

```python
float(Fraction(1, 3))
```

Result

```python
0.3333333333333333
```

Precision is lost.

---

❌ Dividing by zero.

```python
Fraction(1, 0)
```

Raises

```python
ZeroDivisionError
```

---

# When Should I Use This Module?

✅ **Use `fractions` when:**

- Mathematical calculations
- Educational software
- Ratio calculations
- Engineering applications
- Scientific formulas
- Exact rational arithmetic

❌ **Avoid `fractions` when:**

- Approximate decimal values are acceptable.
- High-performance numerical computing is required.

---

# Quick Revision

| Need | Use |
|------|-----|
| Create fraction | `Fraction()` |
| Simplify fraction | Automatic |
| Numerator | `.numerator` |
| Denominator | `.denominator` |
| Convert to float | `float()` |
| From float | `Fraction.from_float()` |
| From Decimal | `Fraction.from_decimal()` |
| Approximate fraction | `limit_denominator()` |
| Add fractions | `+` |
| Compare fractions | `==`, `>`, `<` |

---

# Interview Tip

A common Python interview question is:

**Why use `Fraction` instead of `float`?**

**Answer:**

`Fraction` stores numbers as exact rational values (numerator/denominator), eliminating floating-point precision errors. It is ideal for mathematical, scientific, and educational applications where exact results are required.