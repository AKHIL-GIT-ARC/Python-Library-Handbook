# decimal Module Interview Questions

## Beginner Level

### 1. What is the `decimal` module?

**Answer:**

The `decimal` module is a built-in Python library that provides precise decimal arithmetic. It is mainly used in financial and monetary calculations where accuracy is important.

---

### 2. Why is `Decimal` better than `float` for money?

**Answer:**

`Decimal` stores decimal values exactly, while `float` may introduce precision errors.

Example:

```python
print(0.1 + 0.2)
```

Output

```python
0.30000000000000004
```

Using `Decimal`

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
```

Output

```python
0.3
```

---

### 3. How do you create a Decimal object?

**Answer**

```python
from decimal import Decimal
price = Decimal("99.99")
```

---

### 4. Why should Decimal values be created using strings?

**Answer:**

Creating a `Decimal` from a string preserves the exact value, while creating it from a `float` carries over the float's precision error.

---

### 5. Which module provides `Decimal`?

**Answer**

```python
decimal
```

---

## Intermediate Level

### 6. What does `getcontext()` do?

**Answer:**

`getcontext()` returns the current decimal context, including settings such as precision and rounding.

---

### 7. How do you change decimal precision?

**Answer**

```python
from decimal import getcontext
getcontext().prec = 6
```

---

### 8. What is `quantize()` used for?

**Answer:**

`quantize()` rounds a decimal number to a fixed number of decimal places.

Example

```python
price.quantize(Decimal("0.01"))
```

---

### 9. What is `ROUND_HALF_UP`?

**Answer:**

It is the standard financial rounding method where values ending in 5 are rounded away from zero.

Example

```python
Decimal("15.125").quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
```

Output

```python
15.13
```

---

### 10. Name two other rounding modes.

**Answer**

- `ROUND_UP`
- `ROUND_DOWN`

---

## Advanced Level

### 11. Difference between `float` and `Decimal`?

| float | Decimal |
|--------|----------|
| Approximate values | Exact decimal values |
| Faster | Slightly slower |
| Scientific computing | Financial computing |
| Precision errors | No precision errors |

---

### 12. Difference between `ROUND_UP` and `ROUND_DOWN`?

| ROUND_UP | ROUND_DOWN |
|-----------|------------|
| Always rounds upward | Always rounds downward |
| Increases value | Decreases or keeps value |

---

### 13. Can you mix `float` and `Decimal`?

**Answer:**

No. Mixing them raises a `TypeError`. Convert all numeric values to `Decimal` before performing calculations.

---

### 14. Why is `quantize()` important in finance?

**Answer:**

It ensures that currency values are rounded consistently to the required number of decimal places, such as two decimal places for most currencies.

---

### 15. What information does the decimal context contain?

**Answer:**
It stores settings such as:
- Precision
- Rounding mode
- Exponent limits
- Flags
- Traps

---

## Scenario-Based Questions

### 16. You're developing a banking application. Should you use `float` or `Decimal`?

**Answer**

```python
Decimal
```

Because banking applications require exact calculations.

---

### 17. You need to round ₹199.987 to two decimal places. Which method should you use?

**Answer**

```python
quantize()
```

---

### 18. You want to calculate GST accurately. Which data type should you choose?

**Answer**

```python
Decimal
```

---

### 19. You need six significant digits in calculations. What should you change?

**Answer**

```python
getcontext().prec = 6
```

---

### 20. Which rounding mode is commonly used in financial software?

**Answer**

```python
ROUND_HALF_UP
```

---

## Frequently Used Functions

| Function / Constant | Purpose |
|---------------------|---------|
| `Decimal()` | Create decimal values |
| `getcontext()` | Get decimal context |
| `getcontext().prec` | Set precision |
| `quantize()` | Round decimals |
| `ROUND_HALF_UP` | Financial rounding |
| `ROUND_UP` | Always round up |
| `ROUND_DOWN` | Always round down |

---

## Best Practices

- Always create `Decimal` objects from strings.
- Use `Decimal` for financial applications.
- Use `quantize()` to round currency values.
- Set precision only when necessary.
- Keep all operands as `Decimal` objects.
- Use the appropriate rounding mode for your application.

---

## Common Mistakes

- Creating `Decimal` from `float`.
- Mixing `float` and `Decimal`.
- Forgetting to round currency values.
- Assuming `float` is accurate for money.
- Ignoring precision settings in complex calculations.

---
## Quick Revision

| Need | Function |
|------|----------|
| Create decimal | `Decimal()` |
| Get context | `getcontext()` |
| Set precision | `getcontext().prec` |
| Round currency | `quantize()` |
| Financial rounding | `ROUND_HALF_UP` |
| Always round up | `ROUND_UP` |
| Always round down | `ROUND_DOWN` |
| Accurate monetary calculations | `Decimal` |