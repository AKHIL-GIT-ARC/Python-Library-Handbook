# itertools Module Cheat Sheet

## Import
```python
from itertools import (
    count,
    cycle,
    repeat,
    chain,
    compress,
    accumulate,
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    zip_longest
)
```
The `itertools` module provides fast, memory-efficient iterator building blocks.

---

# Functions Overview

| Function | Purpose |
|----------|---------|
| `count()` | Infinite counting |
| `cycle()` | Repeat iterable forever |
| `repeat()` | Repeat a value |
| `chain()` | Combine iterables |
| `compress()` | Filter using selectors |
| `accumulate()` | Running totals |
| `product()` | Cartesian product |
| `permutations()` | Ordered arrangements |
| `combinations()` | Unordered selections |
| `combinations_with_replacement()` | Combinations allowing repeats |
| `zip_longest()` | Zip unequal iterables |

---

# 1. count()

**Purpose:** Generates an infinite sequence.

**Syntax**

```python
count(start=0, step=1)
```

**Example**

```python
from itertools import count
counter = count(1)
print(next(counter))
print(next(counter))
```

**Output**

```python
1
2
```

---

# 2. cycle()

**Purpose:** Repeats an iterable forever.

**Syntax**

```python
cycle(iterable)
```

**Example**

```python
from itertools import cycle
colors = cycle(["Red", "Blue"])
print(next(colors))
print(next(colors))
print(next(colors))
```

---

# 3. repeat()

**Purpose:** Repeats one value.

**Syntax**

```python
repeat(object, times)
```

**Example**

```python
from itertools import repeat
list(repeat("Python", 3))
```

**Output**

```python
['Python', 'Python', 'Python']
```

---

# 4. chain()

**Purpose:** Combines multiple iterables.

**Syntax**

```python
chain(iter1, iter2, ...)
```

**Example**

```python
from itertools import chain
list(chain([1, 2], [3, 4]))
```
**Output**

```python
[1, 2, 3, 4]
```

---

# 5. compress()

**Purpose:** Filters data using selectors.

**Syntax**

```python
compress(data, selectors)
```

**Example**

```python
from itertools import compress
data = ["A", "B", "C"]
selectors = [1, 0, 1]
list(compress(data, selectors))
```

**Output**

```python
['A', 'C']
```

---

# 6. accumulate()

**Purpose:** Returns cumulative results.

**Syntax**

```python
accumulate(iterable)
```

**Example**

```python
from itertools import accumulate
list(accumulate([1, 2, 3, 4]))
```

**Output**

```python
[1, 3, 6, 10]
```

---

# 7. product()

**Purpose:** Returns the Cartesian product.

**Syntax**

```python
product(iter1, iter2)
```

**Example**

```python
from itertools import product
list(product(["A", "B"], [1, 2]))
```

**Output**

```python
[('A', 1), ('A', 2), ('B', 1), ('B', 2)]
```

---

# 8. permutations()

**Purpose:** Returns all ordered arrangements.

**Syntax**

```python
permutations(iterable, r)
```

**Example**

```python
from itertools import permutations
list(permutations([1, 2, 3], 2))
```

---

# 9. combinations()

**Purpose:** Returns unordered selections.

**Syntax**

```python
combinations(iterable, r)
```

**Example**

```python
from itertools import combinations
list(combinations([1, 2, 3], 2))
```

---

# 10. combinations_with_replacement()

**Purpose:** Returns combinations with repeated elements.

**Syntax**

```python
combinations_with_replacement(iterable, r)
```

**Example**

```python
from itertools import combinations_with_replacement
list(combinations_with_replacement(["A", "B"], 2))
```

---

# 11. zip_longest()

**Purpose:** Zips iterables of unequal length.

**Syntax**

```python
zip_longest(iter1, iter2, fillvalue=value)
```

**Example**

```python
from itertools import zip_longest
names = ["Akhil", "Om"]
marks = [95]
list(zip_longest(names, marks, fillvalue="N/A"))
```

**Output**

```python
[('Akhil', 95), ('Om', 'N/A')]
```

---

# permutations() vs combinations()

| permutations() | combinations() |
|----------------|----------------|
| Order matters | Order doesn't matter |
| `(A, B)` ≠ `(B, A)` | `(A, B)` = `(B, A)` |

---

# combinations() vs combinations_with_replacement()

| combinations() | combinations_with_replacement() |
|----------------|---------------------------------|
| No repeated values | Repeated values allowed |
| `(A, A)` not allowed | `(A, A)` allowed |

---

# zip() vs zip_longest()

| zip() | zip_longest() |
|--------|---------------|
| Stops at shortest iterable | Continues to longest iterable |
| Ignores extra values | Uses `fillvalue` |

---

# Best Practices

- Use `count()` for infinite sequences.
- Use `cycle()` for repeated patterns.
- Use `repeat()` for constant values.
- Use `chain()` instead of manually joining iterables.
- Use `accumulate()` for cumulative calculations.
- Use `product()` for Cartesian products.
- Use `permutations()` when order matters.
- Use `combinations()` when order doesn't matter.
- Use `zip_longest()` for uneven datasets.

---

# Common Mistakes

- Converting infinite iterators (`count()`, `cycle()`) directly to a list.
- Confusing `permutations()` with `combinations()`.
- Forgetting that `product()` returns tuples.
- Using `zip()` when iterables have different lengths.

---

# When Should I Use This Module?

✅ **Use `itertools` when:**

- Processing large datasets
- Generating combinations
- Generating permutations
- Building memory-efficient programs
- Working with iterators

❌ **Avoid `itertools` when:**

- A simple loop is easier to understand.
- Lazy evaluation is unnecessary.

---

# Memory Trick

```
count()
↓

Count Forever

cycle()
↓

Repeat Forever

repeat()
↓

Repeat Value

chain()
↓

Merge

compress()
↓

Filter

accumulate()
↓

Running Total

product()
↓

Cartesian Product

permutations()
↓

Order Matters

combinations()
↓

Choose

combinations_with_replacement()
↓

Choose With Repeats

zip_longest()
↓

Zip Unequal Lists
```

---

# Quick Revision

| Need | Function |
|------|----------|
| Infinite numbers | `count()` |
| Repeat iterable | `cycle()` |
| Repeat value | `repeat()` |
| Merge iterables | `chain()` |
| Filter data | `compress()` |
| Running totals | `accumulate()` |
| Cartesian product | `product()` |
| Ordered arrangements | `permutations()` |
| Unordered selections | `combinations()` |
| Selections with repeats | `combinations_with_replacement()` |
| Zip unequal iterables | `zip_longest()` |