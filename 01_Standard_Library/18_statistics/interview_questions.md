# statistics Module Interview Questions

## Beginner Level

### 1. What is the `statistics` module?

**Answer:**

The `statistics` module is a built-in Python library that provides functions for performing descriptive statistical calculations such as mean, median, mode, variance, and standard deviation.

---

### 2. What does `mean()` return?

**Answer:**

`mean()` returns the arithmetic average of a dataset.

```python
from statistics import mean
numbers = [10, 20, 30]
print(mean(numbers))
```

Output

```python
20
```

---

### 3. What is `fmean()`?

**Answer:**

`fmean()` calculates the arithmetic mean using floating-point arithmetic and is generally faster than `mean()`.

---

### 4. What is the purpose of `median()`?

**Answer:**

`median()` returns the middle value of a sorted dataset.

```python
from statistics import median
numbers = [5, 10, 15]
print(median(numbers))
```

Output

```python
10
```

---

### 5. What does `mode()` return?

**Answer:**

`mode()` returns the value that occurs most frequently in a dataset.

```python
from statistics import mode
numbers = [1, 2, 2, 3]
print(mode(numbers))
```

Output

```python
2
```

---

## Intermediate Level

### 6. What is `multimode()`?

**Answer:**

`multimode()` returns a list of all values with the highest frequency.

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

### 7. What is variance?

**Answer:**

Variance measures how far data values are spread from the mean.

Python provides:

- `variance()` → Sample variance
- `pvariance()` → Population variance

---

### 8. What is standard deviation?

**Answer:**

Standard deviation measures the average distance of data values from the mean.

Python provides:

- `stdev()` → Sample standard deviation
- `pstdev()` → Population standard deviation

---

### 9. What does `quantiles()` do?

**Answer:**

It divides a dataset into equal-sized intervals such as quartiles, deciles, or percentiles.

---

### 10. What are `geometric_mean()` and `harmonic_mean()`?

**Answer:**

- `geometric_mean()` is used for growth rates and multiplicative data.
- `harmonic_mean()` is used for rates such as speed or ratios.

---

## Advanced Level

### 11. Difference between `mean()` and `median()`?

| mean() | median() |
|----------|-----------|
| Arithmetic average | Middle value |
| Affected by outliers | Less affected by outliers |
| Uses every value | Depends on ordered position |

---

### 12. Difference between `variance()` and `pvariance()`?

| variance() | pvariance() |
|-------------|-------------|
| Sample variance | Population variance |
| Divides by (n - 1) | Divides by n |

---

### 13. Difference between `stdev()` and `pstdev()`?

| stdev() | pstdev() |
|----------|-----------|
| Sample standard deviation | Population standard deviation |
| Uses sample variance | Uses population variance |

---

### 14. Difference between `mode()` and `multimode()`?

| mode() | multimode() |
|---------|-------------|
| One most frequent value | All most frequent values |
| Returns one value | Returns a list |

---

### 15. When should you use `median()` instead of `mean()`?

**Answer:**

Use `median()` when the dataset contains extreme values (outliers) because it is less affected by them.

---

## Scenario-Based Questions

### 16. You need the average marks of a class. Which function should you use?

**Answer**

```python
mean()
```

---

### 17. You need the middle salary in a company. Which function is best?

**Answer**

```python
median()
```

---

### 18. You need the most purchased product. Which function should you use?

**Answer**

```python
mode()
```

---

### 19. You need to measure how much marks vary from the average. Which function should you use?

**Answer**

```python
variance()
```

---

### 20. You need to divide marks into quartiles. Which function should you use?

**Answer**

```python
quantiles()
```

---

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `mean()` | Arithmetic average |
| `fmean()` | Fast average |
| `median()` | Middle value |
| `mode()` | Most frequent value |
| `multimode()` | Multiple modes |
| `variance()` | Sample variance |
| `pvariance()` | Population variance |
| `stdev()` | Sample standard deviation |
| `pstdev()` | Population standard deviation |
| `quantiles()` | Quartile calculation |
| `geometric_mean()` | Geometric average |
| `harmonic_mean()` | Harmonic average |

---

## Best Practices

- Use `mean()` for average calculations.
- Use `median()` for skewed datasets with outliers.
- Use `mode()` for categorical or repeated values.
- Use `variance()` and `stdev()` to analyze data spread.
- Use `quantiles()` to divide datasets into intervals.
- Use `geometric_mean()` for growth rates.
- Use `harmonic_mean()` for average rates.

---

## Common Mistakes

- Using `variance()` with only one data point.
- Confusing sample and population statistics.
- Using `mean()` when outliers significantly affect the dataset.
- Expecting `mode()` to return multiple values.
- Using `geometric_mean()` with zero or negative values.

---

## Quick Revision

| Need | Function |
|------|----------|
| Average | `mean()` |
| Fast average | `fmean()` |
| Middle value | `median()` |
| Most frequent value | `mode()` |
| Multiple modes | `multimode()` |
| Sample variance | `variance()` |
| Population variance | `pvariance()` |
| Sample standard deviation | `stdev()` |
| Population standard deviation | `pstdev()` |
| Quartiles | `quantiles()` |
| Geometric average | `geometric_mean()` |
| Harmonic average | `harmonic_mean()` |