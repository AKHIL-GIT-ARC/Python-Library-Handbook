#Scientific Calculator

import math
def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a + b}")
def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a - b}")
def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a * b}")
def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {a / b}")
def square_root():
    num = float(input("Enter a number: "))
    if num < 0:
        print("Square root of a negative number is not possible.")
    else:
        print(f"Result: {math.sqrt(num)}")
def power():
    base = float(input("Enter base: "))
    exponent = float(input("Enter exponent: "))
    print(f"Result: {math.pow(base, exponent)}")
def factorial():
    num = int(input("Enter a positive integer: "))

    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Result: {math.factorial(num)}")
def gcd():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"GCD: {math.gcd(a, b)}")
def lcm():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"LCM: {math.lcm(a, b)}")
def sine():
    angle = float(input("Enter angle in degrees: "))
    print(f"Result: {math.sin(math.radians(angle))}")
def cosine():
    angle = float(input("Enter angle in degrees: "))
    print(f"Result: {math.cos(math.radians(angle))}")
def tangent():
    angle = float(input("Enter angle in degrees: "))
    print(f"Result: {math.tan(math.radians(angle))}")
def logarithm():
    num = float(input("Enter a positive number: "))
    if num <= 0:
        print("Logarithm is only defined for positive numbers.")
    else:
        print(f"Natural Log: {math.log(num)}")
        print(f"Log Base 10: {math.log10(num)}")

while True:
    print("\n======== Scientific Calculator ========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Factorial")
    print("8. GCD")
    print("9. LCM")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Logarithm")
    print("14. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        square_root()
    elif choice == "6":
        power()
    elif choice == "7":
        factorial()
    elif choice == "8":
        gcd()
    elif choice == "9":
        lcm()
    elif choice == "10":
        sine()
    elif choice == "11":
        cosine()
    elif choice == "12":
        tangent()
    elif choice == "13":
        logarithm()
    elif choice == "14":
        print("Thank you for using the Scientific Calculator!")
        break
    else:
        print("Invalid choice. Please try again.")