# collections Module

The `collections` module provides specialized container data types that extend Python's built-in containers like `list`, `tuple`, and `dict`. These data types simplify common programming tasks, improve code readability, and often provide better performance.

---

# Why Use collections?

Without `collections`, many tasks require extra code.

Example:

```python
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
```

Using `Counter`:

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(words)

print(count)
```

Cleaner, shorter, and easier to understand.

---

# Main Classes

| Class | Purpose |
|--------|---------|
| `Counter` | Counts occurrences of elements |
| `defaultdict` | Dictionary with default values |
| `deque` | Double-ended queue for fast insertions/removals |
| `namedtuple` | Tuple with named fields |
| `OrderedDict` | Dictionary with additional ordering operations |
| `ChainMap` | Combines multiple dictionaries into one view |

---

# Frequently Used Classes

## 1. Counter

Counts how many times each element appears.

```python
from collections import Counter

Counter(["a", "b", "a"])
```

Output

```python
Counter({'a': 2, 'b': 1})
```

---

## 2. defaultdict

Automatically creates default values for missing keys.

```python
from collections import defaultdict

marks = defaultdict(int)

marks["Math"] += 10

print(marks)
```

Output

```python
defaultdict(<class 'int'>, {'Math': 10})
```

---

## 3. deque

Fast insertion and deletion from both ends.

```python
from collections import deque

queue = deque([1, 2, 3])

queue.append(4)
queue.appendleft(0)

print(queue)
```

Output

```python
deque([0, 1, 2, 3, 4])
```

---

## 4. namedtuple

Creates tuples with named fields.

```python
from collections import namedtuple

Student = namedtuple("Student", ["name", "age"])

student = Student("Akhil", 20)

print(student.name)
```

Output

```python
Akhil
```

---

## 5. OrderedDict

Dictionary with extra ordering features.

```python
from collections import OrderedDict

data = OrderedDict()

data["A"] = 10
data["B"] = 20

print(data)
```

---

## 6. ChainMap

Combines multiple dictionaries.

```python
from collections import ChainMap

dict1 = {"a": 1}
dict2 = {"b": 2}

combined = ChainMap(dict1, dict2)

print(combined["a"])
print(combined["b"])
```

Output

```python
1
2
```

---

# Advantages

- Less code
- Better readability
- Faster operations
- Built into Python
- Ideal for interviews
- Widely used in real-world applications

---

# Real-World Applications

| Class | Example |
|--------|---------|
| Counter | Word frequency analysis |
| defaultdict | Grouping students by department |
| deque | Browser history, queues, undo/redo |
| namedtuple | Employee and student records |
| OrderedDict | LRU Cache, configuration data |
| ChainMap | Combining multiple configuration files |

---

# Module Summary

| Class | Best Used For |
|--------|---------------|
| Counter | Counting items |
| defaultdict | Missing keys |
| deque | Queue/Stack operations |
| namedtuple | Readable tuples |
| OrderedDict | Ordered dictionary operations |
| ChainMap | Multiple dictionaries |

---

# Prerequisites

Before learning this module, you should know:

- Lists
- Tuples
- Dictionaries
- Loops
- Functions

---

# Mini Project

In this module, you'll build a **Library Inventory Analyzer** using multiple classes from the `collections` module.

Features:

- Count books by category
- Manage a borrowing queue
- Store book records
- Merge multiple library catalogs

---

# Learning Outcomes

After completing this module, you'll be able to:

- Count data efficiently using `Counter`
- Handle missing dictionary keys with `defaultdict`
- Implement queues and stacks using `deque`
- Create readable records using `namedtuple`
- Work with ordered dictionaries
- Combine multiple dictionaries with `ChainMap`