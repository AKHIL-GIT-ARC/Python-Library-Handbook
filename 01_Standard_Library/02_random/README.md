# Random Module

## Introduction

The `random` module is a built-in Python library used to generate random numbers, select random elements, shuffle data, and perform random sampling.

It is widely used in:

- Game Development
- Simulations
- Password Generation
- Machine Learning (Data Shuffling)
- Testing
- Cryptography (basic use only; not for secure applications)

---

## Import

```python
import random
```

---

## Topics Covered

- random()
- randint()
- randrange()
- uniform()
- choice()
- choices()
- sample()
- shuffle()
- seed()
- getrandbits()

---

## Mini Project – Random Utility Toolkit

This project demonstrates the practical usage of Python's `random` module by providing a menu-driven utility application.

### Features

- 🎲 Dice Roller
- 🪙 Coin Toss
- 🔐 Random Password Generator
- 🎟 Lottery Number Generator
- 🎓 Random Student Picker
- 👥 Random Team Generator
- 📈 Random Decimal Number Generator

### Concepts Used

- Functions
- Loops
- Conditional Statements
- Lists
- Strings
- User Input
- Python `random` module

### Functions Used

- `random.randint()`
- `random.choice()`
- `random.choices()`
- `random.sample()`
- `random.shuffle()`
- `random.uniform()`
---

## Best Practices

- Use `random.randint()` for random integers.
- Use `random.choice()` to select a single item.
- Use `random.sample()` when you don't want duplicate selections.
- Use `random.shuffle()` to shuffle lists.
- Do **not** use the `random` module for security-sensitive tasks. Use the `secrets` module instead.

---

## Common Mistakes

- Confusing `randint()` and `randrange()`
- Expecting `shuffle()` to return a new list (it modifies the original list)
- Using `random` for password generation in production