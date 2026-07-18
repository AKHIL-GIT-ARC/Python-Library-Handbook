# collections Module Cheat Sheet

## Import

```python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict, ChainMap
```

The `collections` module provides specialized container data types that extend Python's built-in containers.

---

# Classes Overview

| Class | Purpose |
|--------|---------|
| `Counter` | Count occurrences of elements |
| `defaultdict` | Dictionary with default values |
| `deque` | Fast queue and stack |
| `namedtuple` | Tuple with named fields |
| `OrderedDict` | Ordered dictionary with extra features |
| `ChainMap` | Combine multiple dictionaries |

---

# 1. Counter

**Purpose:** Counts occurrences of hashable objects.

**Syntax**

```python
Counter(iterable)
```

**Example**

```python
from collections import Counter

fruits = ["apple", "banana", "apple"]

count = Counter(fruits)

print(count)
```

**Output**

```python
Counter({'apple': 2, 'banana': 1})
```

### Useful Methods

| Method | Purpose |
|---------|---------|
| `most_common()` | Most frequent elements |
| `elements()` | Repeat elements by count |
| `update()` | Increase counts |
| `subtract()` | Decrease counts |

---

# 2. defaultdict

**Purpose:** Creates missing keys automatically.

**Syntax**

```python
defaultdict(default_factory)
```

**Example**

```python
from collections import defaultdict

marks = defaultdict(int)

marks["Math"] += 90

print(marks)
```

**Output**

```python
defaultdict(<class 'int'>, {'Math': 90})
```

Common factories

| Factory | Default Value |
|----------|---------------|
| `int` | `0` |
| `list` | `[]` |
| `set` | `set()` |
| `str` | `""` |

---

# 3. deque

**Purpose:** Fast insertion and deletion from both ends.

**Syntax**

```python
deque(iterable)
```

### Common Methods

| Method | Purpose |
|---------|---------|
| `append()` | Add right |
| `appendleft()` | Add left |
| `pop()` | Remove right |
| `popleft()` | Remove left |
| `rotate()` | Rotate elements |
| `clear()` | Remove all elements |

---

# 4. namedtuple

**Purpose:** Creates tuples with named fields.

**Syntax**

```python
namedtuple("Name", ["field1", "field2"])
```

**Example**

```python
Student = namedtuple("Student", ["name", "age"])

student = Student("Akhil", 20)

print(student.name)
```

---

# 5. OrderedDict

**Purpose:** Dictionary with additional ordering operations.

**Example**

```python
from collections import OrderedDict

data = OrderedDict()

data["A"] = 10
data["B"] = 20
```

Useful Methods

| Method | Purpose |
|---------|---------|
| `move_to_end()` | Move key to beginning/end |
| `popitem()` | Remove first/last item |

---

# 6. ChainMap

**Purpose:** Combines multiple dictionaries into one view.

**Syntax**

```python
ChainMap(dict1, dict2)
```

**Example**

```python
from collections import ChainMap

a = {"x": 10}
b = {"y": 20}

combined = ChainMap(a, b)
```

---

# Counter vs defaultdict

| Counter | defaultdict |
|----------|-------------|
| Counts elements | Stores default values |
| Best for frequency counting | Best for grouping data |

---

# list vs deque

| list | deque |
|------|-------|
| Slow at beginning | Fast at both ends |
| General-purpose | Queue/Stack operations |

---

# tuple vs namedtuple

| tuple | namedtuple |
|--------|------------|
| Index access | Named field access |
| Less readable | More readable |

---

# dict vs OrderedDict

| dict | OrderedDict |
|------|-------------|
| Maintains insertion order | Extra ordering operations |
| General-purpose | Reordering support |

---

# dict vs ChainMap

| dict | ChainMap |
|------|----------|
| Single dictionary | Multiple dictionaries |
| Stores one mapping | Creates a combined view |

---

# Best Practices

- Use `Counter` for frequency analysis.
- Use `defaultdict` instead of checking missing keys manually.
- Use `deque` for queues and stacks.
- Use `namedtuple` for lightweight records.
- Use `OrderedDict` when reordering keys is required.
- Use `ChainMap` to combine multiple configurations.

---

# Common Mistakes

- Using `list` instead of `deque` for queues.
- Forgetting the default factory in `defaultdict`.
- Treating `namedtuple` like a mutable object.
- Assuming `ChainMap` creates a new dictionary.

---

# When Should I Use This Module?

✅ **Use `collections` when:**

- Counting frequencies
- Grouping data
- Building queues or stacks
- Creating lightweight records
- Combining multiple dictionaries

❌ **Avoid `collections` when:**

- Built-in containers are sufficient for simple tasks.

---

# Quick Revision

| Need | Class |
|------|-------|
| Count items | `Counter` |
| Missing keys | `defaultdict` |
| Queue/Stack | `deque` |
| Named record | `namedtuple` |
| Ordered operations | `OrderedDict` |
| Merge dictionaries | `ChainMap` |