# functools Module Interview Questions

## Beginner Level

### 1. What is the `functools` module?

**Answer:**

`functools` is a built-in Python module that provides higher-order functions and decorators for creating reusable, efficient, and optimized code.

---

### 2. What is `partial()`?

**Answer:**

`partial()` creates a new function by fixing one or more arguments of an existing function.

```python
from functools import partial
def multiply(a, b):
    return a * b
double = partial(multiply, b=2)
print(double(10))
```

Output

```python
20
```

---

### 3. What is `reduce()`?

**Answer:**

`reduce()` repeatedly applies a function to an iterable until only one value remains.

```python
from functools import reduce
numbers = [1, 2, 3]
print(reduce(lambda x, y: x + y, numbers))
```

Output

```python
6
```

---

### 4. What is `lru_cache()`?

**Answer:**

`lru_cache()` stores previously computed function results so repeated calls are much faster.

---

### 5. What is `wraps()` used for?

**Answer:**

`wraps()` preserves the original function's metadata (name, docstring, annotations) when creating decorators.

---

## Intermediate Level

### 6. What does `cmp_to_key()` do?

**Answer:**

It converts an old-style comparison function into a key function for sorting.

```python
numbers.sort(key=cmp_to_key(compare))
```

---

### 7. What is `cached_property()`?

**Answer:**

It computes a property only once and stores the result for future access.

---

### 8. What is `total_ordering()`?

**Answer:**

`total_ordering()` automatically generates the remaining comparison methods when you implement `__eq__()` and one ordering method (such as `__lt__()`).

---

### 9. What is `singledispatch()`?

**Answer:**

It allows one function to have different implementations depending on the type of its first argument.

---

### 10. Why is `lru_cache()` useful?

**Answer:**

It avoids repeating expensive calculations, improving program performance.

---

## Advanced Level

### 11. Difference between `partial()` and `lambda`?

| partial() | lambda |
|------------|---------|
| Reuses existing function | Creates a new anonymous function |
| Better for fixed arguments | Better for simple expressions |
| More readable | Can become harder to read |

---

### 12. Difference between `reduce()` and `sum()`?

| reduce() | sum() |
|-----------|-------|
| Supports any binary operation | Supports only addition |
| More flexible | Simpler and faster for sums |

---

### 13. Difference between `property()` and `cached_property()`?

| property() | cached_property() |
|-------------|-------------------|
| Recalculates every access | Calculates only once |
| No caching | Cached result |

---

### 14. Why should decorators use `@wraps`?

**Answer:**

Without `@wraps`, the decorated function loses its original name, documentation, and metadata.

---

### 15. Which functions in `functools` are decorators?

**Answer:**

- `lru_cache`
- `wraps`
- `cached_property`
- `total_ordering`
- `singledispatch`

---

## Scenario-Based Questions

### 16. A recursive Fibonacci function is slow. Which function can improve its performance?

**Answer**

```python
@lru_cache
```

---

### 17. You need a reusable function that always applies a 15% discount. Which function will you use?

**Answer**

```python
partial()
```

---

### 18. You want to multiply every value in a list into one final result. Which function should you use?

**Answer**

```python
reduce()
```

---

### 19. You already have a comparison function and need to sort a list. Which function should you use?

**Answer**

```python
cmp_to_key()
```

---

### 20. A class has an expensive property that rarely changes. Which decorator is best?

**Answer**

```python
@cached_property
```

---

## Coding Questions

### 21. Create a function that always adds 10 to a number.
```python
partial()
```

---

### 22. Find the product of all numbers in a list.

```python
reduce()
```

---

### 23. Optimize a recursive factorial function.

```python
@lru_cache
```

---

### 24. Create a logging decorator while preserving the function name.

```python
@wraps
```

---

### 25. Sort objects using a comparison function.

```python
cmp_to_key()
```

---

### 26. Create a generic function that behaves differently for integers and strings.

```python
@singledispatch
```

---

## Frequently Used Functions

| Function | Purpose |
|----------|---------|
| `partial()` | Fix arguments |
| `reduce()` | Aggregate iterable |
| `lru_cache()` | Cache results |
| `wraps()` | Preserve metadata |
| `cmp_to_key()` | Custom sorting |
| `cached_property()` | Cached property |
| `total_ordering()` | Auto comparisons |
| `singledispatch()` | Generic functions |

---

## Best Practices

- Use `partial()` to reduce duplicate code.
- Use `reduce()` only when it improves readability.
- Use `lru_cache()` for expensive recursive computations.
- Always use `@wraps` in decorators.
- Use `cached_property()` for costly computed attributes.
- Use `total_ordering()` to minimize comparison methods.
- Use `singledispatch()` instead of long `if isinstance()` chains.

---

## Common Mistakes

- Forgetting `@wraps` inside decorators.
- Using `reduce()` when `sum()` is sufficient.
- Applying `lru_cache()` to functions with mutable arguments.
- Expecting `cached_property()` to refresh automatically after data changes.
- Assuming `singledispatch()` checks every argument (it dispatches only on the first argument).

---

## Quick Revision

| Need | Function |
|------|----------|
| Fix function arguments | `partial()` |
| Reduce iterable | `reduce()` |
| Cache results | `lru_cache()` |
| Preserve metadata | `wraps()` |
| Custom sorting | `cmp_to_key()` |
| Cached property | `cached_property()` |
| Auto comparison methods | `total_ordering()` |
| Function overloading | `singledispatch()` |