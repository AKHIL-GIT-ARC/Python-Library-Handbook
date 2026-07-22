"""
examples.py
Module: decimal

"""
from decimal import (
    Decimal,
    getcontext,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_DOWN
)

print("=" * 30)
print("   DECIMAL MODULE EXAMPLES")
print("=" * 30)

# -----------------------------------------
# Creating Decimal Objects
# -----------------------------------------

print("\n1. Creating Decimal Objects")
a = Decimal("10.5")
b = Decimal("2.25")
print("a =", a)
print("b =", b)

# -----------------------------------------
# Addition
# -----------------------------------------

print("\n2. Addition")
print(a + b)

# -----------------------------------------
# Subtraction
# -----------------------------------------

print("\n3. Subtraction")
print(a - b)

# -----------------------------------------
# Multiplication
# -----------------------------------------

print("\n4. Multiplication")
print(a * b)

# -----------------------------------------
# Division
# -----------------------------------------

print("\n5. Division")
print(a / b)

# -----------------------------------------
# Floating Point Problem
# -----------------------------------------

print("\n6. Float Precision Problem")
print(0.1 + 0.2)
print("\nUsing Decimal")
print(Decimal("0.1") + Decimal("0.2"))

# -----------------------------------------
# Precision
# -----------------------------------------

print("\n7. Setting Precision")
getcontext().prec = 4
x = Decimal("10")
y = Decimal("3")
print(x / y)

# -----------------------------------------
# Default Precision
# -----------------------------------------

print("\n8. Increasing Precision")
getcontext().prec = 20
print(x / y)

# -----------------------------------------
# Rounding (HALF_UP)
# -----------------------------------------

print("\n9. ROUND_HALF_UP")
price = Decimal("99.987")
rounded = price.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
print(rounded)

# -----------------------------------------
# ROUND_UP
# -----------------------------------------

print("\n10. ROUND_UP")
value = Decimal("15.121")
print(
    value.quantize(
        Decimal("0.01"),
        rounding=ROUND_UP
    )
)

# -----------------------------------------
# ROUND_DOWN
# -----------------------------------------

print("\n11. ROUND_DOWN")
print(
    value.quantize(
        Decimal("0.01"),
        rounding=ROUND_DOWN
    )
)

# -----------------------------------------
# Comparison
# -----------------------------------------

print("\n12. Comparison")
num1 = Decimal("20.50")
num2 = Decimal("20.500")
print(num1 == num2)
print(num1 > Decimal("18"))
print(num2 < Decimal("30"))

# -----------------------------------------
# Currency Calculation
# -----------------------------------------

print("\n13. Currency Calculation")
price = Decimal("499.99")
gst = Decimal("89.99")
total = price + gst
print("Price :", price)
print("GST   :", gst)
print("Total :", total)

# -----------------------------------------
# Discount Calculation
# -----------------------------------------

print("\n14. Discount Calculation")
price = Decimal("1000")
discount = Decimal("15")
final_price = price - (
    price * discount / Decimal("100")
)
print("Final Price =", final_price)

# -----------------------------------------
# Interest Calculation
# -----------------------------------------

print("\n15. Simple Interest")
principal = Decimal("5000")
rate = Decimal("8")
time = Decimal("2")
interest = (
    principal * rate * time
) / Decimal("100")
print("Interest =", interest)
