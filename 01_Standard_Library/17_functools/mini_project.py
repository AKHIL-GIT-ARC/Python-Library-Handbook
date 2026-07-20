"""
mini_project.py
Module: functools

Smart Utility Toolkit
Demonstrates the practical use of the functools module.
"""
from functools import (
    partial,
    reduce,
    lru_cache,
    cmp_to_key
)

@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def calculate_price(price, discount):
    return price - (price * discount / 100)
discount_20 = partial(calculate_price, discount=20)

def sum_numbers():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    total = reduce(lambda x, y: x + y, numbers)
    print("\nTotal Sum:", total)

def compare_students(a, b):
    if a[1] < b[1]:
        return 1
    if a[1] > b[1]:
        return -1
    return 0

def sort_students():
    students = [
        ("Deepika", 85),
        ("Akhil", 95),
        ("Charan", 91),
        ("Om", 78),
        ("Chitra", 88)
    ]
    students.sort(key=cmp_to_key(compare_students))
    print("\nStudents Sorted By Marks\n")
    for name, marks in students:
        print(f"{name:<10} {marks}")

def compare_products():
    products = [
        ("Laptop", 65000),
        ("Phone", 25000),
        ("Keyboard", 2500),
        ("Mouse", 1200)
    ]
    expensive = reduce(
        lambda x, y: x if x[1] > y[1] else y,
        products
    )
    cheapest = reduce(
        lambda x, y: x if x[1] < y[1] else y,
        products
    )
    print("\nMost Expensive Product")
    print(expensive)
    print("\nCheapest Product")
    print(cheapest)

while True:
    print("\n" + "=" * 40)
    print("       SMART UTILITY TOOLKIT")
    print("=" * 40)
    print("1. Calculate Factorial (Cached)")
    print("2. Apply 20% Discount")
    print("3. Sum Numbers")
    print("4. Sort Students")
    print("5. Compare Products")
    print("6. Exit")

    choice = input("\nEnter Choice: ")
    if choice == "1":
        number = int(input("Enter Number: "))
        print("Factorial:", factorial(number))
    elif choice == "2":
        price = float(input("Enter Product Price: "))
        print("Final Price:", discount_20(price))
    elif choice == "3":
        sum_numbers()
    elif choice == "4":
        sort_students()
    elif choice == "5":
        compare_products()
    elif choice == "6":
        print("\nThank You For Using Smart Utility Toolkit!")
        break
    else:
        print("Invalid Choice!")