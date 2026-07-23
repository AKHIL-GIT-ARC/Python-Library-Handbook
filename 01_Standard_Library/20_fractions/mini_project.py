"""
mini_project.py
Module: fractions

Fraction Calculator
Demonstrates the practical use of the fractions module.
"""
from fractions import Fraction
def get_fraction(message):
    """Safely read a fraction from the user."""
    while True:
        try:
            value = input(message)
            return Fraction(value)
        except:
            print("Invalid fraction! Examples: 3/4, 5/6, 2")

def add_fractions():
    print("\n--- Add Fractions ---")
    f1 = get_fraction("Enter First Fraction : ")
    f2 = get_fraction("Enter Second Fraction: ")
    print("Result =", f1 + f2)

def subtract_fractions():
    print("\n--- Subtract Fractions ---")
    f1 = get_fraction("Enter First Fraction : ")
    f2 = get_fraction("Enter Second Fraction: ")
    print("Result =", f1 - f2)

def multiply_fractions():
    print("\n--- Multiply Fractions ---")
    f1 = get_fraction("Enter First Fraction : ")
    f2 = get_fraction("Enter Second Fraction: ")
    print("Result =", f1 * f2)

def divide_fractions():
    print("\n--- Divide Fractions ---")
    f1 = get_fraction("Enter First Fraction : ")
    f2 = get_fraction("Enter Second Fraction: ")
    if f2 == 0:
        print("Cannot divide by zero.")
        return
    print("Result =", f1 / f2)

def simplify_fraction():
    print("\n--- Simplify Fraction ---")
    fraction = get_fraction("Enter Fraction: ")
    print("Simplified Fraction =", fraction)

def compare_fractions():
    print("\n--- Compare Fractions ---")
    f1 = get_fraction("Enter First Fraction : ")
    f2 = get_fraction("Enter Second Fraction: ")
    if f1 > f2:
        print(f1, "is greater.")
    elif f2 > f1:
        print(f2, "is greater.")
    else:
        print("Both fractions are equal.")

while True:
    print("\n" + "=" * 30)
    print("     FRACTION CALCULATOR")
    print("=" * 30)
    print("1. Add Fractions")
    print("2. Subtract Fractions")
    print("3. Multiply Fractions")
    print("4. Divide Fractions")
    print("5. Simplify Fraction")
    print("6. Compare Fractions")
    print("7. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        add_fractions()
    elif choice == "2":
        subtract_fractions()
    elif choice == "3":
        multiply_fractions()
    elif choice == "4":
        divide_fractions()
    elif choice == "5":
        simplify_fraction()
    elif choice == "6":
        compare_fractions()
    elif choice == "7":
        print("\nThank You For Using Fraction Calculator!")
        break
    else:
        print("Invalid Choice! Please try again.")