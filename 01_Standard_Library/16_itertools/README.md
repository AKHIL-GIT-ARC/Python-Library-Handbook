# itertools Module

The `itertools` module provides a collection of fast, memory-efficient tools for working with iterators. Instead of storing all values in memory, these tools generate values one at a time, making them ideal for large datasets and combinatorial problems.

---

# Why Use itertools?

Without `itertools`, generating combinations or repeated sequences often requires nested loops and extra memory.
Example:

```python
colors = ["Red", "Blue"]
sizes = ["S", "M"]

result = []

for color in colors:
    for size in sizes:
        result.append((color, size))

print(result)
```

Using `product()`:

```python
from itertools import product

colors = ["Red", "Blue"]
sizes = ["S", "M"]

result = list(product(colors, sizes))

print(result)
```

Cleaner, shorter, and more efficient.

---

# What is an Iterator?

An **iterator** is an object that produces one value at a time.

Example:

```python
numbers = iter([10, 20, 30])
print(next(numbers))
print(next(numbers))
print(next(numbers))
```

Output

```python
10
20
30
```

---

# Lazy Evaluation

`itertools` uses **lazy evaluation**, meaning values are generated only when needed.

Benefits:

- Lower memory usage
- Faster processing
- Suitable for very large datasets
- Efficient looping

---

# Main Functions

| Function | Purpose |
|----------|---------|
| `count()` | Infinite counting |
| `cycle()` | Repeat an iterable forever |
| `repeat()` | Repeat one value |
| `chain()` | Combine multiple iterables |
| `compress()` | Filter data using selectors |
| `accumulate()` | Running totals |
| `product()` | Cartesian product |
| `permutations()` | Ordered arrangements |
| `combinations()` | Unordered selections |
| `combinations_with_replacement()` | Combinations allowing repeated elements |
| `zip_longest()` | Zip iterables of unequal length |

---

# Frequently Used Functions

## 1. count()
Generates an infinite sequence of numbers.

```python
from itertools import count
counter = count(1)
print(next(counter))
print(next(counter))
print(next(counter))
```

Output

```python
1
2
3
```

---

## 2. cycle()
Repeats an iterable forever.

```python
from itertools import cycle
colors = cycle(["Red", "Blue"])
print(next(colors))
print(next(colors))
print(next(colors))
```

Output

```python
Red
Blue
Red
```

---

## 3. repeat()
Repeats the same value.

```python
from itertools import repeat
for value in repeat("Python", 3):
    print(value)
```

Output

```python
Python
Python
Python
```

---

## 4. chain()
Combines multiple iterables.

```python
from itertools import chain
numbers = chain([1, 2], [3, 4])
print(list(numbers))
```

Output

```python
[1, 2, 3, 4]
```

---

## 5. compress()
Filters data using selectors.

```python
from itertools import compress
data = ["A", "B", "C", "D"]
selectors = [1, 0, 1, 0]
print(list(compress(data, selectors)))
```

Output

```python
['A', 'C']
```

---

## 6. accumulate()
Returns running totals.

```python
from itertools import accumulate
numbers = [1, 2, 3, 4]
print(list(accumulate(numbers)))
```

Output

```python
[1, 3, 6, 10]
```

---

## 7. product()
Returns the Cartesian product.

```python
from itertools import product

print(list(product([1, 2], ["A", "B"])))
```

Output

```python
[(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]
```

---

## 8. permutations()
Returns all ordered arrangements.

```python
from itertools import permutations
print(list(permutations([1, 2, 3], 2)))
```

Output

```python
[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

---

## 9. combinations()
Returns unordered selections.

```python
from itertools import combinations
print(list(combinations([1, 2, 3], 2)))
```

Output

```python
[(1, 2), (1, 3), (2, 3)]
```

---

## 10. combinations_with_replacement()
Allows repeated elements.

```python
from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1, 2], 2)))
```

Output

```python
[(1, 1), (1, 2), (2, 2)]
```

---

## 11. zip_longest()
Combines unequal iterables.

```python
from itertools import zip_longest
names = ["Akhil", "Rahul"]
marks = [90]
print(list(zip_longest(names, marks, fillvalue="N/A")))
```
Output

```python
[('Akhil', 90), ('Rahul', 'N/A')]
```

---

# Advantages

- Memory efficient
- Faster than manual loops
- Cleaner code
- Excellent for large datasets
- Ideal for combinatorial problems
- Built into Python

---

# Real-World Applications

| Function | Example |
|----------|---------|
| `count()` | Auto-increment IDs |
| `cycle()` | Round-robin scheduling |
| `repeat()` | Default values |
| `chain()` | Merge datasets |
| `compress()` | Filter selected records |
| `accumulate()` | Running totals |
| `product()` | Product variations |
| `permutations()` | Password generation |
| `combinations()` | Lottery numbers |
| `combinations_with_replacement()` | Ice cream flavor choices |
| `zip_longest()` | Merge uneven datasets |

---

# Module Summary

| Function | Best Used For |
|----------|---------------|
| `count()` | Infinite counting |
| `cycle()` | Infinite repetition |
| `repeat()` | Repeat values |
| `chain()` | Merge iterables |
| `compress()` | Filter data |
| `accumulate()` | Running calculations |
| `product()` | Cartesian products |
| `permutations()` | Ordered arrangements |
| `combinations()` | Selections |
| `combinations_with_replacement()` | Selections with repeats |
| `zip_longest()` | Unequal iterables |

---

# Prerequisites

Before learning this module, you should know:
- Lists
- Tuples
- Loops
- Functions
- Iterators (`iter()` and `next()`)

---

# Mini Project

In this module, you'll build an **Iterator Toolkit**.

Features:
- Generate product combinations
- Generate password permutations
- Create lottery combinations
- Calculate running totals
- Merge multiple datasets

---
