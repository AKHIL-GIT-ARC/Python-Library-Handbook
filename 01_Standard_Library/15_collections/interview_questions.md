# collections Module Interview Questions

## Beginner Level

### 1. What is the `collections` module?

**Answer:**

The `collections` module provides specialized container data types that extend Python's built-in containers like `list`, `tuple`, and `dict`.

---

### 2. Why should we use the `collections` module?

**Answer:**

It provides cleaner, faster, and more efficient data structures for common programming tasks.

---

### 3. What is `Counter`?

**Answer:**

`Counter` counts the frequency of hashable objects.

```python
from collections import Counter
Counter(["a", "b", "a"])
```

Output

```python
Counter({'a': 2, 'b': 1})
```

---

### 4. What is `defaultdict`?

**Answer:**

`defaultdict` automatically creates a default value for missing keys.

```python
from collections import defaultdict
d = defaultdict(int)
d["Math"] += 10
```

---

### 5. What is `deque`?

**Answer:**

`deque` (Double Ended Queue) allows fast insertion and deletion from both ends.

---

## Intermediate Level

### 6. What are the advantages of `Counter` over a normal dictionary?

**Answer**

- Automatic counting
- Less code
- Useful methods like `most_common()`

---

### 7. What is the default factory in `defaultdict`?

**Answer**

The default factory creates the initial value for missing keys.

Example:

```python
defaultdict(int)
defaultdict(list)
defaultdict(set)
defaultdict(str)
```

---

### 8. Why is `deque` faster than `list` for queues?

**Answer**

`deque` performs O(1) insertions and deletions at both ends, while a `list` requires O(n) time for operations at the beginning.

---

### 9. What is `namedtuple`?

**Answer**

`namedtuple` creates tuples with named fields, making the code more readable.

```python
Student = namedtuple("Student", ["name", "age"])
```

---

### 10. What is `ChainMap`?

**Answer**

`ChainMap` combines multiple dictionaries into a single view without copying them.

---

## Advanced Level

### 11. Difference between `dict` and `defaultdict`?

| dict | defaultdict |
|------|-------------|
| Raises `KeyError` | Creates missing key automatically |
| Manual checking required | No manual checking |

---

### 12. Difference between `list` and `deque`?

| list | deque |
|------|-------|
| Slow at beginning | Fast at both ends |
| General-purpose | Queue and stack |

---

### 13. Difference between `tuple` and `namedtuple`?

| tuple | namedtuple |
|--------|------------|
| Access by index | Access by field name |
| Less readable | More readable |

---

### 14. Difference between `Counter` and `defaultdict(int)`?

| Counter | defaultdict(int) |
|----------|------------------|
| Built for counting | General-purpose dictionary |
| Has helper methods | No counting methods |

---

### 15. Difference between `OrderedDict` and `dict`?

**Answer**

Modern Python dictionaries preserve insertion order, but `OrderedDict` provides additional methods like `move_to_end()` and customized ordering operations.

---

## Scenario-Based Questions

### 16. You need to count the frequency of words in a paragraph. Which class will you use?

**Answer**

```python
Counter
```

---

### 17. You are implementing a printer queue. Which class should you use?

**Answer**

```python
deque
```

---

### 18. You need a dictionary where missing keys automatically contain an empty list. Which class should you use?

**Answer**

```python
defaultdict(list)
```

---

### 19. You want to store employee records with readable field names. Which class should you use?

**Answer**

```python
namedtuple
```

---

### 20. You want to combine application settings from multiple dictionaries. Which class should you use?

**Answer**

```python
ChainMap
```

---

## Coding Questions

### 21. Count the frequency of numbers in a list.

**Hint**

```python
Counter(numbers)
```

---

### 22. Create a queue and insert three elements.

**Hint**

```python
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
```

---

### 23. Create a `defaultdict(list)` and group students by department.

**Hint**

```python
students = defaultdict(list)
```

---

### 24. Create a `namedtuple` named `Employee`.

**Hint**

```python
Employee = namedtuple(
    "Employee",
    ["id", "name", "department"]
)
```

---

### 25. Combine two dictionaries.

**Hint**

```python
combined = ChainMap(dict1, dict2)
```

---

### 26. Display the two most common elements using `Counter`.

**Hint**

```python
counter.most_common(2)
```

---

## Commonly Used Classes

| Class | Purpose |
|--------|---------|
| `Counter` | Count occurrences |
| `defaultdict` | Default values |
| `deque` | Queue and stack |
| `namedtuple` | Named records |
| `OrderedDict` | Ordered operations |
| `ChainMap` | Combine dictionaries |

---

## Best Practices

- Use `Counter` instead of manual counting.
- Use `defaultdict` for grouping data.
- Use `deque` for queues and stacks.
- Use `namedtuple` for readable records.
- Use `ChainMap` to combine configurations.

---

## Common Mistakes

- Using `list` instead of `deque` for queues.
- Forgetting to specify a default factory in `defaultdict`.
- Modifying a `namedtuple` (it is immutable).
- Expecting `ChainMap` to create a new dictionary.

---

## Quick Revision

| Need | Class |
|------|-------|
| Count values | `Counter` |
| Default values | `defaultdict` |
| Queue | `deque` |
| Named record | `namedtuple` |
| Ordered operations | `OrderedDict` |
| Merge dictionaries | `ChainMap` |