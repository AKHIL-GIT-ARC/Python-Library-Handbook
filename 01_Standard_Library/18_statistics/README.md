# statistics Module

The `statistics` module is a built-in Python library that provides functions for calculating descriptive statistics. It helps analyze numerical data by computing averages, measures of central tendency, dispersion, and other statistical values without requiring external libraries.

---

# Why Use statistics?

Without `statistics`:

```python
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(average)
```

Using `statistics`:

```python
from statistics import mean
numbers = [10, 20, 30, 40, 50]
print(mean(numbers))
```
Cleaner, more readable, and provides many additional statistical functions.

---

# Main Functions

| Function | Purpose |
|----------|---------|
| `mean()` | Arithmetic mean |
| `fmean()` | Fast floating-point mean |
| `median()` | Middle value |
| `median_low()` | Lower median |
| `median_high()` | Higher median |
| `median_grouped()` | Median for grouped data |
| `mode()` | Most frequent value |
| `multimode()` | Multiple modes |
| `variance()` | Sample variance |
| `pvariance()` | Population variance |
| `stdev()` | Sample standard deviation |
| `pstdev()` | Population standard deviation |
| `quantiles()` | Divide data into equal intervals |
| `geometric_mean()` | Geometric average |
| `harmonic_mean()` | Harmonic average |

---

# Frequently Used Functions

## 1. mean()

Returns the arithmetic average.

```python
from statistics import mean
marks = [80, 85, 90, 95]
print(mean(marks))
```

Output

```python
87.5
```

---

## 2. fmean()

Returns a fast floating-point mean.

```python
from statistics import fmean
numbers = [10, 20, 30]
print(fmean(numbers))
```

Output

```python
20.0
```

---

## 3. median()

Returns the middle value.

```python
from statistics import median
numbers = [10, 30, 20, 40, 50]
print(median(numbers))
```

Output

```python
30
```

---

## 4. mode()

Returns the most frequently occurring value.

```python
from statistics import mode
numbers = [2, 3, 3, 4, 5]
print(mode(numbers))
```

Output

```python
3
```

---

## 5. multimode()

Returns all modes.

```python
from statistics import multimode
numbers = [1, 2, 2, 3, 3]
print(multimode(numbers))
```

Output

```python
[2, 3]
```

---

## 6. variance()

Returns the sample variance.

```python
from statistics import variance
numbers = [2, 4, 6, 8]
print(variance(numbers))
```

Output

```python
6.666666666666667
```

---

## 7. stdev()

Returns the sample standard deviation.

```python
from statistics import stdev
numbers = [2, 4, 6, 8]
print(stdev(numbers))
```

Output

```python
2.581988897471611
```

---

## 8. quantiles()

Divides data into equal-sized intervals.

```python
from statistics import quantiles
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(quantiles(numbers, n=4))
```

Output

```python
[22.5, 45.0, 67.5]
```

---

## 9. geometric_mean()

Returns the geometric mean.

```python
from statistics import geometric_mean
numbers = [2, 8]
print(geometric_mean(numbers))
```

Output

```python
4.0
```

---

## 10. harmonic_mean()

Returns the harmonic mean.

```python
from statistics import harmonic_mean
numbers = [2, 4]
print(harmonic_mean(numbers))
```

Output

```python
2.6666666666666665
```

---

# Advantages

- Built into Python
- Easy to use
- Accurate statistical calculations
- No third-party libraries required
- Useful for education, analytics, and data science

---

# Real-World Applications

| Function | Example |
|----------|---------|
| `mean()` | Student average marks |
| `median()` | Salary analysis |
| `mode()` | Most purchased product |
| `variance()` | Data consistency |
| `stdev()` | Risk analysis |
| `quantiles()` | Quartile analysis |
| `geometric_mean()` | Investment returns |
| `harmonic_mean()` | Average speed calculations |

---

# Module Summary

| Function | Best Used For |
|----------|---------------|
| `mean()` | Average |
| `median()` | Middle value |
| `mode()` | Most common value |
| `variance()` | Data spread |
| `stdev()` | Standard deviation |
| `quantiles()` | Quartile analysis |
| `geometric_mean()` | Growth rate |
| `harmonic_mean()` | Rate calculations |

---

# Prerequisites

Before learning this module, you should know:
- Lists
- Numbers
- Functions
- Basic mathematics

---

# Mini Project

In this module, you'll build a **Student Statistics Analyzer**.
Features:
- Calculate mean marks
- Find median
- Find mode
- Calculate variance
- Calculate standard deviation
- Display quartiles
- Generate performance summary

---