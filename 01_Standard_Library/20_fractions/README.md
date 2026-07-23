# fractions Module

The `fractions` module is a built-in Python library that provides support for **exact rational number arithmetic** using the `Fraction` class.

Unlike floating-point numbers, fractions are represented as **numerator/denominator** pairs, ensuring precise mathematical calculations without rounding errors.

---

# Why Use fractions?

Floating-point numbers can introduce precision errors.

Example:

```python
print(1 / 3)
```

Output

```python
0.3333333333333333
```

Using `Fraction`:

```python
from fractions import Fraction
print(Fraction(1, 3))
```

Output

```python
1/3
```

The fraction is stored exactly instead of approximately.

---

# Importing the Module

```python
from fractions import Fraction
```

or

```python
from fractions import *
```

---

# Functions and Classes Covered

| Function / Class | Purpose |
|------------------|---------|
| `Fraction()` | Create fraction objects |
| `.numerator` | Returns numerator |
| `.denominator` | Returns denominator |
| `limit_denominator()` | Finds the closest simple fraction |
| Arithmetic Operators | Add, subtract, multiply, divide |
| Comparison Operators | Compare fractions |
| `float()` | Convert fraction to float |
| `Fraction.from_float()` | Create fraction from float |
| `Fraction.from_decimal()` | Create fraction from Decimal |

---

# Why Learn fractions?

The `fractions` module is useful in:

- Mathematics
- Scientific calculations
- Engineering
- Education software
- Computer graphics
- Measurement systems
- Ratio calculations

---

# Advantages

- Exact rational arithmetic
- Automatic fraction simplification
- No floating-point precision errors
- Easy arithmetic operations
- Supports comparisons
- Built into Python

---

# Common Operations

## Creating Fractions

```python
from fractions import Fraction
a = Fraction(3, 4)
b = Fraction(5, 8)
```

---

## Automatic Simplification

```python
Fraction(6, 12)
```

Output

```python
1/2
```

---

## Addition

```python
a + b
```

---

## Subtraction

```python
a - b
```

---

## Multiplication

```python
a * b
```

---

## Division

```python
a / b
```

---

## Access Numerator

```python
a.numerator
```

---

## Access Denominator

```python
a.denominator
```

---

## Convert to Float

```python
float(a)
```

Output

```python
0.75
```

---

## Find Closest Fraction

```python
Fraction(3.14159).limit_denominator()
```

Output

```python
355/113
```

---

# Real-World Applications

## Mathematics

- Rational number calculations
- Algebra
- Geometry

---

## Education

- Fraction calculators
- Learning applications

---

## Engineering

- Mechanical ratios
- Measurements

---

## Scientific Computing

- Exact numerical representations
- Formula calculations

---

## Finance

- Ratio calculations
- Profit sharing

---

# Prerequisites

Before learning this module, you should know:
- Variables
- Numbers
- Arithmetic operators
- Functions
- Python imports

---

# Mini Project

## Fraction Calculator

Features:
- Add fractions
- Subtract fractions
- Multiply fractions
- Divide fractions
- Simplify fractions
- Compare fractions

---

# Best Practices

- Use `Fraction` when exact rational values are required.
- Let Python simplify fractions automatically.
- Use `limit_denominator()` for approximating decimal values.
- Convert to `float` only when necessary.
- Use `Fraction` instead of `float` for precise mathematical calculations.

---

# Common Mistakes

- Using `float` when exact fractions are required.
- Forgetting that fractions simplify automatically.
- Converting to `float` too early and losing precision.
- Assuming `Fraction(2, 4)` stays as `2/4` (it becomes `1/2`).

---

# Quick Revision

| Need | Use |
|------|-----|
| Create fraction | `Fraction()` |
| Numerator | `.numerator` |
| Denominator | `.denominator` |
| Simplify | Automatic |
| Approximate fraction | `limit_denominator()` |
| Convert to float | `float()` |
| Create from float | `Fraction.from_float()` |
| Create from Decimal | `Fraction.from_decimal()` |

---

# What's Next?

In `examples.py`, you'll learn with practical examples covering:

- Creating fractions
- Automatic simplification
- Arithmetic operations
- Accessing numerator and denominator
- Comparing fractions
- Converting fractions to floats
- Creating fractions from floats and decimals
- Using `limit_denominator()`