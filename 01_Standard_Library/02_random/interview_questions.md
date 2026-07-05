# Interview Questions

## 1. What is the random module?

The random module is a built-in Python module used to generate random numbers and perform random selections.

---

## 2. Difference between randint() and randrange()?

randint(a, b)
- Includes both endpoints.

Example:
random.randint(1, 5)

Possible Output:
1 2 3 4 5

randrange(start, stop)
- Excludes the stop value.

Example:
random.randrange(1, 5)

Possible Output:
1 2 3 4

---

## 3. Difference between choice() and choices()?

choice()
Returns one element.

choices()
Returns multiple elements.

---

## 4. Difference between sample() and choices()?

sample()
Unique values only.

choices()
Duplicates allowed.

---

## 5. What does shuffle() do?

Randomly rearranges a list in place.

---

## 6. What is random.seed()?

Initializes the random number generator to produce reproducible results.

---

## 7. Is the random module secure?

No.

For secure random values, use the secrets module.

---

## 8. What is getrandbits()?

Returns an integer with the specified number of random bits.

---

## 9. Which function is used to generate floating-point numbers?

random.random()

random.uniform()

---

## 10. Name five commonly used functions.

- random()
- randint()
- choice()
- sample()
- shuffle()