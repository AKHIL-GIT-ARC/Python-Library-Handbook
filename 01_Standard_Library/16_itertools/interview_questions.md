# itertools Module Interview Questions

## Beginner Level

### 1. What is the `itertools` module?

**Answer:**

`itertools` is a built-in Python module that provides fast and memory-efficient tools for working with iterators.

---

### 2. What is an iterator?

**Answer:**

An iterator is an object that returns one item at a time using the `next()` function.

Example:

```python
numbers = iter([10, 20, 30])
print(next(numbers))
```

---

### 3. What is lazy evaluation?

**Answer:**

Lazy evaluation means values are generated only when needed instead of being stored in memory all at once.

---

### 4. What does `count()` do?

**Answer:**

Generates an infinite sequence of numbers.

```python
from itertools import count
counter = count(1)
```

---

### 5. What does `cycle()` do?

**Answer:**

Repeats an iterable forever.

```python
from itertools import cycle
colors = cycle(["Red", "Blue"])
```

---

## Intermediate Level

### 6. What does `repeat()` do?

**Answer:**

Repeats the same value multiple times.

```python
repeat("Python", 3)
```

---

### 7. What does `chain()` do?

**Answer:**

Combines multiple iterables into a single iterator.

```python
chain([1, 2], [3, 4])
```

---

### 8. What does `compress()` do?

**Answer:**

Filters data using a sequence of selectors.

```python
compress(data, selectors)
```

---

### 9. What does `accumulate()` do?

**Answer:**

Returns cumulative results such as running sums.

```python
accumulate([1, 2, 3])
```

Output

```python
1 3 6
```

---

### 10. What does `product()` do?

**Answer:**

Returns the Cartesian product of two or more iterables.

```python
product(["A", "B"], [1, 2])
```

---

## Advanced Level

### 11. Difference between `permutations()` and `combinations()`?

| permutations() | combinations() |
|----------------|----------------|
| Order matters | Order doesn't matter |
| More results | Fewer results |

---

### 12. Difference between `combinations()` and `combinations_with_replacement()`?

| combinations() | combinations_with_replacement() |
|----------------|---------------------------------|
| No repeated values | Repeated values allowed |

---

### 13. Difference between `zip()` and `zip_longest()`?

| zip() | zip_longest() |
|--------|---------------|
| Stops at shortest iterable | Continues to longest iterable |
| No fill value | Uses `fillvalue` |

---

### 14. Why is `itertools` memory efficient?

**Answer:**

Because it generates values one at a time instead of storing all values in memory.

---

### 15. When should you use `product()` instead of nested loops?

**Answer:**

When generating all possible combinations between multiple iterables.

---

## Scenario-Based Questions

### 16. You need an infinite sequence of IDs. Which function will you use?

**Answer**

```python
count()
```

---

### 17. You want to alternate between three colors repeatedly. Which function should you use?

**Answer**

```python
cycle()
```

---

### 18. You need every possible arrangement of three letters. Which function should you use?

**Answer**

```python
permutations()
```

---

### 19. You need every unique pair of students for a project. Which function should you use?

**Answer**

```python
combinations()
```

---

### 20. You need all shirt color and size combinations. Which function should you use?

**Answer**

```python
product()
```

---

## Coding Questions

### 21. Generate numbers starting from 100.

```python
count(100)
```

---

### 22. Merge three lists.

```python
chain(list1, list2, list3)
```

---

### 23. Calculate the running total of a list.

```python
list(accumulate(numbers))
```

---

### 24. Generate all permutations of `"ABC"`.

```python
permutations("ABC")
```

---

### 25. Generate all 2-element combinations.

```python
combinations(data, 2)
```

---

### 26. Zip two unequal lists.

```python
zip_longest(list1, list2, fillvalue="N/A")
```

---

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `count()` | Infinite counting |
| `cycle()` | Repeat iterable |
| `repeat()` | Repeat value |
| `chain()` | Merge iterables |
| `compress()` | Filter data |
| `accumulate()` | Running totals |
| `product()` | Cartesian product |
| `permutations()` | Ordered arrangements |
| `combinations()` | Unordered selections |
| `combinations_with_replacement()` | Repeated selections |
| `zip_longest()` | Zip unequal iterables |

---

## Best Practices

- Use `count()` for infinite counters.
- Use `cycle()` for repeating patterns.
- Use `repeat()` for constant values.
- Use `chain()` instead of manually joining iterables.
- Use `accumulate()` for cumulative calculations.
- Use `product()` for Cartesian products.
- Use `combinations()` when order doesn't matter.
- Use `permutations()` when order matters.

---

## Common Mistakes

- Converting infinite iterators to a list.
- Confusing permutations with combinations.
- Forgetting that `product()` returns tuples.
- Using `zip()` instead of `zip_longest()` for unequal iterables.

---

## Memory Trick

```
count()
↓

Infinite Numbers

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

## Quick Revision

| Need | Function |
|------|----------|
| Infinite sequence | `count()` |
| Repeat iterable | `cycle()` |
| Repeat value | `repeat()` |
| Merge iterables | `chain()` |
| Filter values | `compress()` |
| Running totals | `accumulate()` |
| Cartesian product | `product()` |
| Ordered arrangements | `permutations()` |
| Unordered selections | `combinations()` |
| Selections with repeats | `combinations_with_replacement()` |
| Zip unequal iterables | `zip_longest()` |