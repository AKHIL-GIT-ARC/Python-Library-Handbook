# Random Module Cheat Sheet

## Importing the Module

```python
import random
```

The `random` module is built into Python, so no installation is required.

---

# 1. random.random()

### Purpose

Generates a random floating-point number between **0.0** (inclusive) and **1.0** (exclusive).

### Syntax

```python
random.random()
```

### Example

```python
import random

print(random.random())
```

### Possible Output

```
0.483274629
```

### When to Use

- Simulations
- Probability calculations
- Generating random decimal numbers

---

# 2. random.randint(a, b)

### Purpose

Returns a random integer between **a** and **b**, including both endpoints.

### Syntax

```python
random.randint(a, b)
```

### Example

```python
import random

print(random.randint(1, 10))
```

### Possible Output

```
7
```

### Important Note

Both values are included.

```
1 <= number <= 10
```

### Common Uses

- Dice games
- Lottery numbers
- Guessing games

---

# 3. random.randrange(start, stop, step)

### Purpose

Returns a random number from a specified range.

### Syntax

```python
random.randrange(start, stop, step)
```

### Example

```python
print(random.randrange(1, 20, 2))
```

### Possible Output

```
15
```

### Important Note

The **stop** value is NOT included.

```
1,3,5,7,9,11,13,15,17,19
```

---

# 4. random.uniform(a, b)

### Purpose

Returns a random floating-point number between two numbers.

### Syntax

```python
random.uniform(a, b)
```

### Example

```python
print(random.uniform(1,5))
```

### Possible Output

```
3.67291
```

### Common Uses

- Scientific simulations
- Measurements
- Random decimal values

---

# 5. random.choice(sequence)

### Purpose

Selects one random item from a list, tuple, or string.

### Syntax

```python
random.choice(sequence)
```

### Example

```python
fruits=["Apple","Banana","Orange"]

print(random.choice(fruits))
```

### Possible Output

```
Banana
```

### Common Uses

- Random player
- Random question
- Random winner

---

# 6. random.choices(sequence, k=n)

### Purpose

Returns multiple random elements.

Duplicates are allowed.

### Syntax

```python
random.choices(sequence,k=3)
```

### Example

```python
fruits=["Apple","Banana","Orange"]

print(random.choices(fruits,k=3))
```

### Possible Output

```
['Apple','Apple','Orange']
```

Notice duplicates.

---

# 7. random.sample(sequence, k=n)

### Purpose

Returns multiple **unique** elements.

No duplicates.

### Syntax

```python
random.sample(sequence,k=3)
```

### Example

```python
fruits=["Apple","Banana","Orange","Mango"]

print(random.sample(fruits,3))
```

### Possible Output

```
['Banana','Apple','Mango']
```

### Common Uses

- Lottery
- Quiz questions
- Random team selection

---

# 8. random.shuffle(list)

### Purpose

Randomly rearranges a list.

### Syntax

```python
random.shuffle(list)
```

### Example

```python
numbers=[1,2,3,4,5]

random.shuffle(numbers)

print(numbers)
```

### Possible Output

```
[4,1,5,2,3]
```

### Important Note

`shuffle()` changes the original list.

It does NOT return a new list.

---

# 9. random.seed(value)

### Purpose

Produces the same random sequence every time.

### Syntax

```python
random.seed(10)
```

### Example

```python
random.seed(10)

print(random.randint(1,100))
```

Running the program again produces the same result.

### Common Uses

- Machine Learning
- Testing
- Debugging

---

# 10. random.getrandbits(n)

### Purpose

Returns an integer with n random bits.

### Syntax

```python
random.getrandbits(8)
```

### Example

```python
print(random.getrandbits(8))
```

### Possible Output

```
173
```

### Common Uses

- Bit manipulation
- Random binary values

---

# Frequently Used Functions

| Function | Purpose |
|----------|---------|
| random() | Random decimal number |
| randint() | Random integer |
| randrange() | Random integer from range |
| uniform() | Random decimal within range |
| choice() | One random item |
| choices() | Multiple random items (duplicates allowed) |
| sample() | Multiple unique items |
| shuffle() | Shuffle a list |
| seed() | Repeatable random sequence |
| getrandbits() | Random bits |

---

# Interview Tip

## randint() vs randrange()

```python
random.randint(1,5)
```

Output

```
1 2 3 4 5
```

---

```python
random.randrange(1,5)
```

Output

```
1 2 3 4
```

Notice that **randint() includes the last value**, while **randrange() excludes it**.

---

# Best Practice

❌ Don't use the `random` module for passwords or cryptographic purposes.

✅ Use the `secrets` module for secure random values.