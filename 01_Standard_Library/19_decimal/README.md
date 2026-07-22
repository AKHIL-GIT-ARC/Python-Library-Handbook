# decimal Module

The `decimal` module is a built-in Python library that provides **precise decimal arithmetic**. Unlike the built-in `float` type, it avoids floating-point precision errors, making it ideal for financial and monetary calculations.

---

# Why Use decimal?

Floating-point numbers cannot represent many decimal values exactly.

Example:

```python
print(0.1 + 0.2)
```

Output

```python
0.30000000000000004
```

Using `Decimal`:

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
```

Output

```python
0.3
```

`Decimal` stores decimal values exactly, preventing precision issues.

---

# Importing the Module

```python
from decimal import Decimal
```

or

```python
from decimal import *
```

---

# Functions and Classes Covered

| Function / Class | Purpose |
|------------------|---------|
| `Decimal()` | Create decimal numbers |
| `getcontext()` | Get current decimal context |
| `setcontext()` | Set decimal context |
| `Context.prec` | Set calculation precision |
| `quantize()` | Round decimal values |
| `ROUND_HALF_UP` | Standard financial rounding |
| `ROUND_UP` | Always round upward |
| `ROUND_DOWN` | Always round downward |

---

# Why Learn decimal?

The `decimal` module is commonly used in:

- Banking software
- Accounting systems
- Billing applications
- Tax calculations
- Currency exchange
- E-commerce websites
- Financial reports

---

# Advantages

- Exact decimal arithmetic
- No floating-point precision errors
- Custom precision control
- Multiple rounding modes
- Suitable for financial calculations
- Built into Python

---

# Common Operations

## Creating Decimal Numbers

```python
from decimal import Decimal
price = Decimal("199.99")
tax = Decimal("18.50")
```

---

## Addition

```python
total = price + tax
```

---

## Subtraction

```python
balance = price - tax
```

---

## Multiplication

```python
amount = price * Decimal("2")
```

---

## Division

```python
share = price / Decimal("3")
```

---

## Setting Precision

```python
from decimal import getcontext
getcontext().prec = 5
```

---

## Rounding Values

```python
from decimal import Decimal, ROUND_HALF_UP
price = Decimal("99.987")
rounded = price.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
```

Output

```python
99.99
```

---

# Real-World Applications

## Banking

- Account balance
- Interest calculation
- Transactions

---

## Accounting

- Profit calculation
- Expense reports
- Tax computation

---

## E-Commerce 
- Product prices
- Discounts
- Invoice generation

---

## Payroll

- Salary calculation
- Bonus calculation
- Tax deductions

---

## Currency Conversion

- Exchange rates
- International payments

---

# Prerequisites

Before learning this module, you should know:

- Variables
- Numbers
- Arithmetic operators
- Functions
- Python imports

---

# Mini Project

## Financial Calculator

Features:

- Add money
- Subtract money
- Multiply amount
- Divide amount
- Calculate simple interest
- Round currency
- Compare decimal values

---

# Best Practices

- Always create decimals from **strings** (`Decimal("10.25")`) instead of floats (`Decimal(10.25)`).
- Use `quantize()` for currency values.
- Set precision only when necessary.
- Choose the appropriate rounding mode for your application.
- Use `Decimal` instead of `float` for money-related calculations.

---

# Common Mistakes

- Creating `Decimal` objects directly from `float` values.
- Forgetting to round currency values.
- Mixing `Decimal` and `float` in calculations.
- Assuming the default precision is suitable for all applications.

---

# Quick Revision

| Need | Use |
|------|-----|
| Create decimal | `Decimal()` |
| Get context | `getcontext()` |
| Set precision | `getcontext().prec` |
| Round value | `quantize()` |
| Financial rounding | `ROUND_HALF_UP` |
| Round up | `ROUND_UP` |
| Round down | `ROUND_DOWN` |

---

# What's Next?

In `examples.py`, you'll learn with practical examples covering:

- Creating `Decimal` objects
- Arithmetic operations
- Precision control
- Rounding with `quantize()`
- Different rounding modes
- Comparing decimal values
- Solving floating-point precision problems