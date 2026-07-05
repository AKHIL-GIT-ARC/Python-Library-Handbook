# Math Module Cheat Sheet

## Importing the Module

```python
import math
```

The `math` module is a built-in Python library that provides mathematical functions and constants.

No installation is required.

---

# Constants

## 1. math.pi

### Purpose

Returns the mathematical constant π (Pi).

### Syntax

```python
math.pi
```

### Example

```python
import math

print(math.pi)
```

### Output

```
3.141592653589793
```

### Real-world Applications

- Circle Area
- Circumference
- Trigonometry
- Engineering

---

## 2. math.e

### Purpose

Returns Euler's Number.

### Syntax

```python
math.e
```

### Example

```python
print(math.e)
```

### Output

```
2.718281828459045
```

### Used In

- Machine Learning
- Statistics
- Exponential Growth
- Finance

---

# Square Root

## math.sqrt()

### Purpose

Returns the square root of a number.

### Syntax

```python
math.sqrt(number)
```

### Example

```python
print(math.sqrt(49))
```

### Output

```
7.0
```

### Important Note

Only accepts non-negative numbers.

---

# Power

## math.pow()

### Purpose

Raises a number to a given power.

### Syntax

```python
math.pow(base, exponent)
```

### Example

```python
print(math.pow(2,5))
```

### Output

```
32.0
```

### Interview Tip

`math.pow()` always returns a float.

The `**` operator can return an integer if appropriate.

---

# Ceiling

## math.ceil()

### Purpose

Rounds a number upward.

### Syntax

```python
math.ceil(number)
```

### Example

```python
print(math.ceil(4.2))
```

### Output

```
5
```

---

# Floor

## math.floor()

### Purpose

Rounds a number downward.

### Syntax

```python
math.floor(number)
```

### Example

```python
print(math.floor(4.9))
```

### Output

```
4
```

---

# Factorial

## math.factorial()

### Purpose

Returns the factorial of a positive integer.

### Syntax

```python
math.factorial(number)
```

### Example

```python
print(math.factorial(5))
```

### Output

```
120
```

### Common Uses

- Probability
- Combinations
- Permutations

---

# Greatest Common Divisor

## math.gcd()

### Purpose

Returns the Greatest Common Divisor.

### Syntax

```python
math.gcd(a,b)
```

### Example

```python
print(math.gcd(20,30))
```

### Output

```
10
```

---

# Least Common Multiple

## math.lcm()

### Purpose

Returns the Least Common Multiple.

### Syntax

```python
math.lcm(a,b)
```

### Example

```python
print(math.lcm(20,30))
```

### Output

```
60
```

---

# Sine

## math.sin()

### Purpose

Returns the sine of an angle.

### Syntax

```python
math.sin(math.radians(angle))
```

### Example

```python
print(math.sin(math.radians(90)))
```

### Output

```
1.0
```

---

# Cosine

## math.cos()

### Purpose

Returns cosine.

---

# Tangent

## math.tan()

### Purpose

Returns tangent.

---

# Logarithm

## math.log()

### Purpose

Returns the natural logarithm.

### Example

```python
print(math.log(10))
```

---

# Base-10 Logarithm

## math.log10()

### Purpose

Returns logarithm with base 10.

---

# Distance

## math.dist()

### Purpose

Calculates distance between two points.

### Example

```python
p1=(2,3)
p2=(8,9)

print(math.dist(p1,p2))
```

---

# Degree Conversion

## math.degrees()

Converts radians into degrees.

---

## math.radians()

Converts degrees into radians.

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| math.pi | Pi constant |
| math.e | Euler constant |
| sqrt() | Square root |
| pow() | Power |
| ceil() | Round up |
| floor() | Round down |
| factorial() | Factorial |
| gcd() | Greatest Common Divisor |
| lcm() | Least Common Multiple |
| sin() | Sine |
| cos() | Cosine |
| tan() | Tangent |
| log() | Natural logarithm |
| log10() | Base-10 logarithm |
| dist() | Distance |
| radians() | Degree → Radian |
| degrees() | Radian → Degree |

---

# Best Practices

✅ Use `math.sqrt()` for square roots.

✅ Use `math.pi` instead of writing `3.14`.

✅ Convert degrees into radians before using trigonometric functions.

---

# Interview Tips

### Difference between `pow()` and `**`

```python
math.pow(2,3)
```

Returns

```
8.0
```

---

```python
2**3
```

Returns

```
8
```

The `**` operator preserves integer type when possible, while `math.pow()` always returns a floating-point value.