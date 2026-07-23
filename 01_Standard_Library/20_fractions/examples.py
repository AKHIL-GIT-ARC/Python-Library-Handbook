"""
examples.py
Module: fractions
"""
from fractions import Fraction
from decimal import Decimal
print("=" * 30)
print("  FRACTIONS MODULE EXAMPLES")
print("=" * 30)

# -----------------------------------------
# Creating Fractions
# -----------------------------------------

print("\n1. Creating Fractions")
a = Fraction(3, 4)
b = Fraction(5, 8)
print("a =", a)
print("b =", b)

# -----------------------------------------
# Automatic Simplification
# -----------------------------------------

print("\n2. Automatic Simplification")
fraction = Fraction(12, 18)
print(fraction)

# -----------------------------------------
# Addition
# -----------------------------------------

print("\n3. Addition")
print(a + b)

# -----------------------------------------
# Subtraction
# -----------------------------------------

print("\n4. Subtraction")
print(a - b)

# -----------------------------------------
# Multiplication
# -----------------------------------------

print("\n5. Multiplication")
print(a * b)

# -----------------------------------------
# Division
# -----------------------------------------

print("\n6. Division")
print(a / b)

# -----------------------------------------
# Numerator
# -----------------------------------------

print("\n7. Numerator")
print(a.numerator)

# -----------------------------------------
# Denominator
# -----------------------------------------

print("\n8. Denominator")
print(a.denominator)

# -----------------------------------------
# Fraction Comparison
# -----------------------------------------

print("\n9. Comparison")
x = Fraction(2, 3)
y = Fraction(4, 6)
print(x == y)
print(x > Fraction(1, 2))
print(x < Fraction(3, 4))

# -----------------------------------------
# Convert to Float
# -----------------------------------------

print("\n10. Convert to Float")
print(float(a))

# -----------------------------------------
# Create Fraction from Float
# -----------------------------------------

print("\n11. Fraction from Float")
fraction = Fraction.from_float(0.75)
print(fraction)

# -----------------------------------------
# Create Fraction from Decimal
# -----------------------------------------

print("\n12. Fraction from Decimal")
fraction = Fraction.from_decimal(
    Decimal("2.5")
)
print(fraction)

# -----------------------------------------
# limit_denominator()
# -----------------------------------------

print("\n13. limit_denominator()")
value = Fraction(3.1415926535)
print(value.limit_denominator())

# -----------------------------------------
# Mixed Arithmetic
# -----------------------------------------

print("\n14. Mixed Arithmetic")
num1 = Fraction(1, 2)
num2 = Fraction(3, 5)
result = (
    num1 + num2
) * Fraction(4, 3)
print(result)

# -----------------------------------------
# Fraction to Integer Check
# -----------------------------------------

print("\n15. Whole Number Fraction")
whole = Fraction(10, 5)
print(whole)

# -----------------------------------------
# Summary
# -----------------------------------------

print("\n" + "=" * 20)
print("     SUMMARY")
print("=" * 20)
print("✔ Fraction()")
print("✔ Automatic Simplification")
print("✔ Arithmetic Operations")
print("✔ Numerator")
print("✔ Denominator")
print("✔ Comparison")
print("✔ float()")
print("✔ Fraction.from_float()")
print("✔ Fraction.from_decimal()")
print("✔ limit_denominator()")