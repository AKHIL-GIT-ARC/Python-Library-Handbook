"""
mini_project.py
Module: decimal

Financial Calculator
Demonstrates the practical use of the decimal module.
"""
from decimal import (
    Decimal,
    ROUND_HALF_UP
)

def get_decimal(message):
    """Safely read a Decimal value from the user."""
    while True:
        try:
            return Decimal(input(message))
        except:
            print("Invalid amount! Please enter a valid number.")

def add_money():
    print("\n--- Add Money ---")
    amount1 = get_decimal("Enter First Amount : ")
    amount2 = get_decimal("Enter Second Amount: ")
    print("Total =", amount1 + amount2)

def subtract_money():
    print("\n--- Subtract Money ---")
    amount1 = get_decimal("Enter First Amount : ")
    amount2 = get_decimal("Enter Second Amount: ")
    print("Difference =", amount1 - amount2)

def multiply_amount():
    print("\n--- Multiply Amount ---")
    amount = get_decimal("Enter Amount : ")
    multiplier = get_decimal("Enter Multiplier: ")
    print("Result =", amount * multiplier)

def divide_amount():
    print("\n--- Divide Amount ---")
    amount = get_decimal("Enter Amount : ")
    divisor = get_decimal("Enter Divisor: ")
    if divisor == Decimal("0"):
        print("Cannot divide by zero.")
        return
    print("Result =", amount / divisor)

def calculate_interest():
    print("\n--- Simple Interest ---")
    principal = get_decimal("Principal Amount : ")
    rate = get_decimal("Interest Rate (%) : ")
    time = get_decimal("Time (Years) : ")
    interest = (
        principal * rate * time
    ) / Decimal("100")
    total = principal + interest
    print("Interest      =", interest)
    print("Total Amount  =", total)

def round_currency():
    print("\n--- Round Currency ---")
    amount = get_decimal("Enter Amount: ")
    rounded = amount.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )
    print("Rounded Amount =", rounded)

def compare_values():
    print("\n--- Compare Values ---")
    amount1 = get_decimal("Enter First Amount : ")
    amount2 = get_decimal("Enter Second Amount: ")
    if amount1 > amount2:
        print(amount1, "is greater.")
    elif amount2 > amount1:
        print(amount2, "is greater.")
    else:
        print("Both values are equal.")

while True:
    print("\n" + "=" * 30)
    print("      FINANCIAL CALCULATOR")
    print("=" * 30)
    print("1. Add Money")
    print("2. Subtract Money")
    print("3. Multiply Amount")
    print("4. Divide Amount")
    print("5. Calculate Interest")
    print("6. Round Currency")
    print("7. Compare Decimal Values")
    print("8. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        add_money()
    elif choice == "2":
        subtract_money()
    elif choice == "3":
        multiply_amount()
    elif choice == "4":
        divide_amount()
    elif choice == "5":
        calculate_interest()
    elif choice == "6":
        round_currency()
    elif choice == "7":
        compare_values()
    elif choice == "8":
        print("\nThank You For Using Financial Calculator!")
        break
    else:
        print("Invalid Choice! Please try again.")