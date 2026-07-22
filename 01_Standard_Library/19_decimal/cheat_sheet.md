# decimal Module Cheat Sheet

## Import

```python
from decimal import (
    Decimal,
    getcontext,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_DOWN
)
```
The `decimal` module provides precise decimal arithmetic, making it ideal for financial and monetary calculations.

---

# Functions & Constants Overview

| Function / Constant | Purpose |
|---------------------|---------|
| `Decimal()` | Create a decimal number |
| `getcontext()` | Get current decimal context |
| `getcontext().prec` | Set calculation precision |
| `quantize()` | Round decimal values |
| `ROUND_HALF_UP` | Standard financial rounding |
| `ROUND_UP` | Always round upward |
| `ROUND_DOWN` | Always round downward |

---

# 1. Decimal()

**Purpose:** Creates an exact decimal number.

**Syntax**

```python
Decimal(value)
```

**Example**

```python
from decimal import Decimal
price = Decimal("99.99")
print(price)
```

**Output**

```python
99.99
```

---

# 2. Decimal Arithmetic

### Addition

```python
from decimal import Decimal
a = Decimal("10.5")
b = Decimal("2.5")
print(a + b)
```

**Output**

```python
13.0
```

---

### Subtraction

```python
print(a - b)
```

**Output**

```python
8.0
```

---

### Multiplication

```python
print(a * b)
```

**Output**

```python
26.25
```

---

### Division

```python
print(a / b)
```

**Output**

```python
4.2
```

---

# 3. getcontext()

**Purpose:** Returns the current decimal context.

**Syntax**

```python
getcontext()
```

**Example**

```python
from decimal import getcontext
print(getcontext())
```

---

# 4. Setting Precision

**Purpose:** Controls the number of significant digits.

**Syntax**

```python
getcontext().prec = value
```

**Example**

```python
from decimal import Decimal, getcontext
getcontext().prec = 4
print(Decimal("10") / Decimal("3"))
```

**Output**

```python
3.333
```

---

# 5. quantize()

**Purpose:** Rounds a decimal to a fixed number of decimal places.

**Syntax**

```python
decimal_value.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
```

**Example**

```python
from decimal import Decimal, ROUND_HALF_UP
price = Decimal("99.987")

print(
    price.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
)
```

**Output**

```python
99.99
```

---

# 6. ROUND_HALF_UP

**Purpose:** Standard financial rounding.

**Example**

```python
Decimal("15.125").quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
```

**Output**

```python
15.13
```

---

# 7. ROUND_UP

**Purpose:** Always rounds upward.

**Example**

```python
Decimal("15.121").quantize(
    Decimal("0.01"),
    rounding=ROUND_UP
)
```

**Output**

```python
15.13
```

---

# 8. ROUND_DOWN

**Purpose:** Always rounds downward.

**Example**

```python
Decimal("15.129").quantize(
    Decimal("0.01"),
    rounding=ROUND_DOWN
)
```

**Output**

```python
15.12
```

---

# Float vs Decimal

| float | Decimal |
|--------|----------|
| Precision errors | Exact decimal values |
| Faster | Slightly slower |
| Scientific calculations | Financial calculations |

---

# ROUND_HALF_UP vs ROUND_UP vs ROUND_DOWN

| Mode | Result |
|------|--------|
| `ROUND_HALF_UP` | Standard rounding |
| `ROUND_UP` | Always rounds up |
| `ROUND_DOWN` | Always rounds down |

---

# Precision Example

| Precision | `10 / 3` |
|-----------|----------|
| `4` | `3.333` |
| `10` | `3.333333333` |
| `20` | `3.3333333333333333333` |

---

# Best Practices

- Always create `Decimal` objects using strings.
- Use `Decimal` for financial applications.
- Round currency using `quantize()`.
- Set precision only when necessary.
- Keep all operands as `Decimal` objects.
- Choose the correct rounding mode for your application.

---

# Common Mistakes

❌ Creating `Decimal` from a float

```python
Decimal(0.1)
```

✔ Correct

```python
Decimal("0.1")
```

---

❌ Mixing `float` and `Decimal`

```python
Decimal("10") + 5.5
```

✔ Correct

```python
Decimal("10") + Decimal("5.5")
```

---

❌ Forgetting to round currency

Always use

```python
quantize(Decimal("0.01"))
```
for monetary values.

---

# When Should I Use This Module?

✅ **Use `decimal` when:**

- Banking applications
- Accounting software
- Billing systems
- Tax calculations
- E-commerce
- Currency conversion
- Payroll systems

❌ **Avoid `decimal` when:**

- High-performance scientific computing (prefer NumPy).
- Exact decimal precision is not required.

---

# Quick Revision

| Need | Use |
|------|-----|
| Create decimal | `Decimal()` |
| Get context | `getcontext()` |
| Set precision | `getcontext().prec` |
| Round currency | `quantize()` |
| Financial rounding | `ROUND_HALF_UP` |
| Always round up | `ROUND_UP` |
| Always round down | `ROUND_DOWN` |
| Accurate money calculations | `Decimal` |

---

# Interview Tip

One of the most common Python interview questions is:
**Why should you use `Decimal` instead of `float` for financial calculations?**

**Answer:**
Because `Decimal` provides exact decimal arithmetic and avoids floating-point precision errors, ensuring accurate monetary calculations.