# statistics Module Cheat Sheet

## Import
```python
from statistics import (
    mean,
    fmean,
    median,
    median_low,
    median_high,
    median_grouped,
    mode,
    multimode,
    variance,
    pvariance,
    stdev,
    pstdev,
    quantiles,
    geometric_mean,
    harmonic_mean
)
```
The `statistics` module provides built-in functions for descriptive statistical analysis.

---

# Functions Overview

| Function | Purpose |
|----------|---------|
| `mean()` | Arithmetic average |
| `fmean()` | Fast floating-point average |
| `median()` | Middle value |
| `median_low()` | Lower middle value |
| `median_high()` | Higher middle value |
| `median_grouped()` | Median for grouped data |
| `mode()` | Most frequent value |
| `multimode()` | Multiple most frequent values |
| `variance()` | Sample variance |
| `pvariance()` | Population variance |
| `stdev()` | Sample standard deviation |
| `pstdev()` | Population standard deviation |
| `quantiles()` | Divide data into equal intervals |
| `geometric_mean()` | Geometric average |
| `harmonic_mean()` | Harmonic average |

---

# 1. mean()

**Purpose:** Returns the arithmetic average.

**Syntax**

```python
mean(data)
```

**Example**

```python
from statistics import mean
marks = [80, 85, 90]
print(mean(marks))
```

**Output**

```python
85
```

---

# 2. fmean()

**Purpose:** Returns a faster floating-point mean.

**Syntax**

```python
fmean(data)
```

**Example**

```python
from statistics import fmean
numbers = [10, 20, 30]
print(fmean(numbers))
```

**Output**

```python
20.0
```

---

# 3. median()

**Purpose:** Returns the middle value.

**Syntax**

```python
median(data)
```

**Example**

```python
from statistics import median
numbers = [10, 20, 30, 40, 50]
print(median(numbers))
```

**Output**

```python
30
```

---

# 4. median_low()

**Purpose:** Returns the lower middle value.

**Syntax**

```python
median_low(data)
```

---

# 5. median_high()

**Purpose:** Returns the higher middle value.

**Syntax**

```python
median_high(data)
```

---

# 6. median_grouped()

**Purpose:** Estimates the median for grouped continuous data.

**Syntax**

```python
median_grouped(data)
```

---

# 7. mode()

**Purpose:** Returns the most frequent value.

**Syntax**

```python
mode(data)
```

**Example**

```python
from statistics import mode
numbers = [2, 3, 3, 4]
print(mode(numbers))
```

**Output**

```python
3
```

---

# 8. multimode()

**Purpose:** Returns all modes.

**Syntax**

```python
multimode(data)
```

**Example**

```python
from statistics import multimode
numbers = [1, 2, 2, 3, 3]
print(multimode(numbers))
```

**Output**

```python
[2, 3]
```

---

# 9. variance()

**Purpose:** Returns the sample variance.

**Syntax**

```python
variance(data)
```

---

# 10. pvariance()

**Purpose:** Returns the population variance.

**Syntax**

```python
pvariance(data)
```

---

# 11. stdev()

**Purpose:** Returns the sample standard deviation.

**Syntax**

```python
stdev(data)
```

---

# 12. pstdev()

**Purpose:** Returns the population standard deviation.

**Syntax**

```python
pstdev(data)
```

---

# 13. quantiles()

**Purpose:** Divides data into equal intervals.

**Syntax**

```python
quantiles(data, n=4)
```

**Example**

```python
from statistics import quantiles
marks = [40, 50, 60, 70, 80, 90]
print(quantiles(marks, n=4))
```

---

# 14. geometric_mean()

**Purpose:** Returns the geometric average.

**Syntax**

```python
geometric_mean(data)
```

**Example**

```python
from statistics import geometric_mean
print(geometric_mean([2, 8]))
```

**Output**

```python
4.0
```

---

# 15. harmonic_mean()

**Purpose:** Returns the harmonic average.

**Syntax**

```python
harmonic_mean(data)
```

**Example**

```python
from statistics import harmonic_mean
print(harmonic_mean([2, 4]))
```

**Output**

```python
2.6666666666666665
```

---

# mean() vs fmean()

| mean() | fmean() |
|---------|----------|
| Supports more numeric types | Faster for floating-point numbers |
| Slightly slower | Optimized for speed |

---

# variance() vs pvariance()

| variance() | pvariance() |
|-------------|-------------|
| Sample variance | Population variance |
| Divides by (n - 1) | Divides by n |

---

# stdev() vs pstdev()

| stdev() | pstdev() |
|----------|-----------|
| Sample standard deviation | Population standard deviation |
| Uses sample variance | Uses population variance |

---

# mode() vs multimode()

| mode() | multimode() |
|---------|-------------|
| Returns one most frequent value | Returns all most frequent values |
| Single result | List of results |

---

# median() vs mean()

| mean() | median() |
|---------|-----------|
| Average of all values | Middle value |
| Affected by outliers | Less affected by outliers |

---

# Best Practices

- Use `mean()` for average calculations.
- Use `median()` when outliers may affect the average.
- Use `mode()` for categorical or repeated values.
- Use `variance()` and `stdev()` to measure data spread.
- Use `quantiles()` for quartile analysis.
- Use `geometric_mean()` for growth rates.
- Use `harmonic_mean()` for rates such as average speed.

---

# Common Mistakes

- Using `variance()` with only one value.
- Confusing sample (`variance()`) and population (`pvariance()`) calculations.
- Using `mean()` when the dataset contains extreme outliers.
- Expecting `mode()` to return multiple values (use `multimode()` instead).
- Using `geometric_mean()` with zero or negative numbers.

---

# When Should I Use This Module?

✅ **Use `statistics` when:**

- Calculating averages
- Analyzing student marks
- Survey analysis
- Business reports
- Machine learning preprocessing
- Small to medium datasets

❌ **Avoid `statistics` when:**

- Working with very large datasets (use NumPy/Pandas).
- Advanced statistical modeling is required.

---

# Quick Revision

| Need | Function |
|------|----------|
| Average | `mean()` |
| Fast average | `fmean()` |
| Middle value | `median()` |
| Lower median | `median_low()` |
| Higher median | `median_high()` |
| Grouped median | `median_grouped()` |
| Most frequent value | `mode()` |
| Multiple modes | `multimode()` |
| Sample variance | `variance()` |
| Population variance | `pvariance()` |
| Sample standard deviation | `stdev()` |
| Population standard deviation | `pstdev()` |
| Quartiles | `quantiles()` |
| Geometric average | `geometric_mean()` |
| Harmonic average | `harmonic_mean()` |